echo "Go to the following websites and fill the forms and donwload scanobjectsnn and SensatUrban datasets to their respective folders"
cat ./scanobjectnn/link.txt
cat ./SensatUrban/link.txt
echo "download mi3dmap scene 1"
#curl http://mi3dmap.net/download.jsp?fileNo=AT1glyuSrFX8QNCm --output mi3dmap/scene1.rar
unrar e mi3dmap/scene1.rar mi3dmap/
echo "download mi3dmap scene 2"
curl http://mi3dmap.net/download.jsp?fileNo=hOYXEhoiEgWgaWg --output mi3dmap/scene2.rar
unrar e mi3dmap/scene2.rar mi3dmap/
echo "download mi3dmap scene 3"
curl http://mi3dmap.net/download.jsp?fileNo=8kPMCQDFTHbYPcMk --output mi3dmap/scene3.rar
unrar e mi3dmap/scene3.rar mi3dmap/
echo "download mi3dmap scene 4"
curl http://mi3dmap.net/download.jsp?fileNo=DUHH6YdWkyDJTl04 --output mi3dmap/scene4.rar
unrar e mi3dmap/scene4.rar mi3dmap/
echo "download ModelNet10"
wget http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip
unzip ModelNet10.zip
echo "download ModelNet40"
wget http://modelnet.cs.princeton.edu/ModelNet40.zip
unzip ModelNet40.zip
