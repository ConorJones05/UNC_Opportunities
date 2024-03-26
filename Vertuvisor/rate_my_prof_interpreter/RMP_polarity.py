from textblob import TextBlob


# Define categories
categories = {
    "Movie Reviews": ["movie", "film"],
    "Technology Concerns": ["technology", "AI", "artificial intelligence"],
    "Blob": ['blob'],
    "Nutral": ['lmao']
}

# Initialize sentiment scores for each category
category_sentiment = {category: [] for category in categories}

# Analyze text and categorize sentences
text = """
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant. Fuck the Blob the Blob sucks. 
"""

blob = TextBlob(text)

# Iterate over sentences and categorize them
for sentence in blob.sentences:
    sentence_lower = sentence.lower()
    for category, keywords in categories.items():
        if any(keyword in sentence_lower for keyword in keywords):
            category_sentiment[category].append(sentence.sentiment.polarity)

# Calculate average sentiment polarity for each category
for category, sentiment_scores in category_sentiment.items():
    if sentiment_scores:
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        print(f"Category: {category}, Average Sentiment Polarity: {avg_sentiment:.3f}")
    else:
        print(f"No sentences found for category: {category}")
