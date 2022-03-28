DIR="$( cd "$( dirname "$0" )" && pwd )"
docker rm mesh_sampling
echo "########## run in DIR: ${DIR}"
docker run -it --name mesh_sampling -v ${DIR}:/pc mwernerds/mesh_sampling /pc/mesh_sampling_off.sh 
echo "########## CONVERT 2 ATLAS ##########"
ply2atlas.py ModelNet10/ data/modelnet10_10k.h5 .off.ply
ply2atlas.py ModelNet40/ data/modelnet40_10k.h5 .off.ply