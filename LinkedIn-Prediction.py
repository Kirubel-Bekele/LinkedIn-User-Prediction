import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the dataset
S = pd.read_csv("social_media_usage.csv")
# Preprocess the data
S['sm_li'] = S['web1h'].apply(lambda x: 1 if x == 1 else 0)
S['income'] = S['income'].apply(lambda x: np.nan if x > 9 else x)
S['education'] = S['educ2'].apply(lambda x: np.nan if x > 8 else x)
S['par'] = S['par'].apply(lambda x: 1 if x == 1 else 0)
S['marital'] = S['marital'].apply(lambda x: 1 if x == 1 else 0)
S['gender'] = S['gender'].apply(lambda x: 1 if x == 2 else 0)
S['Age'] = np.where(S['age'] > 98, np.nan, S['age'])
# Selecting relevant columns and dropping missing values
ss = S[['sm_li', 'income', 'education', 'par', 'marital', 'gender', 'age']].dropna()

# Creating the target vector (y) and feature set (X)
y = ss['sm_li']
X = ss.drop('sm_li', axis=1)

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=987)

# Initializing and fitting the logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Streamlit app layout
st.title("LinkedIn Usage Prediction")




# User input options based on the data dictionary
income_options = {
    1: "Less than $10,000",
    2: "10 to under $20,000",
    3: "20 to under $30,000",
    4: "30 to under $40,000",
    5: "40 to under $50,000",
    6: "50 to under $75,000",
    7: "75 to under $100,000",
    8: "100 to under $150,000",
    9: "$150,000 or more"
}

education_options = {
    1: "Less than high school (Grades 1-8 or no formal schooling)",
    2: "High school incomplete (Grades 9-11 or Grade 12 with NO diploma)",
    3: "High school graduate (Grade 12 with diploma or GED certificate)",
    4: "Some college, no degree (includes some community college)",
    5: "Two-year associate degree from a college or university",
    6: "Four-year college or university degree/Bachelor’s degree (e.g., BS, BA, AB)",
    7: "Some postgraduate or professional schooling, no postgraduate degree",
    8: "Postgraduate or professional degree (e.g., MA, MS, PhD, MD, JD)"
}

gender_options = {
    1: "Male",
    2: "Female",
    3: "Other"
}

# User inputs
income = st.select_slider("Select Your Income Level", options=list(income_options.keys()), format_func=lambda x: income_options[x])
education = st.select_slider("Select Your Education Level", options=list(education_options.keys()), format_func=lambda x: education_options[x])
parent = st.radio("Are you a parent of a child under 18 living in your home?", ('Yes', 'No'))
marital_status = st.radio("Marital Status", ('Married', 'Not Married'))
gender = st.selectbox("Select Your Gender", options=list(gender_options.keys()), format_func=lambda x: gender_options[x])
age = st.slider("Enter Your Age", 18, 97, 30)

# Convert inputs to the format expected by the model
input_data = {
    'income': [income],
    'education': [education],
    'par': [1 if parent == 'Yes' else 0],
    'marital': [1 if marital_status == 'Married' else 0],  
    'gender': [gender],
    'age': [age]
}
input_df = pd.DataFrame.from_dict(input_data)

# Predicting LinkedIn usage
if st.button('Predict'):
    prediction = lr.predict(input_df)
    result = "Prediction: LinkedIn User" if prediction[0] == 1 else "Not a LinkedIn User"
    st.write(result)
