#!/bin/bash

source /root/autodl-tmp/bertm/torch26_env/bin/activate

# PRED_FILE="output/submissions/train_v1/pred_seed_13_epoch_10_99999.json"
#新模型  
# PRED_FILE="output/submissions/train_v1/pred_seed_51_epoch_5_99999.json"
PRED_FILE="output/submissions/train_v1/pred_seed_26_epoch_4_99999.json"

GOLD_FILE="../data/dev.json"

echo "Evaluating prediction file: $PRED_FILE"
echo "Using gold file: $GOLD_FILE"

python evaluate.py --pred_file "$PRED_FILE" --gold_file "$GOLD_FILE"