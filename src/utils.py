import codecs
import math


def readlines(path):
    lines = list()
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    return lines


def writelines(path, lines):
    with codecs.open(path, 'w', 'utf-8') as f:
        for line in lines:
            f.writelines(line + "\n")


def generate_word_freq_dict(path):
    words = list()
    counts = list()
    total_count = 0
    word_freq_dict = dict()
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            word_count = line.split()
            words.append(word_count[0])
            counts.append(int(word_count[1]))
            total_count += int(word_count[1])
    for w, c in zip(words, counts):
        word_freq_dict[w] = c / total_count
    return word_freq_dict, total_count
