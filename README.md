# What are the best Systems? New Perspectives on NLP Benchmarking

In Machine Learning, a benchmark refers to an ensemble of datasets associated with one or multiple metrics together with a way to aggregate different systems performances. They are instrumental in {\it (i)}  assessing the progress of new methods along different axes and {\it (ii)} selecting the best systems for practical use. This is particularly the case for NLP with the development of large pre-trained models (\textit{e.g.} GPT, BERT) that are expected to generalize well on a variety of tasks. While the community mainly focused on developing new datasets and metrics, there has been little interest in the aggregation procedure, which is often reduced to a simple average over various performance measures. However, this procedure can be problematic when the metrics are on a different scale, which may lead to spurious conclusions. This paper proposes a new procedure to rank systems based on their performance across different tasks. Motivated by the social choice theory, the final system ordering is obtained through aggregating the rankings induced by each task and is theoretically grounded. We conduct extensive numerical experiments (on over 270k scores) to assess the soundness of our approach both on synthetic and real scores (\textit{e.g.} GLUE, EXTREM, SEVAL, TAC, FLICKR). In particular, we show that our method yields different conclusions on state-of-the-art systems than the mean-aggregation procedure while being both more reliable and robust.




#### Authors:

* [Pierre Colombo](https://scholar.google.com/citations?user=yPoMt8gAAAAJ&hl=fr)
* [Nathan Noiry](https://noiry.perso.math.cnrs.fr/)
* [Ekhine Irurozki](https://scholar.google.com/citations?user=thlVrqIAAAAJ&hl=es)

## Goal :

This repository deals with automatic evaluation of NLG and addresses the special case of reference based evaluation. The goal is to build a metric m: <img src="https://render.githubusercontent.com/render/math?math=m : \mathcal{S} \times \mathcal{S} \rightarrow \mathcal{R}"> where <img src="https://render.githubusercontent.com/render/math?math=m : \mathcal{S}"> is the space of sentences. An example is given below:



## Overview

We start by giving an overview of the proposed methods.

[counter_example.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030618/counter_example.pdf)

[draw_table.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030621/draw_table.pdf)

### Toy Data

[robust2.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030632/robust2.pdf)


### Aggregation when Task Level Information is available


[one_level_ranking_glue.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030643/one_level_ranking_glue.pdf)
[one_level_ranking_superglue.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030644/one_level_ranking_superglue.pdf)
[one_level_ranking_xtrem.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030645/one_level_ranking_xtrem.pdf)



### Aggregation when Instance Level Information is available

[draw_table_2.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030626/draw_table_2.pdf)


[two_level_ranking_FLICKR.csv.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030650/two_level_ranking_FLICKR.csv.pdf)
[two_level_ranking_REAL_SUM.csv.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030653/two_level_ranking_REAL_SUM.csv.pdf)
[two_level_ranking_DIALOG_pc.csv.pdf](https://github.com/PierreColombo/RankingNLPSystems/files/8030655/two_level_ranking_DIALOG_pc.csv.pdf)




### Reproducing the paper results

See notebooks.


## References

If you find this repo useful, please cite our papers:

```
@article{,
  title={},
  author={},
  journal={},
  year={2022}
}

```

## Usage

### Python Function

Running our ranking is require a simple cpu. 

We provide example inputs under `<>.py`. For example for BaryScore

```

```

### Command Line Interface (CLI)

We provide a command line interface (CLI) of BERTScore as well as a python module. For the CLI, you can use it as
follows:

``` 
# TASK LEVEL INFORMATION
export PATH_TO_DF_TO_RANK=sample_df/glue.csv
export MODE=task_level

python ranking_cli.py --df_to_rank=$PATH_TO_DF_TO_RANK --mode=$MODE

# INSTANCE LEVEL INFORMATION
export PATH_TO_DF_TO_RANK=sample_df/TAC_08.csv
export MODE=instance_level
python ranking_cli.py --df_to_rank=$PATH_TO_DF_TO_RANK --mode=$MODE
```

See more options by `python score_cli.py -h`.


## Acknowledgements

This work was granted access
to the HPC resources of IDRIS under the allocation 2021-
101838 made by GENCI. Nathan is funded by the projet
ANR LIMPID.
