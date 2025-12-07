import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df= pd.read_csv('olist_order_reviews.csv')

vader_analyzer = SentimentIntensityAnalyzer()

positive_threshold = 0.05
negative_threshold = -0.05

conditions = [
    (df['vader_sentiment_compound'] >= positive_threshold),
    (df['vader_sentiment_compound'] <= negative_threshold)
]

choices = ['Positive', 'Negative']
df['sentiment_category'] = np.select(conditions, choices, default='Neutral')

print("✅ 'sentiment_category' column is added")

# 3. add cluster_lable column
features = df[['review_score', 'vader_sentiment_compound']].copy()

# standerd the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# KMeans
k = 4
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster_label'] = kmeans.fit_predict(scaled_features)
print(f"✅ 'cluster_label' column adds ({k} group")

# save to csv file
df.to_csv('reviews.csv', index=False, encoding='utf-8')
print(f"✅ Table saved")

# check cluster group information
cluster_summary = df.groupby('cluster_label')[['review_score', 'vader_sentiment_compound']].mean()

print("\n--- (Group Characteristics Summary) ---")
print(cluster_summary)