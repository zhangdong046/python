#!/bin/bash 
source /home/map/.bash_profile
if [ $# -lt 2 ]
then
    exit
fi 

mif_dir=$1
db_name=$2

if [ ! -d $mif_dir ]
then
    echo 'Dir not exist!'
    exit
fi

bak=_back
bak2=_d
mif_file=`ls -al $mif_dir|grep TAB|awk '{print $NF}'`
for f in $mif_file 
do
   #/home/map/qa/tools/bin/ogr2ogr -append -f "PostgreSQL" "PG:dbname=$db_name host=127.0.0.1 port=5432" "gbk:$mif_dir/$f" -lco GEOMETRY_NAME=shape -lco GEOM_TYPE=geometry -a_srs wgs84 --config PG_USE_COPY YES
   /home/map/qa/yirenwei/tools/bin/ogr2ogr  -append -f "PostgreSQL" "PG:dbname=$db_name host=127.0.0.1 port=9123" "gbk:$mif_dir/$f" -lco GEOMETRY_NAME=shape -lco GEOM_TYPE=geometry -a_srs wgs84 --config PG_USE_COPY YES -nln ${f%%.*}$bak
   #/home/map/qa/tools/bin/ogr2ogr -append -f "PostgreSQL" "PG:dbname=$db_name host=127.0.0.1 port=5432" "gbk:$mif_dir/$f" -lco GEOMETRY_NAME=shape -lco GEOM_TYPE=geometry -a_srs wgs84 --config PG_USE_COPY YES -nln ${f%%.*}$bak$bak2
done
