#!/bin/bash
#
# @Author: yangxiaohan
# @Date: 2018-09-21
#

function run()
{
    name=$1
    python -u ./src/${name} $2 > ./log/${name} 2>&1 &
}

source activate python35
python --version

run 0_data_preprocess.py
wait
run 1_basic_feature.py
run 2_pair_feature.py
run 3_statistics_feature.py
wait

run concat_feature.py
wait

run predict.py 1