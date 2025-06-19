### **Project Overview**

#### **Objective:**
- **Problem Statement**: Predict the sale price of residential homes in Ames, Iowa based on various property features to assist in accurate property evaluations for real estate decision-making.
- **Goal**: Develop a predictive model to estimate home sale prices using a variety of features such as house size, number of rooms, neighborhood, and year built.

#### **Data Source:**
- The data comes from the **Ames Housing Dataset**, which contains 2930 samples and 76 features, including both categorical and continuous variables.

#### **Features:**
- Key features for prediction include:
  - **Numerical features**: `Gr Liv Area`, `TotRms AbvGrd`, `Overall Qual`, `Year Built`, `1st Flr SF`, `TotRms AbvGrd`
  - **Categorical features**: `Neighborhood`, `Garage Type`, `Pool QC`, `Fireplaces`
  - **Target variable**: **SalePrice**

#### **Challenges:**
- **Missing Data**: Some features had missing values, which were addressed through imputation.
- **Feature Encoding**: Categorical features had to be transformed into numerical values using One-Hot Encoding.
- **Outliers**: Certain extreme values, particularly for high-value properties, needed to be considered for robust predictions.

#### **Goal of the Model:**
- Develop a model that generalizes well to unseen data and can provide accurate price predictions for homes of various price ranges.

#### **Approach:**
- **Preprocessing**: Handle missing values, scale numerical features, and encode categorical variables.
- **Modeling**: Apply **Ridge regression** to capture relationships between features and target price while preventing overfitting through regularization.
- **Evaluation**: Use metrics like **RMSE** and **R²** to assess model performance and make improvements.

#### **Outcome Expected:**
- A model that can predict the sale price of homes based on their features with high accuracy, supporting better decision-making in real estate investment.

#### **Top 5 Most Accurate Predictions:**
The Ridge model performed exceptionally well on these 5 properties, with very small errors between the actual and predicted sale prices:
- **Prediction Error** was minimal, with errors as low as **$126.39** for the property with an actual price of **$390,000**.
- The **highest error** in this group was **$223.75** for a property valued at **$154,300**.
These results suggest that for mid-range to lower-priced homes, the model is highly accurate, offering strong predictive power for this price segment.

| Actual Price | Predicted Price | Prediction Error |
|--------------|-----------------|------------------|
| $390,000     | $389,873.61     | $126.39          |
| $175,900     | $176,045.30     | $145.30          |
| $302,000     | $302,160.61     | $160.61          |
| $173,733     | $173,897.32     | $164.32          |
| $154,300     | $154,076.25     | $223.75          |

#### **Bottom 5 inaccurate Predictions:**
On the flip side, these properties had large discrepancies between the actual and predicted sale prices, indicating areas where the model struggles:
- The **largest error** occurred for a property with an actual price of **$184,750**, where the predicted price was off by a staggering **$375,378**.
- The **highest prediction error** for high-value homes was **$175,039** for a property priced at **$611,657**.
- These significant errors suggest that the model may face challenges with **high-end properties** or **outliers** in the data, where it tends to underperform, possibly due to the complexity of predicting extreme values.

| Actual Price | Predicted Price | Prediction Error |
|--------------|-----------------|------------------|
| $610,000     | $478,417.09     | $131,582.91      |
| $625,000     | $471,948.89     | $153,051.11      |
| $582,933     | $418,201.83     | $164,731.17      |
| $611,657     | $436,617.86     | $175,039.14      |
| $184,750     | $560,128.15     | $375,378.15      |
