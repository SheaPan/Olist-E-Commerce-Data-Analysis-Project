import pandas as pd
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from itertools import chain
import nltk
import os

# set theme words
THEME_MAPPING = {
    'Product Quality': [
        'broken', 'defective', 'poor', 'terrible', 'wrong', 'leak', 'scratch', 'damage', 
        'excellent', 'great', 'perfect', 'solid', 'sturdy', 'durable', 'high', 'flawless', 'quality'
    ],
    'Delivery/Shipping': [
        'delay', 'late', 'shipping', 'tracking', 'missing', 'long', 'unopened', 'arrive',
        'fast', 'quickly', 'prompt', 'earlier', 'secure', 'speed', 'delivery', 'delivered', 'arrived'
    ],
    'Customer Service': [
        'response', 'agent', 'answer', 'support', 'rude', 'call', 'email', 'contact',
        'helpful', 'friendly', 'solved', 'resolved', 'polite', 'professional', 'amazing', 'service'
    ],
    'Order/Billing': [
        'refund', 'charged', 'payment', 'bill', 'cancel', 'fee', 'easy', 'simple', 'order'
    ],
    'Packaging': [
        'box', 'tape', 'package', 'seal', 'open', 'well', 'packed', 'protected', 'unopened'
    ],
    'General Sentiment': [
        'bad', 'good', 'happy', 'unhappy', 'dissapoint', 'satisfied', 'best', 'worst'
    ]
}

# group keywords in themes
KEYWORD_TO_THEME = {}
for theme, words in THEME_MAPPING.items():
    for word in words:
        if word not in KEYWORD_TO_THEME:
            KEYWORD_TO_THEME[word] = theme

# define more stopwords
english_stopwords = set(stopwords.words('english'))
custom_noise_words = set([
    'one', 'two', 'even', 'still', 'like', 'would', 'want', 'buy', 
    'recommend', 'time', 'already', 'waiting', 'store', 'office', 
    'website', 'far', 'post', 'didnt', 'dont', 'doesnt', 'havent',
    'received', 'delivered', 'arrived', 'sent', 'made', 'came', 'bought', 
    'receive', 'purchase', 'return', 'exchange', 'item', 'lannister', 'products', 'problem', 'message', 
    'get', 'go', 'use', 'know', 'see', 'say', 'look', 'find', 'make'
])

# final stopwords
final_stopwords = english_stopwords.union(custom_noise_words)
lemmatizer = WordNetLemmatizer()

# clean

def clean_and_generate_ngrams(text, min_len=3):
    if pd.isna(text) or not str(text).strip():
        return []
    
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text) 
    text = re.sub(r'\d+', ' ', text)
    words = word_tokenize(text)
    
    # 1-gram
    cleaned_1grams = []
    for word in words:
        if word in KEYWORD_TO_THEME or (word not in final_stopwords and len(word) >= min_len):
            lemmatized_word = lemmatizer.lemmatize(word)
            cleaned_1grams.append(lemmatized_word)
            
    all_themed_ngrams = []
    
    for word in cleaned_1grams:
        theme = KEYWORD_TO_THEME.get(word, 'General Keyword') 
        all_themed_ngrams.append((word, theme))

    # 2-grams
    if len(cleaned_1grams) >= 2:
        for gram in ngrams(cleaned_1grams, 2):
            keyword = "_".join(gram)
            theme_1 = KEYWORD_TO_THEME.get(gram[0])
            theme_2 = KEYWORD_TO_THEME.get(gram[1])

            if theme_1:
                theme = theme_1
            elif theme_2:
                theme = theme_2
            else:
                theme = 'General Ngram'
                
            all_themed_ngrams.append((keyword, theme))
                
    return all_themed_ngrams

# generate Keywords and Frequency DataFrame

def generate_keyword_theme_freq_df(data_frame, sentiment_label):
    print(f"dealing with {sentiment_label}...")
    target_df = data_frame[data_frame['sentiment_category'] == sentiment_label].copy()

    all_ngrams_list = list(chain.from_iterable(
        target_df['review_message'].apply(clean_and_generate_ngrams).tolist() + 
        target_df['review_title'].apply(clean_and_generate_ngrams).tolist()
    ))
    
    ngram_theme_counts = Counter(all_ngrams_list)
    
    records = []
    for (keyword, theme), frequency in ngram_theme_counts.items():
        records.append({
            'Theme': theme,
            'Keyword': keyword,
            'Frequency': frequency,
            'Sentiment_Type': sentiment_label
        })
        
    df_freq = pd.DataFrame(records)
    
    # only save top 2000
    return df_freq.sort_values(by='Frequency', ascending=False).head(2000)

# main code

file_path = 'keywords.csv'

df = pd.read_csv(file_path)

df_negative_themes = generate_keyword_theme_freq_df(df, 'Negative')
df_positive_themes = generate_keyword_theme_freq_df(df, 'Positive') 

df_all_themes = pd.concat([df_negative_themes, df_positive_themes])

theme_keyword_table_filename = 'olist_reviews_word_datasets.csv'
df_all_themes.to_csv(theme_keyword_table_filename, index=False, encoding='utf-8')

print(f"✅ file saved: {theme_keyword_table_filename}")