#!/bin/python3
import glob
import sys
import os
import numpy as np
import h5py
from tqdm import tqdm


def load_pc_file(filename, suncg=False, with_bg=False):
    # load bin file
    # pc=np.fromfile(filename, dtype=np.float32)
    pc = np.fromfile(os.path.join(filename), dtype=np.float32)

    # first entry is the number of points
    # then x, y, z, nx, ny, nz, r, g, b, label, nyu_label

    if(suncg):
        pc = pc[1:].reshape((-1, 3))
    else:
        pc = pc[1:].reshape((-1, 11))

    # only use x, y, z for now
    if with_bg:
        return np.array(pc[:, 0:3]),  np.array(pc[:, 6:9]).astype(np.uint8)

    else:
        # To remove backgorund points
        # filter unwanted class
        filtered_idx = np.intersect1d(np.intersect1d(np.where(
            pc[:, -1] != 0)[0], np.where(pc[:, -1] != 1)[0]), np.where(pc[:, -1] != 2)[0])
        (values, counts) = np.unique(pc[filtered_idx, -1], return_counts=True)
        max_ind = np.argmax(counts)
        idx = np.where(pc[:, -1] == values[max_ind])[0]
        xyz = np.array(pc[idx, 0:3])
        rgb = np.array(pc[idx, 6:9]).astype(np.uint8)
        return xyz, rgb


if __name__ == "__main__":
    with_bg = sys.argv[2].endswith("with_bg.h5")
    ext = ".bin"
    files = glob.glob(f'{sys.argv[1]}**/*{ext}', recursive=True)
    files = [x for x in files if not(x.endswith(
        '_part.bin') or x.endswith('_indices.bin'))]
    print(with_bg, files)
    print("with_bg=", with_bg)

    def process(f, with_bg):
        xyz, rgb = load_pc_file(f, with_bg=with_bg)

        groupname = f.replace("/", "_").replace(ext,
                                                "").replace("object_dataset_", "")
        # print(f"Loaded a dataset of {str(xyz.shape)}, {groupname}", rgb[0])
        cl =

        with h5py.File(sys.argv[2], "a") as f:
            grp = f.require_group(groupname)
            grp.create_dataset("coords", data=xyz)
            grp.create_dataset("rgb", data=rgb)
    for f in tqdm(files):
        try:
            process(f, with_bg)
        except Exception as e:
            print(e)
