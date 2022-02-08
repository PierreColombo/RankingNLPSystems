import numpy as np
import pandas as pd
import itertools
import scipy.stats as stats
import scipy


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
