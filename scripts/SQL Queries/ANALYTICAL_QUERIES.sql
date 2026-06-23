SELECT 
    age_group,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate
FROM diabetes_data
GROUP BY age_group
ORDER BY diabetes_rate DESC;

SELECT 
    age_group,
    ROUND(AVG(stroke)*100,2) AS stroke_rate
FROM stroke_data
GROUP BY age_group
ORDER BY stroke_rate DESC;

SELECT 
    bmi_category,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate,
    COUNT(*) AS population
FROM diabetes_data
GROUP BY bmi_category
ORDER BY diabetes_rate DESC;

SELECT 
    lifestyle_risk,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate
FROM diabetes_data
GROUP BY lifestyle_risk
ORDER BY lifestyle_risk;

SELECT 
    health_score,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate
FROM diabetes_data
GROUP BY health_score
ORDER BY health_score;

SELECT 
    ROUND(SUM(CASE WHEN lifestyle_risk >= 3 THEN 1 ELSE 0 END)*100.0/COUNT(*),2) 
    AS high_risk_percentage
FROM diabetes_data;

SELECT 
    ROUND(AVG(glucose),2) AS avg_glucose,
    stroke
FROM stroke_data
GROUP BY stroke;

SELECT 
    HighBP,
    HighChol,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate
FROM diabetes_data
GROUP BY HighBP, HighChol;

SELECT 
    bmi_category,
    COUNT(*) AS population
FROM diabetes_data
GROUP BY bmi_category;

SELECT 
    age_group,
    ROUND(AVG(lifestyle_risk),2) AS avg_lifestyle_risk,
    ROUND(AVG(health_score),2) AS avg_health_score
FROM diabetes_data
GROUP BY age_group;