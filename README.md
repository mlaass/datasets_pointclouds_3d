# Pointclouds 3D
A curated list of 3d pointcloud datasets used in research.

## requirements

```
docker python3 curl wget unrar unzip
```

```sh
git submodule update --init --recursive
pip3 install tqdm numpy h5py plyfile laspy
```

# instructions

```sh
# 1. run and follow instructions
./download.sh

# sample modelnet meshes
./run_meshsampling.sh

# convert mi3dmap
cd mi3dmap
unzip ...
./convert2atlas.py mi3dmap.h5
mv mi3dmap ../data

# convert scanobjectnn
cd scanobjectnn
unzip ...
./convert2atlas.py object_dataset/ scanobjectnn.h5
./convert2atlas.py object_dataset/ scanobjectnn_with_bg.h5
mv scanobjectnn.h5 ../data
mv scanobjectnn_with_bg.h5 ../data

# convert SensatUrban
cd SensatUrban
./convert2atlas.py ply/ sensat_urban.h5
mv sensat_urban.h5 ../data
```