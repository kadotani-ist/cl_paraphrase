import argparse
import utils
import difficulty_metrics
from operator import itemgetter
import numpy as np


def cal_difficulty(sorted_dataset):
    sorted_metric_score = np.array([s[2] for s in sorted_dataset])
    difficulty = 1. * np.arange(len(sorted_metric_score)) / (len(sorted_metric_score) - 1)
    return difficulty.tolist()


def generate_dataset(src_path, trg_path):
    src = utils.readlines(src_path)
    trg = utils.readlines(trg_path)
    word_freq_dict, total_count = utils.generate_word_freq_dict("data/sample/src_trg_vocab.txt")
    metric_score = [difficulty_metrics.edit_dist(s, t) for s, t in zip(src, trg)]
    dataset = [[s, t, m] for s, t, m in zip(src, trg, metric_score)]
    dataset.sort(key=itemgetter(2))
    difficulty = cal_difficulty(dataset)
    for i, d in enumerate(difficulty):
        dataset[i][2] = d
    return dataset


def output_files(out_path, dataset_output):
    src_output = list()
    trg_output = list()
    difficulty_output = list()
    for d in dataset_output:
        src_output.append(d[0])
        trg_output.append(d[1])
        difficulty_output.append(str(d[2]))
    utils.writelines(out_path + "_sorted.bpe.src", src_output)
    utils.writelines(out_path + "_sorted.bpe.trg", trg_output)
    utils.writelines(out_path + ".difficulty", difficulty_output)


if __name__ == "__main__":

    ap = argparse.ArgumentParser()

    ap.add_argument("--src_path", type=str)
    ap.add_argument("--trg_path", type=str)
    ap.add_argument("--out_path", type=str)
    args = ap.parse_args()

    dataset = generate_dataset(args.src_path, args.trg_path)
    output_files(args.out_path, dataset)
