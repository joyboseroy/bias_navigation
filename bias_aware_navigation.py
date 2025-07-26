# Bias Aware Navigation
# A simple tool to crawl trending news articles, extract content, detect bias using a lexicon-based score, and surface results through a Chrome UI.

# Requirements:
# pip install requests beautifulsoup4 newspaper3k rake-nltk readability-lxml

import requests
from bs4 import BeautifulSoup
from newspaper import Article
from rake_nltk import Rake
import string

# Sample bias lexicon (positive or negative sentiment toward political topics)
bias_lexicon = {
    "allegedly": 1,
    "apparently": 1,
    "claims": 1,
    "supposedly": 1,
    "reportedly": 1,
    "so-called": 1,
    "admittedly": 1,
    "arguably": 1,
    "undeniable": 1,
    "clearly": 1,
    "just": 1,
    "only": 1,
    "even": 1,
    "naturally": 1,
    "of course": 1,
    "fortunately": 1,
    "unfortunately": 1,
    "notably": 1,
    "remarkably": 1,
    "significantly": 1,
    "shocking": 1,
    "important": 1,
    "controversial": 1,
    "disputed": 1,
    "debated": 1,
    "biased": 1,
    "unbiased": -1,
    "neutral": -1,
    "terrorist": 2,
    "freedom": -1,
    "regime": 2,
    "heroic": -1,
    "tyrant": 2,
    "corrupt": 2,
    "elite": 1,
    "grassroots": -1,
    "authoritarian": 2,
    "patriot": -1,
    "enemy": 1,
    "scandal": 2,
    "agenda": 1,
    "radical": 2,
    "extremist": 2,
    "fascist": 2,
    "communist": 2,
    "capitalist": 2,
    "manipulate": 2,
    "mislead": 2,
    "spin": 1,
    "objective": -1,
    "fair": -1,
    "balanced": -1,
    "fact": -1,
    "truth": -1,
    "admits": 1,
    "refuses to comment": 1,
    "shocking revelation": 2,
    "critics say": 1,
    "supporters claim": 1,
    "according to unnamed sources": 2,
    "is widely regarded as": 1,
    "has been accused of": 2,
    "is known for": 1,
    "self-described": 1,
    "repeatedly stated": 1,
    "makes the case that": 1,
    "alleged": 1,
    "purported": 1,
    "reputed": 1,
    "presumably": 1,
    "some believe": 1,
    "others argue": 1,
    "acknowledged": 1
}

# Step 1: Get Trending Topics (Placeholder via Google News)
def get_trending_topics():
    res = requests.get("https://news.google.com")
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.find_all("a")
    trending = list(set([t.get_text() for t in titles if t.get_text().strip()]))[:10]
    return trending

# Step 2: Get URLs for each trending topic (using Bing Search API or Google Search)
def get_urls_for_topic(topic):
    # Updated URLs to more reliably parsable news sources
    return [
        "https://www.hindustantimes.com/india-news/maldives-and-india-reaffirm-relations-during-pm-modis-visit-101690348761123.html",
        "https://indianexpress.com/article/india/pm-modi-visit-maldives-diplomatic-ties-8865512/"
    ]

# Step 3: Extract clean text from URLs using newspaper3k
from readability import Document

def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Newspaper3k failed for {url}: {e}")
        # Try fallback with requests + readability-lxml and HTML cleanup
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            doc = Document(response.text)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # Remove non-content tags
            for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
                tag.decompose()

            # Filter meaningful paragraphs
            article_tag = soup.find("article")
            if article_tag:
                paragraphs = article_tag.find_all("p")
            else:
                paragraphs = soup.find_all("p")

            cleaned_text = "\n".join(
                p.get_text(strip=True) for p in paragraphs
                if len(p.get_text(strip=True).split()) > 5
            ) 

            print(f"Extracted {len(cleaned_text.split())} words from {url}\nPreview: {cleaned_text[:300]}...\n")
            return cleaned_text.strip()
        except Exception as e2:
            print(f"Fallback readability failed for {url}: {e2}")
            return ""


# Step 4: Keyword extraction using RAKE
def extract_keywords_rake(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    ranked_phrases = r.get_ranked_phrases_with_scores()
    top_keywords = [(score, phrase) for score, phrase in ranked_phrases if len(phrase.split()) > 1][:3]
    return top_keywords

# Step 5: Calculate Bias Score
def calculate_bias_score(text):
    import re
    score = 0
    matches = []
    normalized_text = text.lower().translate(str.maketrans('', '', string.punctuation))

    for phrase, weight in bias_lexicon.items():
        pattern = re.compile(re.escape(phrase))
        found = pattern.findall(normalized_text)
        if found:
            count = len(found)
            score += count * weight
            matches.append((phrase, count, weight))

    total_words = len(normalized_text.split())
    bias_density = score / total_words * 100 if total_words > 0 else 0

    print("Matched bias phrases:", matches)
    print("Total bias score:", score)
    print("Bias density (per 100 words):", round(bias_density, 2))
    return round(bias_density, 2)

# Main flow
if __name__ == "__main__":
    print("Getting trending topics...")
    topics = get_trending_topics()

    for topic in topics:
        print(f"\nTopic: {topic}")
        urls = get_urls_for_topic(topic)

        for url in urls:
            print(f"\nURL: {url}")
            text = extract_text_from_url(url)
            if len(text.split()) < 100:
                print("Not enough content extracted. Skipping bias analysis.")
                continue
            keywords = extract_keywords_rake(text)
            bias_score = calculate_bias_score(text)

            print("Top Keywords:", keywords)
            print("Bias Score:", bias_score)

            print("Summary:", topic, url, bias_score, ", ".join([kw[1] for kw in keywords]))

    print("\nBias analysis completed.")
