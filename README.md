# Bias Aware Navigation

A Python tool to detect bias in trending news articles using a lexicon-based scoring system.

## Features

- Crawls trending topics from Google News
- Searches for related articles (hardcoded for now)
- Extracts full article text using Newspaper3k or Readability
- Calculates a bias score based on presence of biased words and phrases
- Prints keywords and a bias density score (per 100 words)

## Bias Detection Method

- Uses a handcrafted lexicon derived from Wikipedia's NPOV guidelines and common biased terms
- Computes both absolute score and normalized bias density
- Matches single words and multi-word biased phrases

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/joyboseroy/bias-aware-navigation.git
cd bias-aware-navigation
