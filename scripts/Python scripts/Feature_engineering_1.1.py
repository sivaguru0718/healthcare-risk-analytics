
import pandas as pd
import numpy as np

df_diabetes = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\data_diabetes.csv")
df_stroke = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\stroke_dataset.csv")

print("Datasets Loaded Successfully\n")

df_stroke['bmi'] = df_stroke['bmi'].fillna(df_stroke['bmi'].mean())

df_diabetes.drop_duplicates(inplace=True)
df_stroke.drop_duplicates(inplace=True)

df_stroke['age'] = df_stroke['age'].astype(int)

df_diabetes.rename(columns={
    'Diabetes_binary': 'diabetes',
    'BMI': 'bmi',
    'Age': 'age'
}, inplace=True)

df_stroke.rename(columns={
    'avg_glucose_level': 'glucose'
}, inplace=True)

print("Cleaning Completed \n")

age_mapping = {
    1: '18-24',
    2: '25-29',
    3: '30-34',
    4: '35-39',
    5: '40-44',
    6: '45-49',
    7: '50-54',
    8: '55-59',
    9: '60-64',
    10: '65-69',
    11: '70-74',
    12: '75-79',
    13: '80+'
}

df_diabetes['age_group'] = df_diabetes['age'].map(age_mapping)

# Stroke dataset uses real age
bins = [0, 18, 25, 35, 45, 55, 65, 75, 85, 120]
labels = ['0-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+']

df_stroke['age_group'] = pd.cut(df_stroke['age'], bins=bins, labels=labels, right=False)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

df_diabetes['bmi_category'] = df_diabetes['bmi'].apply(bmi_category)
df_stroke['bmi_category'] = df_stroke['bmi'].apply(bmi_category)

df_diabetes['lifestyle_risk'] = (
    df_diabetes['Smoker'] +
    df_diabetes['HvyAlcoholConsump'] +
    (1 - df_diabetes['PhysActivity']) +
    (1 - df_diabetes['Fruits']) +
    (1 - df_diabetes['Veggies'])
)

df_diabetes['health_score'] = (
    df_diabetes['GenHlth'] +
    df_diabetes['MentHlth'] +
    df_diabetes['PhysHlth']
) / 3

print("VALIDATION CHECKS \n")

print("Diabetes Age Group Distribution:")
print(df_diabetes['age_group'].value_counts(), "\n")

print("Stroke Age Group Distribution:")
print(df_stroke['age_group'].value_counts(), "\n")

print("Missing Values:")
print(df_diabetes.isnull().sum())
print(df_stroke.isnull().sum(), "\n")

df_diabetes_final = df_diabetes[[
    'diabetes', 'bmi', 'age', 'HighBP', 'HighChol',
    'Smoker', 'PhysActivity', 'Fruits', 'Veggies',
    'HvyAlcoholConsump', 'GenHlth', 'MentHlth', 'PhysHlth',
    'age_group', 'bmi_category', 'lifestyle_risk', 'health_score'
]]

df_stroke_final = df_stroke[[
    'gender', 'age', 'hypertension', 'heart_disease',
    'ever_married', 'work_type', 'Residence_type',
    'glucose', 'bmi', 'smoking_status', 'stroke',
    'age_group', 'bmi_category'
]]

df_diabetes_final.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\diabetes_featured.csv", index=False)
df_stroke_final.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\stroke_featured.csv", index=False)

print("FINAL FEATURED DATASETS SAVED SUCCESSFULLY")

print(df_stroke['age_group'].isnull().sum())

df_stroke['age_group'] = df_stroke['age_group'].fillna('Unknown')