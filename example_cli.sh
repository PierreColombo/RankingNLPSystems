
export PATH_TO_DF_TO_RANK=sample_df/glue.csv
export MODE=task_level

python ranking_cli.py --df_to_rank=$PATH_TO_DF_TO_RANK --mode=$MODE


export PATH_TO_DF_TO_RANK=sample_df/TAC_08.csv
export MODE=instance_level
python ranking_cli.py --df_to_rank=$PATH_TO_DF_TO_RANK --mode=$MODE