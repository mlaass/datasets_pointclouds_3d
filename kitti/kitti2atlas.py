#!/bin/python3

import h5py
import math
import os
import numpy as np
import glob
import sys
from tqdm import tqdm
root_dir = 'dataset/sequences/'
out_file = 'kitti.h5'


if __name__ == "__main__":
    if len(sys.argv) > 2:
        root_dir = sys.argv[1]
        out_file = sys.argv[2]
    hf = h5py.File(out_file, "w")

    print(root_dir, "-->", out_file)
    unq_labels = []
    unq_objects = []
    for flab in tqdm(glob.glob(f'{root_dir}**/*.label', recursive=True)[:]):

        fpc = flab.replace('labels', 'velodyne').replace('.label', '.bin')
        groupname = fpc[len(root_dir):-4].replace("velodyne/",
                                                  "").replace("/", "_")
        # print(groupname, ": \n", flab, ", ", fpc,)

        grp = hf.require_group(groupname)
        lidar = np.fromfile(fpc, dtype=np.float32).reshape(-1, 4)
        lbl = np.fromfile(flab, dtype=np.uint32).reshape(-1)
        labels = ((lbl) & 0xffff).astype(np.uint16)
        objects = (lbl >> 16).astype(np.uint16)

        coords = lidar[:, 0:3]
        if coords.shape[0] != lbl.shape[0]:
            print("ERR", groupname)
            print(lidar.shape, lbl.shape)
        grp.create_dataset("coords", data=coords)
        grp.create_dataset("labels", data=labels)
        grp.create_dataset("objects", data=objects)
        unq_labels.extend(np.unique(labels))
        unq_objects.extend(np.unique(objects))
        unq_objects = list(set(unq_objects))
        unq_labels = list(set(unq_labels))
        #print(lbl[:3], labels[:3], objects[:3])
    print(len(unq_labels), len(unq_objects))
    print(sorted(unq_labels), sorted(unq_objects))
    hf.close()
