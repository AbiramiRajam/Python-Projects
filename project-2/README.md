# Project 2 - Ames Housing Data and Kaggle Challenge

Welcome to Project 2! 

Short Overview of Ames Housing Dataset

Ames is a real place in Iowa, United States. It is a city located in Story County, in the central part of the state. Ames is home to Iowa State University, which is a major public research university. The city is known for its academic, research, and technological contributions, and it's an important educational and economic hub in the region.
The Ames Housing dataset, as mentioned earlier, uses data collected from this city, specifically about homes and their sale prices.


**Primary Learning Objectives:**

## Datasets

'./datasets/train.csv'
'./datasets/test.csv'

## Set-up

# Urban vs Rural Sale Price Prediction: Feature Overview

This document provides an overview of the selected features in the Ames Housing dataset used for predicting urban vs rural sale prices.

## Features Used for Prediction

| Feature Name      | Data Type  | Description/Explanation |
|-------------------|------------|-------------------------|
| **Lot Area**      | Numeric   | The lot size in square feet. Larger lots often correlate with higher prices, especially in suburban areas. |
| **Gr Liv Area**   | Numeric   | The above-ground living area in square feet. Larger living areas generally indicate higher sale prices. |
| **Overall Qual**  | Ordinal   | Overall quality of the house, rated from 1 (low) to 10 (high). Higher ratings indicate better construction quality and design. |
| **Total Bsmt SF** | Numeric   | The total basement area in square feet. Homes with finished basements tend to have higher sale prices. |
| **Garage Cars**   | Numeric   | The number of cars the garage can accommodate. More garage space is often associated with higher home values. |
| **Bsmt Qual**     | Ordinal   | Quality of the basement. Typically rated from 1 (low) to 4 (high). Homes with higher basement quality tend to have a higher price. |
| **Garage Qual**   | Ordinal   | Quality of the garage, similarly rated on a scale from 1 to 4. A higher garage quality can influence the sale price positively. |
| **Lot Config**    | Categorical | Configuration of the lot, such as 'Inside', 'Corner', 'CulDSac', 'FR2', and 'FR3'. These factors can affect a property's desirability and price. |
| **Overall Cond**  | Ordinal   | The overall condition of the property. A higher condition rating correlates with a higher sale price. |


## Conclusion

I took the above Features into consideration for my Urban Vs Rural Price Prediction.
I used Linear Regression Model to build my model and plotting visuals to predict the relationships between features.
After Analyzing into each feature i come with few interesting Assumptions
These assumptions and observations indicate that quality metrics, such as overall house quality, garage quality, and kitchen quality, are strong predictors of house prices in both urban and rural settings. There are other important metrics like Gr Live Area gives high prediction and other Area related metrics gives a moderate prediction of Urban vs Rural Housing prices.
While secondary features like lot shapes and area show some impact, they are not as dominant. The MS Zoning, Street type, and Neighborhood factors also significantly affect the sale price, with specific categories having a higher correlation with urban or rural market prices.

R-squared: 0.8444
RMSE: 30409.748727362963

By focusing on these key assumptions, we can improve the predictive power of our model for urban vs rural housing price prediction.
---
