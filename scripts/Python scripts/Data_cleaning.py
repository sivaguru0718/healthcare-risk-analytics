import pandas as pd

def load_data():
    """Load datasets from local path"""
    try:
        df_diabetes = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\raw_datasets\data_diabetes.csv")
        df_stroke = pd.read_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\raw_datasets\stroke_dataset.csv")
        print("Datasets Loaded Successfully!\n")
        return df_diabetes, df_stroke
    except Exception as e:
        print("Error loading datasets:", e)
        return None, None

def initial_inspection(df_diabetes, df_stroke):
    """Display dataset structure"""
    print("=== DIABETES DATA INFO ===")
    print(df_diabetes.info())

    print("\n=== STROKE DATA INFO ===")
    print(df_stroke.info())

def check_missing_values(df_diabetes, df_stroke):
    """Check missing values"""
    print("\n=== MISSING VALUES ===")
    print("Diabetes Dataset:\n", df_diabetes.isnull().sum())
    print("\nStroke Dataset:\n", df_stroke.isnull().sum())

def handle_missing_values(df_stroke):
    """Handle missing BMI values"""
    df_stroke['bmi'] = df_stroke['bmi'].fillna(df_stroke['bmi'].mean())
    print("\nMissing BMI values handled successfully.")
    return df_stroke

def remove_duplicates(df_diabetes, df_stroke):
    """Remove duplicate rows"""
    df_diabetes = df_diabetes.drop_duplicates()
    df_stroke = df_stroke.drop_duplicates()
    print("\nDuplicates removed.")
    return df_diabetes, df_stroke

def fix_data_types(df_stroke):
    """Fix incorrect data types"""
    df_stroke['age'] = df_stroke['age'].astype(int)
    print("\nData types corrected.")
    return df_stroke

def rename_columns(df_diabetes, df_stroke):
    """Standardize column names"""
    df_diabetes = df_diabetes.rename(columns={
        'Diabetes_binary': 'diabetes',
        'BMI': 'bmi',
        'Age': 'age'
    })

    df_stroke = df_stroke.rename(columns={
        'avg_glucose_level': 'glucose'
    })

    print("\nColumns renamed successfully.")
    return df_diabetes, df_stroke

def final_validation(df_diabetes, df_stroke):
    """Final dataset validation"""
    print("\n FINAL CHECK")

    print("\n Missing Values After Cleaning:")
    print(df_diabetes.isnull().sum())
    print(df_stroke.isnull().sum())

    print("\nDataset Shapes After Cleaning:")
    print("Diabetes:", df_diabetes.shape)
    print("Stroke:", df_stroke.shape)

    print("\nSample Data:")
    print(df_diabetes.head())
    print(df_stroke.head())


def save_cleaned_data(df_diabetes, df_stroke):
    """Save cleaned datasets"""
    try:
        df_diabetes.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\diabetes_cleaned.csv", index=False)
        df_stroke.to_csv(r"C:\Users\Admin\VS Projects\Healthcare_Project\Dataset\stroke_cleaned.csv", index=False)
        print("\nCleaned datasets saved successfully!")
    except Exception as e:
        print("Error saving files:", e)



def main():
    df_diabetes, df_stroke = load_data()

    if df_diabetes is None or df_stroke is None:
        print("Pipeline stopped due to loading error.")
        return

    initial_inspection(df_diabetes, df_stroke)
    check_missing_values(df_diabetes, df_stroke)

    df_stroke = handle_missing_values(df_stroke)
    df_diabetes, df_stroke = remove_duplicates(df_diabetes, df_stroke)
    df_stroke = fix_data_types(df_stroke)
    df_diabetes, df_stroke = rename_columns(df_diabetes, df_stroke)

    final_validation(df_diabetes, df_stroke)
    save_cleaned_data(df_diabetes, df_stroke)

    print("\n✅ DATA CLEANING PIPELINE COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
