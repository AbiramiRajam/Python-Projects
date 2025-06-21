# Predicting Top Honeymoon Destination Countries Using Travel and TravelHacks Reddit

##  Objective

To classify subreddit posts and identify top and bottom honeymoon destinations using sentiment analysis and machine learning.



##  Motivation & Problem Statement

Online travel forums like Reddit contain valuable, first-hand travel experiences. However, there's limited **automated insight** into how these public opinions reflect destination popularity—especially for **honeymoon planning**.

This project aims to bridge that gap by:
- Extracting travel-related discussions from Reddit
- Using NLP to classify and analyze sentiment
- Identifying top honeymoon destinations based on user sentiment



## 1. Data Collection

- Reddit posts were scraped from two subreddits: `travel` and `travelhacks` using the Reddit API.
- Data collected includes post ID, creation time, title, author, selftext, number of comments, score, and subreddit name.
- Duplicate posts were avoided by checking unique timestamps (`created_utc`) before appending new data.
- The data was saved into CSV files for subsequent processing and analysis.



## 2. Data Cleaning and Preparation

- Combined `title` and `selftext` columns into a new `combined_text` column for unified text analysis.
- Removed posts with missing or null text data to ensure quality input for modeling.
- Created a binary column `is_honeymoon` to mark posts containing the word "honeymoon" (case-insensitive).
- Applied text preprocessing steps such as lowercasing, removing stopwords, and tokenization where necessary.



## 3. Data Processing and Feature Engineering

- Extracted locations mentioned in honeymoon posts using spaCy’s Named Entity Recognition (NER) to identify geographical entities.
- Verified location entities against a country database (`pycountry`) to confirm valid country names.
- Calculated sentiment scores for each post using VADER sentiment analyzer to quantify positive or negative sentiment.
- Aggregated sentiment scores by country to identify top and bottom honeymoon destinations based on user sentiment.



## 4. Modeling

- **Baseline Model:** Logistic Regression using TF-IDF vectorized `combined_text` for classifying posts into `travel` or `travelhacks`.
- **Final Model:** Voting Classifier ensemble combining Logistic Regression, Random Forest, and SVM classifiers for improved accuracy.
- Models were trained and evaluated using train-test splits and cross-validation to ensure robustness.



## 5. Model Evaluation

- **Baseline Model Performance:**
  - Accuracy: 81.75%
  - Balanced precision and recall around 81-83% for both classes.
  - Provided a reliable initial benchmark for classification.

- **Final Model Performance:**
  - Accuracy improved to approximately 86.5%.
  - Precision and recall showed significant improvement, particularly in correctly classifying Travel and TravelHacks posts.
  - Ensemble approach leveraged strengths of individual models for better overall prediction.



## 6. Insights and Visualization

- Identified top 5 honeymoon countries based on average sentiment scores from relevant posts.
- Bar plots visually highlighted the most loved and appreciated honeymoon destinations among Reddit users.
- These insights provide valuable information for travel marketers, planners, and honeymooners seeking popular destinations.



## 7. Conclusion

- Combining subreddit classification with sentiment analysis effectively predicts user preferences for honeymoon destinations.
- The Voting Classifier ensemble demonstrated the best classification performance.
- Sentiment-based location analysis revealed clear user sentiment trends, enabling data-driven decision making in travel-related contexts.



## 8. Future Work

- Incorporate more advanced NLP techniques such as topic modeling to better understand user discussions.
- Expand dataset by including additional travel-related subreddits for broader analysis.
- Explore temporal trends in honeymoon destinations to see how preferences evolve over time.
