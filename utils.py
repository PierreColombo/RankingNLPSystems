import numpy as np
import pandas as pd
import itertools
import scipy.stats as stats
import scipy


def reverse_ranking(sigma):
    """
    :param sigma: permutation
    :return: the associated ranking
    """
    if not isinstance(sigma, list):
        sigma = sigma.tolist()
    final_ranking = []
    for i in range(len(sigma)):
        final_ranking.append(sigma.index(i))
    return np.array(final_ranking)


def kendallTau(A, B):
    pairs = itertools.combinations(range(0, len(A)), 2)

    distance = 0

    for x, y in pairs:
        a = A[x] - A[y]
        b = B[x] - B[y]

        # if discordant (different signs)
        if (a * b < 0):
            distance += 1

    return distance


def scores_by_utterances(df, metric):
    # get scores by utterances
    # return array of size (nb of utterances, nb of systems),
    # where row i contains scores of systems for utterance i.
    # Note for the future: easier to use pd.IndexSlice instead
    # of the loops.

    utterances = []
    scores = []
    for sys, ut in df.index:
        if ut not in utterances:
            utterances.append(ut)
            scores.append([])
        n_ut = utterances.index(ut)
        scores[n_ut].append(df.loc[(sys, ut)][metric])
    return np.array(scores)


def rankings_by_utterances(df, metric):
    # return array of size (nb of utterances, nb of systems),
    # where row i corresponds to the ranking of systems according
    # to their perfomances on utterance i.
    # NB: the ranking is in decreasing order meaning that
    # [40, 3, 2, ...] reads: S0 is ranked 40, S1 is ranked 3, etc

    # get scores
    scores = scores_by_utterances(df, metric)

    # compute rankings
    rankings = []
    for score in scores:
        r = np.argsort(np.argsort(score))
        rankings.append(r)
    return np.array(rankings)


def borda_aggregation_metric(df, metric):
    rankings = np.array(rankings_by_utterances(df, metric))
    # each row of rankings is an utterance, each column is a system
    # we sum the ranks obtained by each system, that is along axis 0
    borda_count = rankings.sum(axis=0)  # array of size nb_systems with cumulated ranks
    borda_aggr = np.argsort(np.argsort(borda_count))
    return borda_aggr


def two_levels_aggregation(df, return_count=False):
    # return the rankings of the systems
    # [7, 2, ...] reads S0 is ranked 7th, S1 is ranked 2nd, etc
    # rmk: the best system is the argmin

    rankings_by_metrics = []
    for metric in df.columns:
        rankings_by_metrics.append(borda_aggregation_metric(df, metric))
    r = np.array(rankings_by_metrics)
    borda_count = r.sum(axis=0)
    borda_aggr = np.argsort(np.argsort(borda_count))
    if return_count:
        return borda_aggr, borda_count
    else:
        return borda_aggr


def direct_aggregation(df, return_count=False):
    utterances = np.unique(np.array(df.index.get_level_values(1)))
    rankings = []
    for ut in utterances:
        for metric in df.columns:
            scores_ut_metric = df.loc[pd.IndexSlice[:, ut], metric].values
            ranks = np.argsort(np.argsort(scores_ut_metric))
            rankings.append(ranks)
    rankings = np.array(rankings)
    borda_count = rankings.sum(axis=0)
    borda_aggr = np.argsort(np.argsort(borda_count))
    if return_count:
        return borda_aggr, borda_count
    else:
        return borda_aggr


def mean_aggregation_instance_level(df):
    # return the rankings of the systems when considering the mean
    means = df.groupby('System').mean().mean(axis=1).values
    return np.argsort(np.argsort(means)), means


def mean_aggregation_task_level(input_df):
    """
    :param input_df: input dataframe
    :return: rank obtained via mean, mean scores
    """
    means = input_df.mean(axis=1, numeric_only=True).values
    return np.argsort(np.argsort(means)), means


def ranking_aggregation(input_df, return_count=False):
    """
    :param input_df: input dataframe
    :param return_count: if True return borda count
    :return: rank obtained via borda count, borda count scores
    """
    rankings = []
    for index, columns in input_df.iteritems():
        if index != 'Model':
            rankings.append(columns.argsort().argsort().values)

    df_ranking = np.argsort(np.argsort(sum(rankings)))
    if return_count:
        return df_ranking, sum(rankings)
    else:
        return df_ranking


def kendall_tau_distance(order_a, order_b):
    """
    :param order_a: ranking A
    :param order_b: ranking B
    :return: Kendall distance
    """
    pairs = itertools.combinations(range(0, len(order_a)), 2)
    distance = 0
    for x, y in pairs:
        a = order_a.index(x) - order_a.index(y)
        b = order_b.index(x) - order_b.index(y)
        if a * b < 0:
            distance += 1
    return distance


def distorsion_measure(reference_ranking, list_of_rankings):
    distorsion_measure = []
    for ranking in list_of_rankings:
        distorsion_measure.append(kendall_tau_distance(reference_ranking, ranking))
    return sum(distorsion_measure) / len(distorsion_measure)


def interection_length(list1, list2):
    """
    :param list1: list 1
    :param list2: list 2
    :return: number of agrement between list 1 and list 2
    """
    return len(list(set(list1).intersection(list2)))


def compute_correlation(df, human, metric):
    """
    df: considered matrix M
    human: human annotation name to compute correlation with
    metric: metric name to compute correlation with
    """
    ##################
    ## System Level ##
    ##################
    hum_metric = df[human].groupby('System').mean().values
    sys_metric = df[metric].groupby('System').mean().values
    final_dic = {'$S_\\rho$': stats.pearsonr(hum_metric, sys_metric)[0],
                 '$S_p$': stats.spearmanr(hum_metric, sys_metric)[0],
                 '$S_\\tau$': stats.kendalltau(hum_metric, sys_metric)[0],
                 '$T_\\rho$': [], '$T_p$': [], '$T_\\tau$': []}

    ################
    ## Text Level ##
    ################
    for (_, df_h), (_, df_m) in zip(df[human].groupby(level=0), df[metric].groupby(level=0)):
        if stats.pearsonr(df_h.values, df_m.values)[1] < 0.05:
            final_dic['$T_p$'].append(stats.pearsonr(df_h.values, df_m.values)[0])
        if stats.spearmanr(df_h.values, df_m.values)[1] < 0.05:
            final_dic['$T_\\rho$'].append(stats.spearmanr(df_h.values, df_m.values)[0])
        if scipy.stats.kendalltau(df_h.values, df_m.values)[1] < 0.05:
            final_dic['$T_\\tau$'].append(stats.kendalltau(df_h.values, df_m.values)[0])
    final_dic['$T_p$'] = sum(final_dic['$T_p$']) / len(final_dic['$T_p$'])
    final_dic['$T_\\rho$'] = sum(final_dic['$T_\\rho$']) / len(final_dic['$T_\\rho$'])
    final_dic['$T_\\tau$'] = sum(final_dic['$T_\\tau$']) / len(final_dic['$T_\\tau$'])

    return final_dic
