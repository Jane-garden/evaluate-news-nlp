# source ~/.bashrc
source /root/autodl-tmp/bertm/torch26_env/bin/activate
# export PATH="/yrfs1/rc/zpchen/tools/anaconda9/bin:$PATH"
INPUT_TRAIN_FILE=../data/train.json
INPUT_DEV_FILE=../data/dev.json

# OUTPUT_DIR=./data/processed #this dir must the same as the data_dir in train.sh
OUTPUT_DIR=./processed
mkdir ${OUTPUT_DIR}
#新模型：
tokenizer_path='/root/autodl-tmp/法律智能问答案例/baseline/lawformer'

# tokenizer_path='autodl-tmp/bertm/预训练模型应用实例-更新版/chinese-roberta-wwm-ext'

python data_process.py \
    --tokenizer_path=$tokenizer_path \
    --full_data=${INPUT_TRAIN_FILE} \
    --example_output=${OUTPUT_DIR}/train_example.pkl.gz \
    --feature_output=${OUTPUT_DIR}/train_feature.pkl.gz \

python data_process.py \
    --tokenizer_path=$tokenizer_path \
    --full_data=${INPUT_DEV_FILE} \
    --example_output=${OUTPUT_DIR}/dev_example.pkl.gz \
    --feature_output=${OUTPUT_DIR}/dev_feature.pkl.gz \


