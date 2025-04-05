# Project 3: Web APIs & NLP

### Problem Statement

A couple, infrequent travelers, are seeking unique and highly-rated honeymoon destinations. Utilized Reddit posts from 'travel' and 'travel hacks' subreddits, the goal is to develop a model that fairly predicts the origin of each post. In addition, the model identifies posts from which subreddit in this case 'travel' dataset or travel hacks dataset. Model analyzed sentiment scores, thus providing the couple with a list of honeymoon spots. 



#### About API

For this project, you will be using [PRAW](https://praw.readthedocs.io/en/stable/index.html) to collect posts from two different subreddits. 

To help you get started, we have a [notebook](./Reddit-PRAW-tutorial.ipynb) detailing the process of creating an app and obtaining your API credentials.

Note: Rather than working in this template notebook, make a brand new "scraping" notebook (or script), with your own unique work and comments, so you can use this project in a portfolio!

---

### Data Collection

Data Collection:

Source Reddit website using PRAW Web API

Travel subreddit is a community on Reddit where users discuss topics related to travel. 
 
TravelHacks is a community on Reddit sharing tips, tricks, and strategies to make travel more affordable, efficient, and enjoyable. 

## Features Used for Prediction

| Column        | Non-Null Count | Dtype    | Description                                                   |
|---------------|----------------|--------- | --------------------------------------------------------------|
| id            | 1103           | object   | unique identifier assigned to each Reddit post                |
| created_utc   | 1103           | float64  | column stores the timestamp of when the post was created      |
| title         | 1103           | object   | title of the Reddit post                                      |
| author        | 1059           | object   | contains the username of the Reddit user who created the post |
| selftext      | 493            | object   | column holds the body text of the Reddit post                 |
| num_comments  | 1103           | int64    | number of comments that the post has received                 |
| score         | 1103           | int64    | score (upvotes minus downvotes) of the Reddit post            |
| subreddit     | 1103           | object   |the name of the subreddit where the post was submitted         |




---

### API 

Using Web API and Natural Language Processing collected 1000 unique subreddits posts for the columns id, created_utc, title, author, selftext, num_comments, score, subreddit

Removed Duplicates
Converted text columns to lower case for easier readability
Created_utc converted to human readable format
Lot of selftext is missing and hence combined title and selftext to gain more meaningful data
Filled Unknown to missing authors


---

## Data Cleaning

Exploratory Data Analysis

Performed Exploratory Data Analysis separately to identify statistical analysis of both travel and travel hacks subreddits

Displayed sample data using df.head() method
Performed summary statistics using df.describe
Visualize the Distribution of features 
Explored correlation between features
Text Data Exploration
Tokenization
Bigrams and Trigrams analysis
Checks for balance of class/target feature
Explored score and number of posts

##
Stop words to remove unnecessary words
Tokenized converts textual data into a format that can be processed
Modeled Baseline Model as Logistic Regression with TF-IDF
Vectorize text using TF-IDF , using TfidfVectorizer(stop_words='english', ngram_range=(1, 1)) to converts text documents into numerical feature vectors using TF-IDF to capture the importance words and performed baseline predictions

Iterated Models to improve baseline score. Iterated to Random Forest Classifier and compared with baseline predictions but score is much lower than baseline model

Iterated to tune performance using GridSearchCV for hyperparameter tuning but still it did not help to increase the accuracy

After Iterations considered to incorporate Logistic Regression with TF-IDF with SVM Support Vector Machines (SVMs) and xgboost as an ensemble model

combine numerical and categorical features and Create the Voting Classifier and it slightly improves the model accuracy.

Generate Confusion matrix to check sensitivity and specificity

Total Records ≈ 2110
Test Set Size: 20% of 2000 = 0.2 * 2000 = 422 posts
Training Set Size: 80% of 2000 = 0.8 * 2000 = 1600 posts


Predicted/Actual
Travel (Predicted)
TravelHacks (Predicted)
Travel (Actual)
191 (True Positive)
10 (False Negative)
TravelHacks (Actual)
48 (False Positive)
173 (True Negative)

Performed sentimental analysis for text and score using Vader

Created a new column called is_honeymoon to identify patterns in combined_text(title and selftext) and mapped 1 if it contains honeymoon word and 0 if it does not contain honeymoon word

#installed spaCy for advanced Natural Language Processing (NLP) in Python to recognize the location and places using pip install spacy

Identified places and cleaned places columns and visualized location vs sentiment_score to predict places having positive reviews

Finalized optimized model to deploy to production based on accuracy score of ensemble model using test data



### Recommendatations

Can improve model performance with hyperparameter optimization using techniques like grid search or Bayesian optimization, combined with k-fold cross-validation, to maximize model performance and generalization.

Still further improve model predictions by Analyzing user preferences and trending spots.

---
