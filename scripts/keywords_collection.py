from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain
import re
import pandas as pd

english_stopwords = set(stopwords.words('english'))
df= pd.read_csv('reviews.csv')
def clean_and_tokenize_english(text, min_len=3):
    if pd.isna(text) or not str(text).strip():
        return []
    
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    words = word_tokenize(text)
    
    # filter stop words and lenth < min_len
    return [word for word in words if word not in english_stopwords and len(word) >= min_len]

# filter sentiment category, create Keyword and Frequency DataFrame
def generate_word_freq_df(data_frame, sentiment_label):
    target_df = data_frame[data_frame['sentiment_category'] == sentiment_label].copy()

    all_words_list = list(chain.from_iterable(
        target_df['review_message'].apply(clean_and_tokenize_english).tolist() + 
        target_df['review_title'].apply(clean_and_tokenize_english).tolist()
    ))
    
    word_counts = Counter(all_words_list)
    df_freq = pd.DataFrame(word_counts.items(), columns=['Keyword', 'Frequency'])
    df_freq['Sentiment_Type'] = sentiment_label
    
    # only save top 500
    return df_freq.sort_values(by='Frequency', ascending=False).head(500)

df_negative_keywords = generate_word_freq_df(df, 'Negative')
df_positive_keywords = generate_word_freq_df(df, 'Positive')

# combine positive and negative DataFrame
df_all_keywords = pd.concat([df_negative_keywords, df_positive_keywords])

keyword_table_filename = 'keyword.csv'
df_all_keywords.to_csv(keyword_table_filename, index=False, encoding='utf-8')

print(f"✅ Keyword csv file saved:{keyword_table_filename}")