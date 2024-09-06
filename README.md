# SpaceX Falcon 9 First Stage Landing Prediction

## Table of Contents

Project Overview

Data Collection

Exploratory Data Analysis (EDA)

Machine Learning Models

Results and Insights

## Project Overview
This project aims to predict whether the first stage of SpaceX's Falcon 9 rocket will successfully land, which is critical for the reusability of rockets and reducing launch costs. The project involves gathering data from SpaceX launches, conducting Exploratory Data Analysis (EDA), and building machine learning models to predict landing outcomes based on various factors such as launch site, payload mass, and orbit type. The insights gathered from this analysis can help a competing company, Space Y, optimize their launches and reduce costs by reusing rockets like SpaceX.

## Data Collection
The dataset used for this project includes information on SpaceX Falcon 9 launches. Key columns in the dataset include:

+ Flight Number: Unique identifier for each launch.

+ Date: Date of the launch.

+ Booster Version: Version of the Falcon 9 booster used.

+ Payload Mass: The mass of the payload being launched (in kg).

+ Launch Site: The launch site from which the rocket was launched.

+ Orbit: Target orbit for the payload.

+ Outcome: Whether the rocket successfully landed or failed.

+ LandingPad: The landing platform used.

+ Class: The target variable indicating whether the landing was successful (1) or not (0).

## Exploratory Data Analysis (EDA)
I performed EDA to gain insights into the factors that influence the success of the first stage landing:

+ Payload Mass vs. Success: I found that lighter payloads tend to have higher landing success rates, particularly with the FT and B4 booster versions.

+ Launch Site Analysis: Some launch sites, such as KSC LC-39A, showed a higher success rate (76.9%) compared to others like CCAFS, which had a higher failure rate.

+ Orbits and Success: Orbits like LEO (Low Earth Orbit) showed higher success rates for heavier payloads, while GTO (Geostationary Transfer Orbit) had mixed outcomes.

==> These insights helped me better understand how different variables affect landing success.

## Machine Learning Models
I built several machine learning models to predict whether the Falcon 9 first stage would successfully land:

- Logistic Regression

- Support Vector Machine (SVM)

- K-Nearest Neighbors (KNN)

- Decision Tree

## Methodology
1. Data Preparation:

- Standardized the data for all features.
  
- Split the data into training and testing sets (80/20 split).
  
- Created a new column, Class, indicating the target variable (1 for successful landings, 0 for failures).
  
2. Model Tuning:
   
- Used GridSearchCV to find the best hyperparameters for each model.
  
3. Model Evaluation:
   
- Evaluated the models using accuracy, precision, and recall metrics.
  
- The Decision Tree model performed the best, with a high accuracy rate and minimal false predictions, as seen in the confusion matrix.
  
### Confusion Matrix (Decision Tree):
The confusion matrix showed:

+ True Positives: 12 correctly predicted successful landings.
  
+ True Negatives: 5 correctly predicted unsuccessful landings.
  
+ False Positives: 1 incorrect prediction of a landing.
  
+ False Negatives: 0 incorrect predictions of no landing.
  
## Results and Insights
The following are key insights and conclusions from the project:

1. First-Stage Reuse: The success of first-stage landings is a critical factor in reducing launch costs. The ability to predict these outcomes allows Space Y to strategically plan for reusability, similar to SpaceX's cost-saving model.

2. Launch Site Performance: Launch sites like KSC LC-39A showed consistently high success rates, making them ideal for future launches.

3. Payload Mass and Success: Lighter payloads are more likely to result in successful landings, particularly with newer booster versions such as FT and B4.

4. Model Performance: The Decision Tree model was the most effective in predicting landing outcomes, with high accuracy and minimal misclassification, making it suitable for predicting rocket reusability.
