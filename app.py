import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english')) - {'not'}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<[^>]+>', ' ', text)         
    text = re.sub(r'[^a-z\s]', ' ', text)        
    text = re.sub(r'\s+', ' ', text)            
    return ' '.join([word for word in text.split() if word not in stop_words])

st.title("Headphone Reviews Phrase Analyzer")

df = pd.read_csv('/Users/yashashari/Desktop/Prod_Review/Data/Reviews.csv')

df['clean'] = df['content'].apply(clean_text)

cv = CountVectorizer(ngram_range=(2,3), min_df=5)

X = cv.fit_transform(df['clean'])

phrase_freq = zip(cv.get_feature_names_out(), X.sum(axis=0).A1)

top_phrases = sorted(phrase_freq, key=lambda x: x[1], reverse=True)[:20]

phrases, counts = zip(*top_phrases)

fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x=list(counts), y=list(phrases), ax=ax)

ax.set_xlabel("Count")
ax.set_ylabel("Phrase")
ax.set_title("Top 20 Common Phrases in Headphone Reviews")

st.pyplot(fig)



