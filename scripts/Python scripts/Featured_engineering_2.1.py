import pandas as pd
import numpy as np
import os


file_path = r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\cleaned_datasets\stroke_cleaned.csv"
df = pd.read_csv(file_path)


df.columns = df.columns.str.strip().str.lower()


df = df.drop_duplicates()


def safe_col(df, col, default=0):
    return df[col] if col in df.columns else default


df["age"] = pd.to_numeric(safe_col(df, "age"), errors="coerce")
df["bmi"] = pd.to_numeric(safe_col(df, "bmi"), errors="coerce")
df["glucose"] = pd.to_numeric(safe_col(df, "glucose"), errors="coerce")


for col in df.columns:
    if df[col].dropna().isin([0,1]).all():
        df[col] = df[col].astype(int)


df = df[(df["age"] > 0) & (df["age"] <= 100)]

if "bmi" in df.columns:
    df = df[(df["bmi"] >= 12) & (df["bmi"] <= 60)]

if "glucose" in df.columns:
    df = df[(df["glucose"] >= 50) & (df["glucose"] <= 300)]


df["age_group"] = pd.cut(
    df["age"],
    bins=[0,18,30,45,60,75,100],
    labels=["0-18","19-30","31-45","46-60","61-75","75+"],
    include_lowest=True
)


if "bmi" in df.columns:
    df["bmi_category"] = pd.cut(
        df["bmi"],
        bins=[0,18.5,25,30,100],
        labels=["Underweight","Normal","Overweight","Obese"]
    )



if "smoking_status" in df.columns:
    df["smoking_status"] = df["smoking_status"].astype(str).str.strip().str.lower()

if "gender" in df.columns:
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()



if "smoking_status" in df.columns:
    df["smoking_status"] = df["smoking_status"].astype(str).str.strip().str.lower()

    df["Smoker"] = df["smoking_status"].map({
        "never smoked": 0,
        "formerly smoked": 1,
        "smokes": 1,
        "unknown": 0
    }).fillna(0)
else:
    df["Smoker"] = 0



df["lifestyle_risk"] = (
    df["Smoker"] +
    (1 - df.get("PhysActivity", 1)) +
    df.get("HvyAlcoholConsump", 0)
)



df["lifestyle_risk"] = (
    df["lifestyle_risk"] +
    (df["bmi"] / 30) +
    (df["age"] / 100)
)


df["lifestyle_risk"] = (
    df["lifestyle_risk"] - df["lifestyle_risk"].min()
) / (df["lifestyle_risk"].max() - df["lifestyle_risk"].min()) * 3

df["lifestyle_risk"] = df["lifestyle_risk"].round(0)


health_components = []

if "hypertension" in df.columns:
    health_components.append((1 - df["hypertension"]) * 20)

if "heart_disease" in df.columns:
    health_components.append((1 - df["heart_disease"]) * 20)

if "bmi" in df.columns:
    health_components.append((1 - (df["bmi"] / 60)) * 20)

if "glucose" in df.columns:
    health_components.append((1 - (df["glucose"] / 300)) * 20)

if health_components:
    df["health_index"] = np.mean(health_components, axis=0) * 5
else:
    df["health_index"] = 50



df["health_index_bin"] = pd.cut(
    df["health_index"],
    bins=[0,40,60,75,100],
    labels=["Poor","Fair","Good","Excellent"]
)



if "glucose" in df.columns:
    df["glucose_bin"] = pd.cut(
        df["glucose"],
        bins=[0,100,140,200,300],
        labels=["Normal","Prediabetes","Diabetes","High"]
    )


if "stroke" in df.columns:
    df["stroke_rate"] = df["stroke"]



df.drop(columns=["stroke"], inplace=True, errors="ignore")


for col in df.columns:
    if df[col].nunique() <= 1:
        df.drop(columns=[col], inplace=True)


print("\n FINAL DATA SUMMARY")
print(df.describe())

print("\n UNIQUE VALUES")
print(df.nunique())


output_path = r"C:\Users\Admin\VS Projects\Healthcare_Project"

if not os.path.exists(output_path):
    os.makedirs(output_path)

final_file = os.path.join(output_path, "stroke_final_v6.csv")


