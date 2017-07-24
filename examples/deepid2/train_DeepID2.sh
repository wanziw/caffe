#!/usr/bin/env sh
set -e

TOOLS=./build/tools

$TOOLS/caffe train --solver=./DeepID2_solver.prototxt $@
