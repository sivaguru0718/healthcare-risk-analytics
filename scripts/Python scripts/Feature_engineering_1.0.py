
import pandas as pd



df_diabetes = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\diabetes_cleaned.csv")
df_stroke = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\stroke_cleaned.csv")



df_diabetes['age_group'] = pd.cut(
    df_diabetes['age'],
    bins=[0, 30, 50, 70, 100],
    labels=['Young', 'Mid-Age', 'Senior', 'Elderly']
)



def bmi_category(x):
    if x < 18.5:
        return 'Underweight'
    elif x < 25:
        return 'Normal'
    elif x < 30:
        return 'Overweight'
    else:
        return 'Obese'

df_diabetes['bmi_category'] = df_diabetes['bmi'].apply(bmi_category)
df_stroke['bmi_category'] = df_stroke['bmi'].apply(bmi_category)



df_diabetes['lifestyle_risk'] = (
    df_diabetes['bmi'] * 0.3 +
    df_diabetes['Smoker'] * 15 +
    df_diabetes['PhysActivity'] * (-10) +
    df_diabetes['HvyAlcoholConsump'] * 10
)



df_diabetes['health_score'] = (
    df_diabetes['HighBP'] +
    df_diabetes['HighChol'] +
    df_diabetes['HeartDiseaseorAttack'] +
    df_diabetes['Stroke']
)



df_diabetes.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\diabetes_featured.csv", index=False)
df_stroke.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\stroke_featured.csv", index=False)

print("Feature Engineering Completed Successfully!")
