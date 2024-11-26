#!/bin/bash

# 设置环境变量
export PRE_SEQ_LEN=128
export LR=2e-2

# 运行训练脚本
CUDA_VISIBLE_DEVICES=0 python3 main_train.py \
    --do_train \
    --train_file ../data/formatted_data.json \
    --validation_file ../data/formatted_data.json \
    --prompt_column content \
    --response_column summary \
    --overwrite_cache \
    --model_name_or_path ./base_model \
    --output_dir output/ \
    --overwrite_output_dir \
    --max_source_length 64 \
    --quantization_bit 4 \
    --pre_seq_len ${PRE_SEQ_LEN} \
    --learning_rate ${LR}
