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
<figcaption> Kemeny Conscensus </figcaption>
    </div>
</figure>
</div>



### Aggregation when Task Level Information is available


<div sstyle="width:100%">
    <figure class="left" >
    <img class="top" style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154021-8108dfa9-b51c-44c4-8434-a65597d5c29b.png"/>
    <figcaption> Fig1. Production value and quantity of the 10 top commodities </figcaption>
    </figure>

    <figure class="right">
    <img class="average" style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154021-8108dfa9-b51c-44c4-8434-a65597d5c29b.png"/>
    <figcaption> Fig2. Averages per metric ton </figcaption>
    </figure>
</div>

<figure class="left">
  <img class="top" src="https://user-images.githubusercontent.com/22492839/153154021-8108dfa9-b51c-44c4-8434-a65597d5c29b.png" style="width:50%"/>
  <figcaption> SuperGLUE </figcaption>
</figure>

<figure class="right">
  <img class="average" src="https://user-images.githubusercontent.com/22492839/153154028-00f1f10b-4248-45df-81a3-30b4748a54e6.png" style="width:50%"/>
  <figcaption> XTREM </figcaption>
</figure>


### Toy Data

<div align="center">
<figure>
    <img style="width:50%" src="https://user-images.githubusercontent.com/22492839/153154032-3863595c-e801-4cc9-b3c5-544a97e6ad54.png">
    <div align="center">
<figcaption> Toy Example </figcaption>
    </div>
</figure>
</div>





### Aggregation when Instance Level Information is available

![draw_table_2-1](https://user-images.githubusercontent.com/22492839/153154016-a9848d0d-7eaf-4526-82dc-634e1b1e4fdf.png)

![two_level_ranking_DIALOG_pc csv-1](https://user-images.githubusercontent.com/22492839/153154035-369da055-573c-4bad-9b55-31c90dd83c2c.png)
![two_level_ranking_FLICKR csv-1](https://user-images.githubusercontent.com/22492839/153154038-d8cd9570-0692-44f4-8dd8-0d02692bf09d.png)
![two_level_ranking_REAL_SUM csv-1](https://user-images.githubusercontent.com/22492839/153154042-adddccdc-81a7-46cf-91d0-9c9d18fffe08.png)



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
