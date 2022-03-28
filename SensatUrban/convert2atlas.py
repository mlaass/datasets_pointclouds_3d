#!/bin/python3
import glob
import sys
import numpy as np
import h5py
from tqdm import tqdm

from SensatUrban.helper_ply import read_ply


def read_ply_data(path, with_rgb=True, with_label=True):
    data = read_ply(path)
    fields = len(data.dtype.names)
    print(data.dtype.names)
    xyz = np.vstack((data['x'], data['y'], data['z'])).T
    if with_rgb and with_label and fields == 7:
        rgb = np.vstack((data['red'], data['green'], data['blue'])).T
        labels = data['class']
        return xyz.astype(np.float32), rgb.astype(np.uint8), labels.astype(np.uint8)
    elif with_rgb and not with_label:
        rgb = np.vstack((data['red'], data['green'], data['blue'])).T
        return xyz.astype(np.float32), rgb.astype(np.uint8)
    elif not with_rgb and with_label:
        labels = data['class']
        return xyz.astype(np.float32), labels.astype(np.uint8)
    elif not with_rgb and not with_label:
        return xyz.astype(np.float32)


if __name__ == "__main__":
    ext = ".ply"
    ply_files = glob.glob(f'{sys.argv[1]}**/*{ext}', recursive=True)
    print(ply_files)

    def process(f):
        # xyz, rgb = read_ply_data(f, with_rgb=True, with_label=False)
        data = read_ply(f)
        fields = len(data.dtype.names)
        print(data.dtype.names)
        xyz = (np.vstack((data['x'], data['y'], data['z'])).T).astype(
            np.float32)
        xyz -= np.min(xyz, axis=0)
        xyz /= np.max(xyz)
        xyz -= 0.5
        xyz *= 50
        rgb = (np.vstack((data['red'], data['green'], data['blue'])).T).astype(
            np.uint8)
        rgb = rgb
        has_labels = False
        labels = None
        if 'class' in data.dtype.names:
            has_labels = True
            labels = data['class'].astype(np.uint8)

        groupname = f.replace(sys.argv[1], "").replace(
            "/", "_").replace(ext, "")
        print(f"Loaded a dataset of {str(xyz.shape)}, {groupname}")

        with h5py.File(sys.argv[2], "a") as f:
            grp = f.require_group(groupname)
            grp.create_dataset("coords", data=xyz)
            grp.create_dataset("rgb", data=rgb)
            if has_labels:
                grp.create_dataset("class", data=labels)
    for f in tqdm(ply_files):
        process(f)
