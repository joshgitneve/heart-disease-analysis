# Heart Disease Analysis

## Project overview
Exploratory data analysis and machine learning model to predict 
heart disease diagnosis using the Kaggle heart disease dataset: https://www.kaggle.com/datasets/amirmahdiabbootalebi/heart-disease?select=heart.csv

## Project structure
data/raw/ - original unmodified dataset
data/processed/ - cleaned and encoded dataset
src/patient.py - Patient and PatientRecord class definitions
src/main.py - example usage of Patient classes


## Setup
1. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate
2. Install dependencies:
   pip install -r requirements.txt


## Steps
1. Data loading and exploration
2. Data cleaning — handling disguised missing values in Cholesterol and RestingBP
3. Encoding categorical variables
4. Correlation analysis
5. Object oriented data modelling (src/)
6. ML model (coming soon)

## Key findings
- ST_Slope is the strongest predictor of heart disease in this dataset
- Exercise-induced angina and Oldpeak also show strong correlation
- 172 cholesterol values were recorded as 0 and imputed with the median