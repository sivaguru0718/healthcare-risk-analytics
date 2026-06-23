**Healthcare Risk Analytics Dashboard**

**Project Overview**

This project presents an end-to-end healthcare analytics solution focused on identifying and analyzing risk patterns associated with Diabetes and Stroke. By leveraging feature engineering, exploratory data analysis (EDA), SQL-based data transformation, and Power BI visualization, the project delivers actionable insights for early risk detection and preventive healthcare strategies.

---

**Business Problem**

Chronic diseases like diabetes and stroke pose significant challenges to healthcare systems. The key objective of this project is:

«To identify high-risk populations based on age, BMI, and lifestyle factors, and understand the progression from metabolic disorders (diabetes) to cardiovascular conditions (stroke).»

---

**Methodology**

1. Data Collection & Preparation

  - Utilized structured healthcare datasets:
  - Diabetes Dataset
  - Stroke Dataset
  - Cleaned and preprocessed missing and inconsistent values
---

2. Feature Engineering

Derived meaningful analytical features:

  - Age Groups (18–24 to 80+)
  - BMI Categories (Underweight, Normal, Overweight, Obese)
  - Lifestyle Risk Index
  - Health Score

👉 This step enhanced interpretability and enabled meaningful segmentation.
---

3. SQL-Based Data Transformation

  - Implemented SQL queries for structured data handling
  - Created analytical views to support dashboard insights

⭐ Key SQL View:

"FINAL_RISK_SUMMARY"

  - Aggregates:
  - Diabetes Rate
  - Stroke Rate
  - Risk Gap
  - High-Risk Population %
  - Used directly in Power BI for KPI generation
---

**4. Exploratory Data Analysis (EDA)**

Performed multi-dimensional analysis using Python:

  - Age vs Disease Trends
  - BMI vs Risk Distribution
  - Lifestyle Impact Analysis
  - Glucose vs Stroke Relationship
  - Correlation Heatmap
---

**5. Dashboard Development (Power BI)**

Developed an interactive dashboard with the following pages:

Executive Overview

- KPI Cards:
  - Total Population
  - Diabetes Rate %
  - Stroke Rate %
  - Risk Gap
  - High Risk %

Diabetes Risk Analysis

- Age vs BMI progression
- Lifestyle impact on diabetes
- High-risk segmentation

Comparative Health Insights

- Diabetes vs Stroke comparison
- Distribution across BMI categories
- Health score relationship

Conclusion
  
  - Key risk segments:
  - Obese population
  - Age group 70–74
  - Final actionable insights
---

Key Insights

- Diabetes risk (~15%) is significantly higher than stroke (~5%)
- Risk increases sharply after age 50
- Obesity is the strongest contributing factor
- Lifestyle risk strongly correlates with diabetes occurrence
- Stroke risk follows a similar trend but appears as a secondary progression
---

Tech Stack

- Python: Pandas, NumPy, Matplotlib, Seaborn
- SQL: Data transformation, analytical views
- Power BI: Dashboarding & visualization
- Data Analysis: Feature Engineering & EDA
---

Project Structure

Healthcare-Risk-Analytics/
│
├── data/
├── scripts/
├── dashboard/
├── images/
├── README.md
├── requirements.txt
---

**Dashboard Preview**

"Executive Overview" (images/page1.png)
"Diabetes Analysis" (images/page2.png)
"Comparative Insights" (images/page3.png)
"Final Summary" (images/page4.png)
---

**Outcome :**

This project successfully delivers a data-driven decision support system that:

- Identifies high-risk populations
- Highlights key contributing factors
- Demonstrates disease progression patterns
- Supports early intervention strategies
---

**Limitations :**

- Dataset is synthetic and may not fully represent real-world scenarios
- Analysis is descriptive (EDA-based), not predictive
- No statistical hypothesis testing applied
---

**Future Enhancements :**

  - Build predictive models (Logistic Regression / ML models)
  - Integrate real-world healthcare datasets
  - Deploy dashboard to Power BI Service
  - Add real-time data pipeline
---

**Contact**

If you found this project insightful, feel free to connect or reach out!
 And if you like this project, consider giving it a star!
