# What are the best Systems? New Perspectives on NLP Benchmarking

In Machine Learning, a benchmark refers to an ensemble of datasets associated with one or multiple metrics together with a way to aggregate different systems performances. They are instrumental in  (i)  assessing the progress of new methods along different axes and (ii) selecting the best systems for practical use. This is particularly the case for NLP with the development of large pre-trained models (e.g GPT, BERT) that are expected to generalize well on a variety of tasks. While the community mainly focused on developing new datasets and metrics, there has been little interest in the aggregation procedure, which is often reduced to a simple average over various performance measures. However, this procedure can be problematic when the metrics are on a different scale, which may lead to spurious conclusions. This paper proposes a new procedure to rank systems based on their performance across different tasks. Motivated by the social choice theory, the final system ordering is obtained through aggregating the rankings induced by each task and is theoretically grounded. We conduct extensive numerical experiments (on over 270k scores) to assess the soundness of our approach both on synthetic and real scores (e.g GLUE, EXTREM, SEVAL, TAC, FLICKR). In particular, we show that our method yields different conclusions on state-of-the-art systems than the mean-aggregation procedure while being both more reliable and robust.




#### Authors:

* [Pierre Colombo](https://scholar.google.com/citations?user=yPoMt8gAAAAJ&hl=fr)
* [Nathan Noiry](https://noiry.perso.math.cnrs.fr/)
* [Ekhine Irurozki](https://scholar.google.com/citations?user=thlVrqIAAAAJ&hl=es)

## Goal :

This repository aims at answering the question What are the best systems? when given a table of score. Concretly, we aim at finding an aggregation procedure that orders the systems and that is better than the widely used mean average. We propose to use the Borda Count.

This repository provide a CLI tool to do that while requiring a single CPU.


## Overview

### Limitations of Mean Aggregation


Taking the mean aggregation, is seriously flawed since the differen metrics on different task are usually not on the same scales and can even be unbounded. Thus even a pre-processing renormalization scheme would fail to capture the intrinsic difficulty of the tasks.

A naive alternative is to rely on pairwise ranking. However, the example below shows that pairwise rankings can be paradoxical.
Mean aggregation outputs A > B > C while pairwise ranking considered fails to rank the systems and produce B > A, C > B, A = C. Our method does not have this flaw and outputs C > B > A.



<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153153946-ea7b94cb-ed2d-496c-9c3b-bab712368191.png">
    <div align="center">
<figcaption> Counter Example </figcaption>
    </div>
</figure>
</div>

### Ranking when Task Level information is available using Kemeny Conscencus


In this setting, one has access to the scores of N systems across T tasks. Each task t being associated with a metric and a test set. For every n and every t, we  only have access to the aggregated performance of system n on task t


<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154009-3bde1420-7104-43ef-a71c-fd648cd2cc6e.png">
    <div align="center">
<figcaption> Kemeny Conscensus when Task Level Information is available </figcaption>
    </div>
</figure>
</div>

When using ranking to aggregate the score a natural choice is to rely on Kemeny consensus aggregation. This procedure is the only rule that satisfies three natural properties: neutrality, meaning that it does not depend on the order of the tasks; consistency, and the Condorcet criterion, meaning that an item
wining all its pairwise comparison is ranked fist. Moreover,
the Kemeny consensus is also the maximum likelihood of
the widely-used Mallows statistical on the symmetric group.



### Ranking Analysis

Our method can be used to rank models. As you can see below on two famous NLP benchmark when changing the aggregation function, the response to our initial question ”what are the best systems?” varies.

<div align="center">
<figure>
<img  style="width:50%"  src="https://user-images.githubusercontent.com/22492839/157666940-4dc58b96-45a0-4a3f-80e3-50e29cc40fb2.png">
        <div align="center">
<figcaption> Ranking Analysis </figcaption>
    </div>
</figure>
</div>



## Aggregation when Instance Level Information is available

The second setting of interrest is when for every n, every t and every k, access to the aggregated performance of system n on instance k of task t. In this setting, we recommand to do 2 levels of Borda count. 


<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154016-a9848d0d-7eaf-4526-82dc-634e1b1e4fdf.png">
    <div align="center">
<figcaption> Kemeny Conscensus when Task Level Information is available </figcaption>
    </div>
</figure>
</div>




## Reproducing the paper results

See notebooks.


## References

If you find this repo useful, please cite our papers:

```
@article{colombo2022best,
  title={What are the best systems? New perspectives on NLP Benchmarking},
  author={Colombo, Pierre and Noiry, Nathan and Irurozki, Ekhine and Clemencon, Stephan},
  journal={arXiv preprint arXiv:2202.03799},
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
