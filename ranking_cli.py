import os
import argparse
import logging
import sys
from utils import *
import pandas as pd

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO)


def perm_to_rank(systems, mean_rank):
    return [systems[mean_rank.tolist().index(i)] for i in range(len(mean_rank))][::-1]


def main():
    ####################
    # Common Arguments #
    ####################
    parser = argparse.ArgumentParser("Compute Different Aggregation")
    parser.add_argument("--df_to_rank", default="sample_df/glue.csv", type=str, required=False,
                        help="dataframe to rank")
    parser.add_argument("--mode", type=str, default="task_level",
                        choices=['task_level', 'instance_level'],
                        help="Which level of aggregation is available")

    parser.add_argument("--path_to_save", type=str, default=None,
                        help="Where to save the dataframe, if None saving in the same file")

    args = parser.parse_args()
    logging.info("Computing Different Aggregation {}".format(args.df_to_rank))
    logging.info("**** Level of information available is {}".format(args.mode))

    try:
        df_to_rank = pd.read_csv(args.df_to_rank)
        logging.info("Files opened Starting To Rank")
    except:
        logging.info("Error while loading the file ! Please check it !")
        sys.exit(1)

    if args.mode == 'task_level':
        systems = df_to_rank.Model.values.tolist()
        mean_rank, mean_scores = mean_aggregation_task_level(df_to_rank)
        one_level_rank, one_level_borda_scores = ranking_aggregation(df_to_rank, return_count=True)
        logging.info('In our paper we advise to use the 1 level ranking')
        logging.info('Example:   [7, 2, ...] reads S0 is ranked 7th, S1 is ranked 2nd, etc')
        logging.info('Results of the mean ranking {} : {}'.format(mean_rank, mean_scores))
        logging.info('Results of the 1 level ranking {} : {}'.format(one_level_rank, one_level_borda_scores))

        logging.info('*********** Final Results ***********')
        logging.info('Mean ranking : {}'.format(perm_to_rank(systems, mean_rank)))
        logging.info('1 level ranking : {}'.format(perm_to_rank(systems, one_level_rank)))
    elif args.mode == 'instance_level':
        systems = df_to_rank.System.values.tolist()
        df_to_rank = df_to_rank.set_index(['System', 'Utterance'])  # this step is important
        mean_rank, mean_scores = mean_aggregation_instance_level(df_to_rank)
        one_level_rank, one_level_borda_scores = direct_aggregation(df_to_rank, return_count=True)
        two_level_rank, two_level_borda_scores = two_levels_aggregation(df_to_rank, return_count=True)
        logging.info('In our paper we advise to use the 2 level ranking')
        logging.info('*********** Results ***********')
        logging.info('Example:   [7, 2, ...] reads S0 is ranked 7th, S1 is ranked 2nd, etc')
        logging.info('Results of the mean ranking {} : {}'.format(mean_rank, mean_scores))
        logging.info('Results of the 1 level ranking {} : {}'.format(one_level_rank, one_level_borda_scores))
        logging.info('Results of the 2 level ranking {} : {}'.format(two_level_rank, two_level_borda_scores))

        logging.info('*********** Final Results ***********')
        logging.info('Mean ranking : {}'.format(perm_to_rank(systems, mean_rank)))
        logging.info('1 level ranking : {}'.format(perm_to_rank(systems, one_level_rank)))
        logging.info('2 level ranking : {}'.format(perm_to_rank(systems, two_level_rank)))

    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
