#!/bin/bash
echo "######## SAMPLE MESHES ##########"
function process()
{
    echo "Processing $1"
    mesh_sampling --in "$1" --out "$1".ply --samples 10000 --type xyz
}
export -f process
find /pc/ModelNet10 -name *.off   | parallel process {}
find /pc/ModelNet40 -name *.off   | parallel process {}
