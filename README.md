# Analysis of Social Media Usage: Predicting LinkedIn Activity with a Streamlit App

## Introduction

In the digital era, social media platforms have become central to personal and professional networking. LinkedIn, as a professional networking site, serves as a pivotal tool for career development and professional connections. This report delves into an analysis of social media usage with a particular focus on LinkedIn. We utilize a dataset detailing various aspects of social media usage to explore factors influencing LinkedIn activity among users.

## Methodology

### Data Acquisition and Initial Exploration

The analysis commenced with the importation of essential Python libraries, including pandas for data manipulation, numpy for numerical operations, seaborn and matplotlib for data visualization, and scikit-learn for machine learning tasks.

The dataset, loaded into a DataFrame named `S`, contains 1502 entries and 89 features, encompassing a wide array of variables such as respondent ID, survey completion date, language, state, demographic information, and specific social media usage behaviors.

### Data Cleaning and Transformation

A crucial step in the analysis involved defining a function `clean_sm` to transform certain dataset variables into a binary format. This transformation was applied to various features including LinkedIn usage (identified as `sm_li`), income, education, parental status, marital status, gender, and age. Entries with missing or unrealistic values for income, education, and age were replaced with `NaN` to ensure data quality.

### Data Analysis

#### Descriptive Analysis

The cleaned dataset `ss` was analyzed to understand the distribution and characteristics of the study population. Descriptive statistics highlighted the average age, income level, education status, marital status, gender distribution, and LinkedIn usage among the respondents. The age distribution was visualized to provide insights into the demographic makeup of the dataset.

#### Correlation Analysis

A correlation matrix was constructed to identify potential relationships between LinkedIn usage and various demographic and social factors. This analysis aimed to uncover any significant predictors of LinkedIn activity within the dataset.

### Logistic Regression Modeling

#### Model Training

The dataset was split into a feature set `X` (independent variables) and a target vector `y` (LinkedIn usage), followed by the division into training and testing sets. A logistic regression model was trained on the training set, with the class weight adjusted to 'balanced' to account for any imbalances in the dataset.

#### Model Evaluation

The model's performance was assessed using accuracy, confusion matrix, precision, recall, and F1 score metrics. These evaluations provided insights into the model's ability to accurately predict LinkedIn usage, including its strengths and limitations in identifying true positives and negatives.

### Predictive Analysis

The logistic regression model was applied to predict LinkedIn usage for hypothetical individuals with specified characteristics. This step illustrated the model's utility in real-world applications, demonstrating how demographic and social factors can influence the likelihood of LinkedIn activity.
Upon obtaining user inputs, the app dynamically constructs a DataFrame matching the user's demographic profile and utilizes the logistic regression model to predict the user's likelihood of being a LinkedIn user, displaying the results immediately.
### Implementation Details

The Streamlit application starts with importing the necessary libraries and preprocessing the dataset in line with the initial analysis. The app layout is designed to gather user inputs through intuitive interfaces, covering income level, education, parental status, marital status, gender, and age.

## Conclusion

The analysis of social media usage, focusing on LinkedIn, revealed several key findings. Firstly, demographic factors such as age, income, and education level significantly influence an individual's likelihood of using LinkedIn. Secondly, the logistic regression model provided a valuable tool for predicting LinkedIn activity, although its accuracy and predictive power are subject to the quality and comprehensiveness of the training data.
This project not only offers insights into factors influencing LinkedIn usage but also demonstrates the application of data science techniques in analyzing social media trends. The integration of a Streamlit application further showcases the model's real-world applicability, bridging the gap between data science and end-user interaction. Through this innovative approach, users gain personalized insights, highlighting the practical utility of machine learning models in understanding and predicting social media behavior. 


[Visit the LinkedIn Usage Prediction App](https://linkedin-predictionpy-dhqejus5znxdwsxyb2gxtd.streamlit.app/)
