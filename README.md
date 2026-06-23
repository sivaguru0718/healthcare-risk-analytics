# Healthcare Risk Analytics – End-to-End Data Project

## Project Overview
This project presents a comprehensive end-to-end healthcare analytics solution focused on identifying and analyzing risk patterns associated with Diabetes and Stroke. The analysis leverages structured datasets and applies data engineering, SQL transformation, exploratory data analysis, and business intelligence visualization to derive actionable insights.

The primary objective is to understand how demographic and health-related factors such as age, BMI, lifestyle risk, and health indicators influence disease occurrence and progression.

---

## Business Problem
Healthcare organizations require data-driven approaches to:
- Identify high-risk population segments
- Understand the impact of lifestyle and physiological factors
- Enable early intervention and preventive strategies

This project addresses the problem by analyzing:
- How diabetes and stroke risks vary across age groups
- The influence of BMI and lifestyle on disease probability
- The relationship between metabolic and cardiovascular risks

---

## Project Workflow

Raw Data → Data Cleaning → Feature Engineering → SQL Transformation → EDA → Power BI Dashboard → Insights

---

## Phase 1: Data Cleaning and Preparation

### Key Activities
- Handling missing values and inconsistencies
- Removing duplicates
- Standardizing categorical variables
- Validating dataset integrity

### Challenges Faced
- Inconsistent category labels in BMI and health indicators
- Missing or incomplete values in critical columns
- Synthetic dataset inconsistencies affecting realism

### Resolution
- Applied controlled imputation strategies
- Created standardized mappings for categorical fields
- Ensured consistency across datasets before further processing

---

## Phase 2: Feature Engineering

### Engineered Features
- Age Group segmentation
- BMI Category classification
- Lifestyle Risk scoring
- Health Score (composite metric)

### Challenges Faced
- Initial engineered features lacked logical correlation with target variables
- Encountered errors such as missing feature columns during analysis
- Unrealistic distributions affecting downstream analysis

### Resolution
- Iteratively refined datasets (v1 to v6)
- Rebuilt features based on domain logic and statistical validation
- Ensured alignment between engineered features and expected outcomes

---

## Phase 3: SQL Data Transformation

### Key Work
- Developed analytical queries for aggregation and segmentation
- Created reusable SQL views for reporting

### Key Output
- FINAL_RISK_SUMMARY view used in Power BI dashboard

### Challenges Faced
- Incorrect joins leading to duplication
- Aggregation inconsistencies
- Performance inefficiencies in query execution

### Resolution
- Optimized joins and grouping logic
- Validated query outputs against source data
- Structured SQL views for efficient BI integration

---

## Phase 4: Exploratory Data Analysis

### Analysis Performed
- Distribution analysis of age, BMI, and lifestyle risk
- Comparative analysis between diabetic and non-diabetic populations
- Stroke vs diabetes relationship exploration
- Correlation analysis between health indicators

### Challenges Faced
- Misleading visualizations due to improper feature alignment
- Incorrect category ordering affecting interpretation
- Data inconsistencies impacting chart accuracy

### Resolution
- Standardized category ordering
- Validated feature integrity before plotting
- Ensured consistent visualization logic across all charts

---

## Phase 5: Power BI Dashboard Development

### Dashboard Structure
- Executive Overview
- Diabetes Risk Analysis
- Comparative Health Insights
- Final Conclusion

### Features Implemented
- KPI cards for key metrics
- Age-wise risk trend analysis
- BMI-based segmentation
- Lifestyle impact visualization
- Interactive filtering capabilities

### Challenges Faced
- KPI values initially showing incorrect results due to DAX issues
- Difficulty in establishing proper data relationships
- Layout and storytelling inconsistencies

### Resolution
- Corrected DAX measures and relationships
- Structured dashboard flow for better storytelling
- Applied consistent design and visual hierarchy

---

## Key Insights

- Diabetes risk increases significantly with age
- Obesity and overweight categories show the highest risk levels
- Lifestyle factors strongly influence disease probability
- Stroke risk follows a similar pattern but at a lower magnitude
- There is a progression from metabolic disorders to cardiovascular risks

---

## Tools and Technologies

- Python (Pandas, Seaborn, Matplotlib)
- SQL (Data transformation and analytical views)
- Power BI (Dashboard and visualization)
- Excel (Intermediate validation)

---

## Project Structure

Healthcare_Risk_Analytics/
│
├── Dashboard/
│   ├── Healthcare_Dashboard.pbix
│   └── PNG Images of Dashboard/
│       ├── Executive Overview.png
│       ├── Diabetes Risk Analysis by BMI & Lifestyle.png
│       ├── Comparative Health Risk Insights.png
│       └── Conclusion.png
│
├── data/
│   ├── raw_datasets/
│   ├── cleaned_datasets/
│   ├── featured_datasets_1/
│   ├── featured_datasets_2/
│   └── SQL_derived_datasets_and_views/
│       ├── Analytical_Datasets/
│       └── SQL_Views/
│
├── Images/
│   └── EDA_graphs/
│       ├── Age Group vs Diabetes (Count Comparison).png
│       ├── BMI Category vs Diabetes (Count Analysis).png
│       ├── BMI Category vs Diabetes (Proportion Analysis).png
│       ├── Lifestyle Risk vs Diabetes (Distribution Analysis).png
│       ├── Health Score vs Diabetes (Distribution Analysis).png
│       ├── Age vs Stroke (Distribution Analysis).png
│       ├── Glucose Level vs Stroke (Distribution Analysis).png
│       ├── Correlation Heatmap of Health Risk Factors.png
│       ├── BMI Category vs Stroke (Proportion Analysis).png
│       ├── Diabetes Age Distribution.png
│       ├── Stroke Age Distribution.png
│       ├── Diabetes Rate by Age Group (%).png
│       ├── Stroke Rate by BMI Category (%).png
│       ├── Lifestyle Risk Distribution.png
│       └── Age Group Comparative Risk Analysis.png
│
├── scripts/
│   ├── Python_scripts/
│   │   ├── Data_cleaning.py
│   │   ├── EDA.py
│   │   ├── Feature_engineering_1.0.py
│   │   ├── Feature_engineering_1.1.py
│   │   ├── Featured_engineering_2.0.py
│   │   └── Featured_engineering_2.1.py
│   │
│   └── SQL_Queries/
│       ├── TABLE_CREATION_AND_LOADING_DATA.sql
│       ├── VIEWS_AND_JOINS.sql
│       ├── ANALYTICAL_QUERIES.sql
│       ├── STORED_PROCEDURES_AND_INDEXES.sql
│       └── FIXES_IN_PROJECT.sql
│
└── README.md

## Conclusion

This project demonstrates a complete data analytics workflow from raw data processing to business intelligence reporting. It highlights the importance of feature engineering, data validation, and structured visualization in deriving meaningful insights from healthcare data.

---
