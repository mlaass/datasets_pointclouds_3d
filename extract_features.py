#!/bin/python3
import mpcl
import io
import sys
import os
import glob
import h5py
from tqdm import tqdm
import numpy as np
import faulthandler

faulthandler.enable()


config = {
    "datapath": "/data/ssd/moritz/tf/pointclouds/data/"
}


files = glob.glob(f'{config["datapath"]}**.h5', recursive=False)
files = [f for f in files if not (f.endswith(
    '_features.h5') or f == f'{config["datapath"]}sensat_urban.h5')]
print(files)

files = [f'{config["datapath"]}sensat_urban.h5']

for file in files[:]:
    outfile = f'{file[:-3]}_features.h5'
    print("******* extract: ", file, "->", outfile)

    with h5py.File(file, "r") as f:
        for grp in tqdm(list(f.keys())):
            pc = mpcl.pointcloud(f[grp]["coords"])
            g = f.require_group(grp)
            # print(grp, list(g.keys()))
            # k = 6
            for k in (range(6, 11, 2)):

                with h5py.File(outfile, "a") as fout:

                    gout = fout.require_group(grp)
                    nfeat = f"features_k{k}"
                    nneigh = f"neighbors_k{k}"
                    if not nfeat in gout or not nneigh in gout:
                        features, neighbors = pc.extractKnnTensorsAndNeighbors(
                            k)
                        # print(k, features.shape, features.dtype,
                        #       neighbors.shape, neighbors.dtype)
                        if not nfeat in gout:
                            gout.create_dataset(
                                nfeat, data=features.astype(np.float32))
                        if not nneigh in gout:
                            gout.create_dataset(
                                nneigh, data=neighbors.astype(np.float32))
