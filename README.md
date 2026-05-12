# Bias Aware Navigation

Code related to the paper:

**A Bias Aware News Recommendation System**
Patankar A., Bose J.
IEEE International Conference on Semantic Computing (ICSC) 2019
[arXiv:1803.03428](https://arxiv.org/abs/1803.03428)

---

## What this is about (plain English)

When you read news online, the articles you see are often biased without
you realising it. Words are chosen, facts are selected, and framings are
used that subtly push you toward a particular viewpoint.

This tool automatically detects bias in news articles as you browse.

It works by:
1. Fetching trending news articles from Google News
2. Extracting the full article text
3. Scoring each article for bias using a handcrafted lexicon based on
   Wikipedia's Neutral Point of View (NPOV) guidelines
4. Showing you a bias density score so you can judge the article yourself

The goal is not to tell you what to think. It is to make the bias
visible so you can make a more informed decision.

---

## Features

- Crawls trending topics from Google News
- Extracts full article text using Newspaper3k or Readability
- Calculates bias score based on biased words and phrases
- Computes both absolute score and normalised bias density per 100 words
- Matches single words and multi-word biased phrases
- Lexicon derived from Wikipedia NPOV guidelines

---

## Files

| File | What it does |
|---|---|
| `bias_aware_navigation.py` | Main bias detection script |
| `requirements.txt` | Dependencies |

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/joyboseroy/bias_navigation.git
cd bias_navigation

# Install dependencies
pip install -r requirements.txt

# Run
python bias_aware_navigation.py
```

---

## Citation

```bibtex
@inproceedings{patankar2019bias,
  title={A Bias Aware News Recommendation System},
  author={Patankar, Anish Anil and Bose, Joy},
  booktitle={IEEE International Conference on Semantic Computing (ICSC)},
  year={2019}
}
```

---

## Related Work

- **Bias Based Navigation for News Articles and Media**
  Patankar A., Bose J. NLDB 2016.
- **A web browser responsive to the user interest level**
  Bose J. et al. IEEE INDICON 2015. (Best Paper Award)
- **A Hands Free Browser Using EEG and Voice Inputs**
  Bose J. et al. IJCNN 2015.

---

## Author

**Dr. Joy Bose** — Senior Data Scientist and AI Architect, Ericsson Global

[LinkedIn](https://linkedin.com/in/joyboseroy) ·
[Google Scholar](https://scholar.google.com/citations?user=1E0YgA4AAAAJ) ·
[Personal site](https://joyboseroy.github.io)
