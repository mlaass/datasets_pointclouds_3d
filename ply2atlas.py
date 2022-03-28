#!/bin/python3
import glob
import sys
from plyfile import (PlyData, PlyElement)
import numpy as np
import h5py
from joblib import Parallel, delayed


def load_ply_data(filename):

    plydata = PlyData.read(filename)
    pc = plydata['vertex'].data
    pc_array = np.array([[x, y, z] for x, y, z in pc]).astype(np.float32)
    return pc_array


if __name__ == "__main__":
    print(sys.argv)
    ext = ".off.ply"
    if len(sys.argv) == 4:
        ext = sys.argv[3]
    print("all files in ", sys.argv[1],
          " with ext:'", ext, "' => ", sys.argv[2])
    ply_files = glob.glob(f'{sys.argv[1]}**/*{ext}', recursive=True)
    # # print(ply_files)

    def process(f):
        m = load_ply_data(f)
        groupname = f.replace("/", "_").replace(ext,
                                                "").replace('ModelNet10_', '')
        print(f"Loaded a dataset of {str(m.shape)}, {groupname}")

        with h5py.File(sys.argv[2], "a") as f:
            grp = f.require_group(groupname)
            grp.create_dataset("coords", data=m)
    for f in ply_files[:]:
        process(f)
