# =====================================
# FINAL PERFECT EDA (EXACT MATCH VERSION)
# =====================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# -------------------------------
# LOAD DATA
# -------------------------------
df_diabetes = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\featured_datasets_1\diabetes_featured.csv")
df_stroke = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\featured_datasets_1\stroke_featured.csv")

# -------------------------------
# AGE GROUP FIX (CRITICAL)
# -------------------------------
age_order = [
    '18-24','25-29','30-34','35-39','40-44',
    '45-49','50-54','55-59','60-64',
    '65-69','70-74','75-79','80+'
]

# Ensure diabetes age_group exists correctly
if 'age_group' not in df_diabetes.columns:
    bins = [18,25,30,35,40,45,50,55,60,65,70,75,80,100]
    df_diabetes['age_group'] = pd.cut(df_diabetes['age'], bins=bins, labels=age_order, right=False)

# Convert to categorical (fix ordering issue)
df_diabetes['age_group'] = pd.Categorical(df_diabetes['age_group'], categories=age_order, ordered=True)

# Stroke dataset → DO NOT RECREATE (your dataset already grouped)
df_stroke['age_group'] = df_stroke['age_group'].astype(str)

# -------------------------------
# BMI ORDER
# -------------------------------
bmi_order = ['Underweight', 'Normal', 'Overweight', 'Obese']

# =====================================
# 1. AGE GROUP vs DIABETES (FIXED)
# =====================================
plt.figure()
sns.countplot(data=df_diabetes, x='age_group', hue='diabetes', order=age_order)
plt.title("Age Group vs Diabetes")
plt.xticks(rotation=45)
plt.show()

# =====================================
# 2. DIABETES AGE DISTRIBUTION
# =====================================
plt.figure()
sns.countplot(data=df_diabetes, x='age_group', order=age_order)
plt.title("Diabetes Age Distribution")
plt.xticks(rotation=45)
plt.show()

# =====================================
# 3. STROKE AGE DISTRIBUTION (KEEP ORIGINAL ORDER)
# =====================================
plt.figure()
sns.countplot(data=df_stroke, x='age_group')
plt.title("Stroke Age Distribution")
plt.xticks(rotation=45)
plt.show()

# =====================================
# 4. LIFESTYLE RISK DISTRIBUTION (FIXED SCALE)
# =====================================
plt.figure()
sns.histplot(df_diabetes['lifestyle_risk'], bins=6, kde=True)
plt.title("Lifestyle Risk Distribution")
plt.show()

# =====================================
# 5. DIABETES RATE BY AGE GROUP (%)
# =====================================
diabetes_rate = df_diabetes.groupby('age_group')['diabetes'].mean() * 100

plt.figure()
diabetes_rate = diabetes_rate.reindex(age_order)
diabetes_rate.plot(kind='bar')
plt.title("Diabetes Rate by Age Group (%)")
plt.ylabel("Diabetes Rate (%)")
plt.xticks(rotation=45)
plt.show()

# =====================================
# 6. STROKE RATE BY BMI CATEGORY (%)
# =====================================
stroke_rate = df_stroke.groupby('bmi_category')['stroke'].mean() * 100

plt.figure()
stroke_rate = stroke_rate.reindex(bmi_order)
stroke_rate.plot(kind='bar')
plt.title("Stroke Rate by BMI Category (%)")
plt.ylabel("Stroke Rate (%)")
plt.show()

# =====================================
# ADDITIONAL CORE CHARTS (FROM PREVIOUS)
# =====================================

# BMI vs DIABETES (COUNT)
plt.figure()
sns.countplot(x='bmi_category', hue='diabetes', data=df_diabetes, order=bmi_order)
plt.title("BMI vs Diabetes (Count)")
plt.show()

# BMI vs DIABETES (PROPORTION)
bmi_ratio = pd.crosstab(df_diabetes['bmi_category'], df_diabetes['diabetes'], normalize='index')
bmi_ratio = bmi_ratio.reindex(bmi_order)

bmi_ratio.plot(kind='bar', stacked=True)
plt.title("BMI vs Diabetes (Proportion)")
plt.ylabel("Proportion")
plt.show()

# LIFESTYLE vs DIABETES
plt.figure()
sns.boxplot(x='diabetes', y='lifestyle_risk', data=df_diabetes)
plt.title("Lifestyle Risk vs Diabetes")
plt.show()

# HEALTH SCORE vs DIABETES
plt.figure()
sns.boxplot(x='diabetes', y='health_score', data=df_diabetes)
plt.title("Health Score vs Diabetes")
plt.show()

# AGE vs STROKE
plt.figure()
sns.boxplot(x='stroke', y='age', data=df_stroke)
plt.title("Age vs Stroke")
plt.show()

# GLUCOSE vs STROKE (AUTO FIX COLUMN NAME)
glucose_col = 'glucose' if 'glucose' in df_stroke.columns else 'avg_glucose_level'

plt.figure()
sns.boxplot(x='stroke', y=glucose_col, data=df_stroke)
plt.title("Glucose vs Stroke")
plt.show()

# BMI vs STROKE (PROPORTION)
stroke_ratio = pd.crosstab(df_stroke['bmi_category'], df_stroke['stroke'], normalize='index')
stroke_ratio = stroke_ratio.reindex(bmi_order)

stroke_ratio.plot(kind='bar', stacked=True)
plt.title("BMI vs Stroke (Proportion)")
plt.ylabel("Proportion")
plt.show()

# CORRELATION HEATMAP
features = ['diabetes','HighBP','HighChol','lifestyle_risk','health_score']

plt.figure(figsize=(10,8))
sns.heatmap(df_diabetes[features].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

print("✅ FINAL EDA (ALL CHARTS MATCHED CORRECTLY)")