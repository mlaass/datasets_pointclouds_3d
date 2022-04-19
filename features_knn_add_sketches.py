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
from pathlib import Path

import globimap as gm


def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom == 0] = 1
    return x_min + nom/denom


class cfg:
    k = 6
    logm = [7, 8, 9]


faulthandler.enable()


config = {
    "datapath": "/data/ssd/moritz/tf/pointclouds/data/"
}


files = glob.glob(f'{config["datapath"]}**_features.h5', recursive=False)
files = [f for f in files if not (
    f == f'{config["datapath"]}sensat_urban_features.h5')]
print(files)
#files = ["modelnet10_sample_features.h5"]

for file in files[:]:
    print("******* extend: ", file)

    with h5py.File(file, "r+") as f:
        Q = tqdm(list(f.keys())[:100], ncols=80)
        for grp in Q:
            g = f.require_group(grp)
            Q.set_description(f'{grp}')
            # print(grp, list(g.keys()))
            # k = 6
            for k in (range(6, 11, 2)):
                Q.set_description(f'{grp}.k{k}')
                nfeat = f"features_k{k}"
                nneigh = f"neighbors_k{k}"
                n = g[nneigh][:]

                for logm in cfg.logm:
                    Q.set_description(f'{grp}.k{k}.logm{logm}')

                    nneigh_gm = f"neighbors_k{k}_gm_{pow(2,logm)}"
                    if not nneigh_gm in g:
                        gmf = []
                        foz = []
                        for p in n:
                            m = gm.globimap()
                            m.configure(cfg.k, logm)
                            p = p.reshape(k+1, 3)
                            p = scale(p, 0, 1)
                            p = (p*1024).astype(np.uint32)
                            for x in p:
                                m.put(x[0], x[1], x[2])
                            gmf.append(np.array(m.get_filter(), dtype=bool))
                            #foz.append(np.array(m.stats(), dtype=np.float32))
                        # print(gmf)
                        g.create_dataset(nneigh_gm, data=np.array(gmf))
                        # g.create_dataset(f"{nneigh_gm}_stats",
                        #                  data=np.array(foz))
        print("==>", Path(file).stem, "done...\n")
