#!/usr/bin/env sh

set -e

TOOLS=./build/tools

$TOOLS/caffe test -model=./DeepID2_train_test.prototxt -weights=./examples/deepid2/deepid2_iter_600000.caffemodel -gpu=0 $@

#cp ./daLFW.out ../JB/JB-python_DeepID2/data/
#cp ./idLFW.out ../JB/JB-python_DeepID2/data/
#cp ./data/deepid2/intra.out ../JB/JB-python_DeepID2/data/
#cp ./data/deepid2/extra.out ../JB/JB-python_DeepID2/data/
#cd ../JB/JB-python_DeepID2/src/
#python test_lfw.py
