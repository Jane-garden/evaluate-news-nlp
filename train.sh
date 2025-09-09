date
source /root/autodl-tmp/bertm/torch26_env/bin/activate
# source ~/.bashrc
# export PATH="/yrfs1/rc/zpchen/tools/anaconda9/bin:$PATH"
# bert_dir='/root/autodl-tmp/bertm/预训练模型应用实例-更新版/chinese-roberta-wwm-ext'
bert_dir='/root/autodl-tmp/法律智能问答案例/baseline/lawformer'

python run_cail.py \
    --name train_v1 \
    --bert_model $bert_dir \
    --tokenizer_path $bert_dir \
    --data_dir processed \
    --batch_size 2 \
    --eval_batch_size 32 \
    --lr 1e-5 \
    --gradient_accumulation_steps 1 \
    --epochs 2

date
