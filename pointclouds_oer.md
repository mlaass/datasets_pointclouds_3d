---
title: A list of 3d pointcloud datasets
author: Moritz Laass <moritz.laass@tum.de>
license: CC-BY-SA
classified: internal
license: undefined
path: /data/pointclouds3d/
editlink: 
---

### TL;DR
This document provides a curated list of 3d pointcloud datasets used in our research.

### Qualification Goal
In this article, get an overview of the datasets 
- The sources and original formats
- The processing used top extract them into h5
- How to use them in your own research

# Introduction
Please describe what someone would learn by working through your OER in no more than one sentence. Also formulate expectations in very concise form, preferably linking to educational resources providing the skills.

# Datasets
| Name  | File | Size | Pointclouds | pts/pc| Total pts | RGB | Source Format | | Source|
| ---- | ----- | ----- | ------ | ------- | ------- | ------- | ------- | ------- | ------- | 
|mi3dmap |mi3dmap.h5| 707M | 4 |2.1M - 11.1M| 30.9M | false | .las | http://mi3dmap.net/datatype1.jsp |
|ModelNet10 | modelnet10_10k.h5 | 571M| 4899| 10k|49M| false| .off | https://modelnet.cs.princeton.edu/ |
|ModelNet40  | modelnet40_10k.h5| 1.5G| 12311| 10k|123M| false| .off | https://modelnet.cs.princeton.edu/ |
|scanobjectnn  | scanobjectnn.h5 |  3.8G | 2902| 1.52k - 1.17M| 269M| true| numpy .bin | https://hkust-vgd.github.io/scanobjectnn/ |
|scanobjectnn with backgrounds| scanobjectnn_with_bg.h5 |  6.2G | 2902| 2.09k - 2.74M| 438M| true | numpy .bin | https://hkust-vgd.github.io/scanobjectnn/ |
|SensatUrban  | sensat_urban.h5 |  39G | 42| 201k - 140M| 2.62G| true| numpy .ply | https://github.com/QingyongHu/SensatUrban |


## mi3dmap

```bibtex
@article{mi3dmap,
  title={Semantic line framework-based indoor building modeling using backpacked laser scanning point cloud},
  author={Wang, Cheng and Hou, Shiwei and Wen, Chenglu and Gong, Zheng and Li, Qing and Sun, Xiaotian and Li, Jonathan},
  journal={ISPRS journal of photogrammetry and remote sensing},
  volume={143},
  pages={150--166},
  year={2018},
  publisher={Elsevier}
}

```
![](http://mi3dmap.net/assets/img/big/line1.png)

## ModelNet10 & ModelNet40 

```bibtex
@inproceedings{modelnet,
  title={3d shapenets: A deep representation for volumetric shapes},
  author={Wu, Zhirong and Song, Shuran and Khosla, Aditya and Yu, Fisher and Zhang, Linguang and Tang, Xiaoou and Xiao, Jianxiong},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={1912--1920},
  year={2015}
}

```


## scanobjectnn

Abstract
Deep learning techniques for point cloud data have demonstrated great potentials in solving classical problems in 3D computer vision such as 3D object classification and segmentation. Several recent 3D object classification methods have reported state-of-the-art performance on CAD model datasets such as ModelNet40 with high accuracy ~92%. Despite such impressive results, in this paper, we argue that object classification is still a challenging task when objects are framed with real-world settings. To prove this, we introduce ScanObjectNN, a new real-world point cloud object dataset based on scanned indoor scene data. From our comprehensive benchmark, we show that our dataset poses great challenges to existing point cloud classification techniques as objects from real-world scans are often cluttered with background and/or are partial due to occlusions. We identify three key open problems for point cloud object classification, and propose new point cloud classification neural networks that achieve state-of-the-art performance on classifying objects with cluttered background.

![](https://hkust-vgd.github.io/scanobjectnn/images/objects_teaser.png)

```bibtex
@inproceedings{scanobjectnn,
      title = {Revisiting Point Cloud Classification: A New Benchmark Dataset and Classification Model on Real-World Data},
      author = {Mikaela Angelina Uy and Quang-Hieu Pham and Binh-Son Hua and Duc Thanh Nguyen and Sai-Kit Yeung},
      booktitle = {International Conference on Computer Vision (ICCV)},
      year = {2019}
  }
```

## SenSat Urban
SensatUrban is an urban-scale photogrammetric point cloud dataset with nearly three billion richly annotated points. This dataset consists of large areas from two UK cities, covering about 6 km2 of the city landscape. In the dataset, each 3D point is labeled as one of 13 semantic classes such as ground, vegetation, car, etc..

```bibtex
@inproceedings{sensat_urban,
  title={Towards semantic segmentation of urban-scale 3D point clouds: A dataset, benchmarks and challenges},
  author={Hu, Qingyong and Yang, Bo and Khalid, Sheikh and Xiao, Wen and Trigoni, Niki and Markham, Andrew},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={4977--4987},
  year={2021}
}
```
![](https://github.com/QingyongHu/SensatUrban/raw/master/imgs/Fig1.png)

### processing

The data was downloaded in the provided format and preprocessed in the following way:

In addition to extracting the data from the provided `.ply` format using the code from the original git repository, uniform scaling and translation was applied in order to center the points around the origin with a maximum spanning size of 100 units. Coordinates where saved as 32 bit float triplets, colors as uint8 rtriplets and class labels where available as uint8 values.

### remarks

```
https://github.com/QingyongHu/SensatUrban

>Evaluation server: https://competitions.codalab.org/competitions/31519

>Urban3D Challenge@ICCV'21: https://urban3dchallenge.github.io/

For any questions or problems contact us at: qingyong.hu@cs.ox.ac.uk
```



# Links
download and processing scripts:

https://github.com/mlaass/datasets_pointclouds_3d

bgd nas:

"TULR/bgd/datasets/pointclouds_3d":

https://webdisk.ads.mwn.de/Handlers/AnonymousDownload.ashx?folder=409a697c