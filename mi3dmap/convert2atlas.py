#!/bin/python3
import glob
import sys
import os
import numpy as np
import h5py
from tqdm import tqdm
import laspy


def load_las_file(filename):
    las = laspy.read(filename)
    coords = np.vstack((las.x, las.y, las.z)).transpose()
    print(coords.shape)
    return coords


if __name__ == "__main__":
    ext = ".las"
    files = glob.glob(f'**{ext}', recursive=True)
    print(files)

    def process(f):
        xyz = load_las_file(f)

        groupname = f.replace("/", "_").replace(ext, "")
        #print(f"Loaded a dataset of {str(xyz.shape)}, {groupname}")

        with h5py.File(sys.argv[2], "a") as f:
            grp = f.require_group(groupname)
            grp.create_dataset("coords", data=xyz)
    for f in tqdm(files):
        try:
            process(f)
        except Exception as e:
            print(e)
