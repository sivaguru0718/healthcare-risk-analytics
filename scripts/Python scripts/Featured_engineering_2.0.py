import pandas as pd
import numpy as np
import os

# =========================
# LOAD DATA
# =========================
file_path = r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\cleaned_datasets\diabetes_cleaned.csv"
df = pd.read_csv(file_path)

# =========================
# STANDARDIZE COLUMN NAMES
# =========================
df.columns = df.columns.str.strip().str.lower()

# =========================
# REMOVE DUPLICATES
# =========================
df = df.drop_duplicates()

# =========================
# SAFE COLUMN ACCESS FUNCTION
# =========================
def safe_col(df, col, default=0):
    return df[col] if col in df.columns else default

# =========================
# FIX DATA TYPES
# =========================
for col in df.columns:
    if df[col].dropna().isin([0,1]).all():
        df[col] = df[col].astype(int)

df["age"] = pd.to_numeric(safe_col(df, "age"), errors="coerce")
df["bmi"] = pd.to_numeric(safe_col(df, "bmi"), errors="coerce")

# =========================
# REMOVE INVALID VALUES
# =========================
df = df[(df["age"] > 0) & (df["age"] <= 100)]
df = df[(df["bmi"] >= 12) & (df["bmi"] <= 60)]

# =========================
# AGE GROUP
# =========================
df["age_group"] = pd.cut(
    df["age"],
    bins=[18,25,35,45,55,65,75,100],
    labels=["18-24","25-34","35-44","45-54","55-64","65-74","75+"],
    include_lowest=True
)

# =========================
# BMI CATEGORY
# =========================
df["bmi_category"] = pd.cut(
    df["bmi"],
    bins=[0,18.5,25,30,100],
    labels=["Underweight","Normal","Overweight","Obese"]
)

# =========================
# LIFESTYLE RISK (SAFE)
# =========================
# =========================
# FIX SMOKING COLUMN (IMPORTANT)
# =========================
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

# =========================
# LIFESTYLE RISK (FIXED)
# =========================
df["lifestyle_risk"] = (
    df["Smoker"] +
    (1 - df.get("PhysActivity", 1)) +
    df.get("HvyAlcoholConsump", 0)
)

# =========================
# MAKE IT MORE REALISTIC
# =========================
df["lifestyle_risk"] = (
    df["lifestyle_risk"] +
    (df["bmi"] / 30) +
    (df["age"] / 100)
)

# Normalize (0–3 range)
df["lifestyle_risk"] = (
    df["lifestyle_risk"] - df["lifestyle_risk"].min()
) / (df["lifestyle_risk"].max() - df["lifestyle_risk"].min()) * 3

df["lifestyle_risk"] = df["lifestyle_risk"].round(0)
# =========================
# HEALTH INDEX (CONTROLLED VERSION)
# =========================
# Normalize instead of random-like values

health_components = []

if "genhlth" in df.columns:
    health_components.append((6 - df["genhlth"]) * 10)

if "menthlth" in df.columns:
    health_components.append((30 - df["menthlth"]))

if "physhlth" in df.columns:
    health_components.append((30 - df["physhlth"]))

if health_components:
    df["health_index"] = np.mean(health_components, axis=0)
else:
    df["health_index"] = 50  # fallback safe value

# =========================
# HEALTH INDEX BIN (IMPORTANT FIX)
# =========================
df["health_index_bin"] = pd.cut(
    df["health_index"],
    bins=[0,40,60,75,100],
    labels=["Poor","Fair","Good","Excellent"]
)

# =========================
# GLUCOSE HANDLING (SAFE)
# =========================
if "glucose" in df.columns:
    df["glucose"] = pd.to_numeric(df["glucose"], errors="coerce")

    df["glucose_bin"] = pd.cut(
        df["glucose"],
        bins=[0,100,140,200,300],
        labels=["Normal","Prediabetes","Diabetes","High"]
    )

# =========================
# TARGET VARIABLE
# =========================
if "diabetes_binary" in df.columns:
    df["diabetes"] = df["diabetes_binary"]

# =========================
# REMOVE REDUNDANT COLUMNS
# =========================
df.drop(columns=["diabetes_binary"], inplace=True, errors="ignore")

# =========================
# REMOVE LOW VARIANCE COLUMNS
# =========================
for col in df.columns:
    if df[col].nunique() <= 1:
        df.drop(columns=[col], inplace=True)

# =========================
# FINAL CLEAN CHECK
# =========================
print("\n✅ FINAL DATA SUMMARY")
print(df.describe())
print("\n✅ UNIQUE VALUES")
print(df.nunique())

# =========================
# SAVE FILE
# =========================
output_path = r"C:\Users\Admin\VS Projects\Healthcare_Project"

if not os.path.exists(output_path):
    os.makedirs(output_path)

final_file = os.path.join(output_path, "diabetes_final_v6.csv")

try:
    df.to_csv(final_file, index=False)
    print("\n✅ File saved successfully at:", final_file)
except Exception as e:
    print("\n❌ Save error:", e)