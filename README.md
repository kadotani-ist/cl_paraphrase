# Edit Distance Based Curriculum Learning for Paraphrase Generation

This repository provides an implementation of the edit distance based curriculum learning method.
This method is based on [competence-based curriculum learning](https://aclanthology.org/N19-1119).

## Prerequisites
Please make sure to install all the dependent libraries in ``requirements.txt``

## Usage
### Generate files required for curriculum learning.
```
python3 src/sort_by_difficulty.py --src_path data/sample/train.bpe.src --trg_path data/sample/train.bpe.trg --out_path data/sample/train
```
The following files will be generated.

* ```train_sorted.bpe.src```: Input sentences of training data sorted by difficulty
* ```train_sorted.bpe.trg```: Reference sentences of training data sorted by difficulty
* ```train.difficulty```: Difficulty of each training sample

For selecting the difficulty metric (sentence length, word rarity, edit distance), change the function in ```generate_dataset(src_path, trg_path)``` function.

### Training
```
python3 -m joeynmt train configs/transformer_sample.yaml
```
I implemented using [Joey NMT framework](https://github.com/joeynmt/joeynmt).

If you want to change the number of training steps which the model fully competent, please change ```total_steps```   in ```steps_based(steps)``` function in ```competence_metrics.py```

## Dataset
I applied the edit distance based curriculum learning for formality transformation.
I used [Grammarly's Yahoo Answers Formality Corpus (GYAFC)](https://github.com/raosudha89/GYAFC-corpus) as the dataset.

## Citation
When you use our codes in your projects, please cite the following paper.

Sora Kadotani, Tomoyuki Kajiwara, Yuki Arase, Makoto Onizuka. 2021. Edit Distance Based Curriculum Learning for Paraphrase Generation. In Proceedings of the Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing Student Research Workshop (ACL-IJCNLP 2021 SRW)", pp. ?-?.
```
@inproceedings{kadotani-etal-2021-edit,
    title = "Edit Distance Based Curriculum Learning for Paraphrase Generation",
    author = "Kadotani, Sora  and
      Kajiwara, Tomoyuki and
      Arase, Yuki and
      Makoto, Onizuka",
    booktitle = "The Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing Student Research Workshop (ACL-IJCNLP 2021 SRW)",
    month = aug,
    year = "2021",
    address = "Bangkok, Thailand (Online)",
    publisher = "?",
    url = "?",
    doi = "?",
    pages = "?--?"
}
