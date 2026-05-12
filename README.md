## Papers

This repo implements two related papers:

**Bias Discovery in News Articles Using Word Vectors**
Patankar A., Bose J.
IEEE International Conference on Machine Learning and Applications
(ICMLA) 2017, pp. 785-788
[DOI: 10.1109/ICMLA.2017.00-62](https://ieeexplore.ieee.org/document/8260730)

**Bias Based Navigation for News Articles and Media**
Patankar A., Bose J.
NLDB 2016, pp. 465-470

---

## What this is about (plain English)

When you read news online, articles are often biased without
you realising it. Certain word choices subtly push you toward
a viewpoint.

This tool detects bias automatically using word vectors.
Instead of just counting biased words, it measures how
similar each word in an article is to a list of known biased
words, using Word2Vec trained on Wikipedia.

Key finding from the paper: Wikipedia articles score lower
bias than news articles, which score lower than opinion blogs.
Pro-Trump and anti-Trump articles both score higher bias than
the neutral Wikipedia article on Trump — the system detects
bias regardless of political direction.

The bias score is a number between 0 and 1. Higher means
more biased language.

---

## Citation

```bibtex
@inproceedings{patankar2017bias,
  title={Bias Discovery in News Articles Using Word Vectors},
  author={Patankar, Anish Anil and Bose, Joy},
  booktitle={IEEE International Conference on Machine Learning
  and Applications (ICMLA)},
  pages={785--788},
  year={2017}
}
```
