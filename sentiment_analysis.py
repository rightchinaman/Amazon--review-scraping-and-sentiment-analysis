import pandas as pd
from textblob import TextBlob

file_path = 'D:\\Amazon scraping\\reviews.xlsx'
df = pd.read_excel(file_path)

def get_sentiment(text):
    try:
        blob = TextBlob(str(text))
        sentiment_polarity = blob.sentiment.polarity
        return sentiment_polarity
    except Exception as e:
        print(f"Error analyzing sentiment for text: {text}. Error: {e}")
        return None

df['sentiment'] = df['text'].apply(get_sentiment)

def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_label'] = df['sentiment'].apply(classify_sentiment)

output_file = 'reviews_with_sentiment.xlsx'
df.to_excel(output_file, index=False)

print(f"Sentiment analysis results saved to {output_file}")
