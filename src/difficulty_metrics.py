import math
import editdistance


def src_sentence_length(src):
    words = src.split()
    return len(words)


def src_word_rarity(src, word_freq_dict, total_count):
    words = src.split()
    difficulty_rarity = 0
    for w in words:
        if w in word_freq_dict:
            difficulty_rarity += - math.log(word_freq_dict[w])
        else:
            difficulty_rarity += - math.log(1 / total_count)
    return difficulty_rarity


def edit_dist(src, trg):
    src_words = src.split()
    trg_words = trg.split()
    return editdistance.eval(src_words, trg_words)
