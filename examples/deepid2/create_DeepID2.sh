#!/usr/bin/env sh
# This script converts the CASIA-maxpy-clean into lmdb format.
set -e

EXAMPLE=examples/deepid2
DATA=./data/deepid2/
TOOLS=./build/tools

RESIZE_HEIGHT=55
RESIZE_WIDTH=47

#pre-run python script in order to generate train.out and val.out
#You have to specify the dataset location first
python ./data/deepid2/get_data.py $1 $2

echo "creating lmdb..."

rm -rf $EXAMPLE/DeepID2_train_lmdb

rm -rf $EXAMPLE/DeepID2_test_lmdb


$TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    $DATA \
    $DATA/train.out \
    $EXAMPLE/DeepID2_train_lmdb

$TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    $DATA \
    $DATA/val.out \
    $EXAMPLE/DeepID2_test_lmdb

echo "compute image mean..."

$TOOLS/compute_image_mean $EXAMPLE/DeepID2_train_lmdb \
  $EXAMPLE/DeepID2_mean.proto

echo "done..."

