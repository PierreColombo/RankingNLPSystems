# What are the best Systems? New Perspectives on NLP Benchmarking

In Machine Learning, a benchmark refers to an ensemble of datasets associated with one or multiple metrics together with a way to aggregate different systems performances. They are instrumental in {\it (i)}  assessing the progress of new methods along different axes and {\it (ii)} selecting the best systems for practical use. This is particularly the case for NLP with the development of large pre-trained models (\textit{e.g.} GPT, BERT) that are expected to generalize well on a variety of tasks. While the community mainly focused on developing new datasets and metrics, there has been little interest in the aggregation procedure, which is often reduced to a simple average over various performance measures. However, this procedure can be problematic when the metrics are on a different scale, which may lead to spurious conclusions. This paper proposes a new procedure to rank systems based on their performance across different tasks. Motivated by the social choice theory, the final system ordering is obtained through aggregating the rankings induced by each task and is theoretically grounded. We conduct extensive numerical experiments (on over 270k scores) to assess the soundness of our approach both on synthetic and real scores (\textit{e.g.} GLUE, EXTREM, SEVAL, TAC, FLICKR). In particular, we show that our method yields different conclusions on state-of-the-art systems than the mean-aggregation procedure while being both more reliable and robust.




#### Authors:

* [Pierre Colombo](https://scholar.google.com/citations?user=yPoMt8gAAAAJ&hl=fr)
* [Nathan Noiry](https://noiry.perso.math.cnrs.fr/)
* [Ekhine Irurozki](https://scholar.google.com/citations?user=thlVrqIAAAAJ&hl=es)

## Goal :

This repository deals with automatic evaluation of NLG and addresses the special case of reference based evaluation. The goal is to build a metric m: <img src="https://render.githubusercontent.com/render/math?math=m : \mathcal{S} \times \mathcal{S} \rightarrow \mathcal{R}"> where <img src="https://render.githubusercontent.com/render/math?math=m : \mathcal{S}"> is the space of sentences. An example is given below:



## Overview

### Limitations of Mean Aggregation

<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153153946-ea7b94cb-ed2d-496c-9c3b-bab712368191.png">
    <div align="center">
<figcaption> Counter Example </figcaption>
    </div>
</figure>
</div>

### Kemeny Conscensus based Aggregation

<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154009-3bde1420-7104-43ef-a71c-fd648cd2cc6e.png">
    <div align="center">
<figcaption> Kemeny Conscensus when Task Level Information is available </figcaption>
    </div>
</figure>
</div>



### Aggregation when Task Level Information is available


### Toy Data

<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154032-3863595c-e801-4cc9-b3c5-544a97e6ad54.png">
    <div align="center">
<figcaption> Toy Example </figcaption>
    </div>
</figure>
</div>


### Robustness Analysis
<div align="center">
<figure>
<img  style="width:50%"  src="https://user-images.githubusercontent.com/22492839/157666912-09dbe8b4-da95-48e1-b054-2a35f7b41b15.png">
        <div align="center">
<figcaption> Robustness Analysis </figcaption>
    </div>
</figure>
</div>


### Ranking Analysis

<div align="center">
<figure>
<img  style="width:50%"  src="https://user-images.githubusercontent.com/22492839/157666940-4dc58b96-45a0-4a3f-80e3-50e29cc40fb2.png">
        <div align="center">
<figcaption> Ranking Analysis </figcaption>
    </div>
</figure>
</div>



## Aggregation when Instance Level Information is available


<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154016-a9848d0d-7eaf-4526-82dc-634e1b1e4fdf.png">
    <div align="center">
<figcaption> Kemeny Conscensus when Task Level Information is available </figcaption>
    </div>
</figure>
</div>

### Robustness Analysis


<div align="center">
<figure>
<img  style="width:50%"   src="https://user-images.githubusercontent.com/22492839/157667196-1698a4ec-df22-4d7a-8a9b-4ac11eadff60.png">
        <div align="center">
<figcaption> Robustness Analysis With Instance Level Information </figcaption>
    </div>
</figure>
</div>

### Rank Analysis

<div align="center">
<figure>
<img  style="width:50%"   src="https://user-images.githubusercontent.com/22492839/157667235-5bd3260c-78fc-408f-842a-668fb2b3213a.png">
        <div align="center">
<figcaption> Ranking Analysis With Instance Level Information </figcaption>
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
