import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')
nltk.download('stopwords')

def analyze_reviews(file_path):

    df = pd.read_excel(file_path)

    df.dropna(subset=['text'], inplace=True)

    sia = SentimentIntensityAnalyzer()
    
    all_text = ' '.join(df['text'])
    words = [word for word in all_text.split() if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    
    word_counts = Counter(filtered_words)
    
    df['sentiment'] = df['text'].apply(lambda x: sia.polarity_scores(x)['compound'])
    
    best_keywords = df.loc[df['sentiment'] > 0, 'text'].str.cat(sep=' ').split()
    worst_keywords = df.loc[df['sentiment'] < 0, 'text'].str.cat(sep=' ').split()

    best_word_counts = Counter(best_keywords)
    worst_word_counts = Counter(worst_keywords)

    best_common = best_word_counts.most_common(10)
    worst_common = worst_word_counts.most_common(10)

    return best_common, worst_common

def plot_keywords(best, worst):

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(*zip(*best), color='green')
    plt.title('Best Keywords')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.bar(*zip(*worst), color='red')
    plt.title('Worst Keywords')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

file_path = 'reviews.xlsx' 
best_keywords, worst_keywords = analyze_reviews(file_path)
plot_keywords(best_keywords, worst_keywords)