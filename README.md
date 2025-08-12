# Headphone Reviews Phrase Analyzer

A Streamlit app that analyzes headphone reviews by extracting and visualizing the most common 2- and 3-word phrases from the review content. 
This helps identify frequent customer sentiments and common features mentioned.

---

## Features

- Cleans review text by removing HTML tags, special characters, and stopwords (except 'not')
- Extracts top 20 common 2- and 3-word phrases using n-gram frequency analysis
- Visualizes results with a bar chart

---

## How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/YashasHari/Headphone_Review_Analysis.git
   cd headphone-review-analysis

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the app:

   ```bash
   streamlit run app.py

## Deployment
   Deploy on Streamlit Cloud or any Python-supported cloud. Update the dataset path in app.py to a relative path or upload the dataset to the cloud environment.

## Requirements
  - streamlit
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - nltk

## Live Demo
- Try the app online here:
  [Headphone Reviews Phrase Analyzer](https://headphone-review-analysis.streamlit.app/)

## Notes

- The app downloads NLTK stopwords on first run.
- Dataset path in app.py is currently an absolute local path; update before deployment.
   
   
   
