# Business Survival Analysis in San Francisco – Focused on Supervisor District 3 Funding

### Executive Summary

Predictive analytics on business registration trends can provide insights on prioritization of neighborhoods within San Francisco Supervisor District 3 for development funds by understanding business emergence and density evolution. This project specifically analyzes factors influencing business survival within Supervisor District 3, aiming to predict administrative closure using survival analysis to support targeted funding decisions.

---

### Why Model Business Survival for District 3 Funding Decisions?

Understanding why some businesses in San Francisco Supervisor District 3 are more likely to close administratively than others offers valuable insights specifically for the funding team. This analysis can help:

- **Targeted Resource Allocation**  
  Identify specific business segments or neighborhoods within District 3 that exhibit higher closure rates, allowing for the strategic allocation of development funds and support programs to the most vulnerable areas.

- **Informed Funding Strategies**  
  Understand the factors contributing to business instability within the district, enabling the funding team to design more effective and tailored interventions to promote business longevity.

- **Performance Measurement**  
  Establish a baseline understanding of business survival in District 3 against which the impact of funding initiatives can be measured over time.

- **Prioritization of Investment**  
  Inform decisions about where and what types of businesses within Supervisor District 3 would benefit most from development funds to maximize economic impact and sustainability.

---

### Goal

Predict the likelihood of a business being administratively closed over time specifically within San Francisco Supervisor District 3 using survival analysis to inform funding decisions.

---

### Data Collection

A Python script collected San Francisco business registration data from the Open Data API (`https://data.sfgov.org/resource/g8m3-pdis.json`), handling pagination, deduplication, storage in CSV format, error handling, progress tracking, and rate limiting. The dataset was subsequently filtered to include only businesses within Supervisor District 3.

---

### Data Cleaning and Preprocessing

- Standardized city names and corrected "San Francisco" misspellings.
- Renamed geographic columns.
- Filtered data for San Francisco, then specifically for Supervisor District 3.
- Converted dates and calculated `business_age`.
- Encoded administrative closures and handled missing values in the supervisor district column.

---

### Metrics

- **Duration Variable**: `business_age` (operational duration)  
- **Event Indicator**: `administratively_closed` (1 if closed, 0 if operational)  
- **Model Evaluation**: Concordance index, hazard ratios, p-values from the Cox Proportional Hazards model

---

### Findings Specific to District 3

- Newer businesses in District 3 have a higher closure risk.
- Tax features (e.g., `transient_occupancy_tax`) and `naic_code_description` influence survival within the district.
- Certain zip codes and industries in District 3 correlate with varying survival likelihood.

---

### Risks, Limitations, and Assumptions

- Administrative closure may not equal actual business failure.
- Businesses without closure dates are assumed operational.
- The Cox Proportional Hazards model assumes proportional hazards over time.
- The model’s findings are specific to data from Supervisor District 3.

---

### Exploratory Data Analysis (EDA) for District 3

Visualized business trends within Supervisor District 3 using bar charts and time series plots:

- Top license descriptions  
- Registrations per year/decade  
- Average business age by license type  
- Top neighborhoods by business count  
- Openings vs. closures over time  

Outliers in `business_age` were removed for visualization, only last 10 years trends are taken into consideration for visualization

---

### Data Preprocessing and Baseline Modeling for District 3

- **Baseline Model**: Survival Analysis using Cox Proportional Hazards Model
- Filled missing `naic_code_description` with 'Missing'
- One-hot encoded `naic_code_description`
- Selected features: tax fields, `business_zip`, `business_age`, `administratively_closed`
- Filtered for complete records within District 3
- Fitted model with `business_age` as duration and `administratively_closed` as event
- Generated summary of feature impacts on business survival

---

### Why Survival Analysis and CoxPHFitter?

Survival analysis is ideal for modeling *time until an event* (business closure) and handling censored data (businesses still operating at data collection). The Cox Proportional Hazards (CoxPH) model is chosen for its ability to:

- Estimate the hazard rate based on multiple predictors  
- Quantify risk changes (hazard ratios)  
- Avoid assumptions about the underlying survival distribution  

This makes it well-suited for guiding targeted funding strategies in District 3.

---

### Model Evaluation – Baseline Model Interpretation (District 3)

- **Concordance**:  Model performance is evaluated based on Concordance

---

### Model Enhancement: PCA + Cox Proportional Hazards Model (District 3)

- Removed unnecessary columns and selected numeric ones  
- Imputed missing values with zero  
- Standardized features and applied PCA (10 components)  
- Target variables: `business_age`, `administratively_closed`  
- Selected PC3 and PC5 as model inputs  
- Split data into train/test sets  
- Fitted model and analyzed PCA loadings  
- Identified top and bottom contributing features for PC3 and PC5  
- Predicted survival times on test set  

---

### Interpretation of Enhanced Model (District 3)

- **Concordance**: 0.74 

---

### Top Contributing Features

The top contributing features for both PC3 and PC5 reflect the variables that have the most substantial influence on the model’s prediction.

#### Top Features for PC3
- **Transient Occupancy Tax**: 0.41  
  Higher values increase the likelihood of closure.
- **Parking Tax**: 0.38  
  Also positively correlated with administrative closure.

#### Top Features for PC5
- **Parking Tax**: 0.66  
  Strong positive association with administrative closure.
- **Transient Occupancy Tax**: 0.44  
  Increases the risk of closure.
- **Neighborhood Analysis**: 0.04  
  Certain neighborhoods have slightly higher closure risk.
- **Business Zip**: -0.01  
  Minor influence on closure risk.

---

### Bottom Contributing Features

These features have the least influence on model predictions.

#### Bottom Features for PC3
- **Planning Area**: -0.03  
  Minimal effect on closure likelihood.
- **Neighborhood Analysis**: -0.02  
  Slight negative correlation with closure.
- **Supervisor District**: 0.00  
  No measurable effect.

#### Bottom Features for PC5
- **Business Age**: -0.56  
  Older businesses are less likely to close.
- **Administratively Closed**: -0.21  
  Slight negative association in PC5.
- **Planning Area**: -0.10  
  Weak overall impact.

---

## Summary of Business Survival Trends

---

### Business Survival by Neighborhood (5 and 10 Years)

Based on the survival analysis, the overall business survival rates across neighborhoods are:

- **Average 5-Year Survival Rate**: 11.03%  
- **Average 10-Year Survival Rate**: 7.23%

These survival rates provide a clear indication of the overall business longevity across neighborhoods.

- **Best Performing Neighborhood (5-Year)**: Russian Hill — 14.81%  
- **Bottom Performing Neighborhood (5-Year)**: Nob Hill — 8.42%

The difference in survival rates between neighborhoods highlights areas where business conditions may need improvement.

---

### Business Survival by License Type (5 and 10 Years)

Based on the survival analysis, the overall business survival rates across license types are:

- **Average 5-Year Survival Rate**: 10.51%  
- **Average 10-Year Survival Rate**: 6.57%

These survival rates reveal distinct patterns of business longevity linked to each license type.

- **Best Performing License Type (5-Year)**: Restaurant 1,000 - 2,000 Sqft — 12.75%  
- **Bottom Performing License Type (5-Year)**: Healthy Housing Hotels — 8.3%

The variation in survival rates across license types highlights areas where business conditions could be improved.

---

## Overall Recommendations

### Neighborhoods

- Neighborhoods with higher survival rates should be further nurtured with targeted economic development programs.  
- Neighborhoods with lower survival rates should receive tailored support such as:
  - Grants  
  - Infrastructure improvements  
  - Mentorship programs

### License Types

- License types with higher survival rates could serve as models for businesses in struggling sectors.  
- Focus efforts on business types with lower survival rates by:
  - Identifying barriers to success  
  - Offering targeted programs, policy changes, and financial support

---

### Future Recommendations

- Incorporate additional data sources such as:
  - **Crime data** 
  - **Tourist data**  
  - **Employment data**  
  - **Other socio-economic indicators**

  This can enhance the model's predictive power and provide a more comprehensive understanding of the factors influencing business survival.
