import json
import re
import string
import argparse
from collections import Counter

def normalize_answer(s):
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)
    def white_space_fix(text):
        return ' '.join(text.split())
    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)
    def lower(text):
        return text.lower()
    return white_space_fix(remove_articles(remove_punc(lower(s))))

def f1_score(prediction, ground_truth):
    normalized_prediction = normalize_answer(prediction)
    normalized_ground_truth = normalize_answer(ground_truth)
    ZERO_METRIC = (0, 0, 0)
    if normalized_prediction in ['yes', 'no', 'unknown'] and normalized_prediction != normalized_ground_truth:
        return ZERO_METRIC
    if normalized_ground_truth in ['yes', 'no', 'unknown'] and normalized_prediction != normalized_ground_truth:
        return ZERO_METRIC
    prediction_tokens = list(normalized_prediction)
    ground_truth_tokens = list(normalized_ground_truth)
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return ZERO_METRIC
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1, precision, recall

def exact_match_score(prediction, ground_truth):
    return normalize_answer(prediction) == normalize_answer(ground_truth)

def update_answer(metrics, prediction, gold):
    em = exact_match_score(prediction, gold)
    f1, prec, recall = f1_score(prediction, gold)
    metrics['em'] += float(em)
    metrics['f1'] += f1
    metrics['prec'] += prec
    metrics['recall'] += recall
    return em, prec, recall

def update_sp(metrics, prediction, gold):
    cur_sp_pred = set(map(tuple, prediction))
    gold_sp_pred = set(map(tuple, gold))
    tp = len(cur_sp_pred & gold_sp_pred)
    fp = len(cur_sp_pred - gold_sp_pred)
    fn = len(gold_sp_pred - cur_sp_pred)
    prec = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0
    f1 = 2 * prec * recall / (prec + recall) if prec + recall > 0 else 0.0
    em = 1.0 if fp + fn == 0 else 0.0
    metrics['sp_em'] += em
    metrics['sp_f1'] += f1
    metrics['sp_prec'] += prec
    metrics['sp_recall'] += recall
    return em, prec, recall

def evaluate(gold_file, pred_file):
    with open(pred_file, 'r', encoding='utf-8') as f:
        prediction = json.load(f)
    with open(gold_file, 'r', encoding='utf-8') as f:
        gold = json.load(f)

    metrics = {
        'em': 0, 'f1': 0, 'prec': 0, 'recall': 0,
        'sp_em': 0, 'sp_f1': 0, 'sp_prec': 0, 'sp_recall': 0,
        'joint_em': 0, 'joint_f1': 0, 'joint_prec': 0, 'joint_recall': 0
    }

    for dp in gold:
        cur_id = str(dp['_id'])
        can_eval_joint = True

        if cur_id not in prediction.get('answer', {}):
            print(f'missing answer: {cur_id}')
            can_eval_joint = False
        else:
            em, prec, recall = update_answer(metrics, prediction['answer'][cur_id], dp['answer'])

        if cur_id not in prediction.get('sp', {}):
            print(f'missing sp: {cur_id}')
            can_eval_joint = False
        else:
            sp_em, sp_prec, sp_recall = update_sp(metrics, prediction['sp'][cur_id], dp['supporting_facts'])

        if can_eval_joint:
            joint_prec = prec * sp_prec
            joint_recall = recall * sp_recall
            joint_f1 = 2 * joint_prec * joint_recall / (joint_prec + joint_recall) if joint_prec + joint_recall > 0 else 0.0
            joint_em = em * sp_em
            metrics['joint_em'] += joint_em
            metrics['joint_f1'] += joint_f1
            metrics['joint_prec'] += joint_prec
            metrics['joint_recall'] += joint_recall

    N = len(gold)
    for k in metrics:
        metrics[k] /= N

    print(json.dumps(metrics, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gold_file', type=str, required=True)
    parser.add_argument('--pred_file', type=str, required=True)
    args = parser.parse_args()

    evaluate(args.gold_file, args.pred_file)