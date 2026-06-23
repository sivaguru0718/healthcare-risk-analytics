SELECT 
    d.age_group,
    ROUND(AVG(d.diabetes)*100,2) AS diabetes_rate,
    ROUND(AVG(s.stroke)*100,2) AS stroke_rate
FROM 
    (SELECT age_group, diabetes FROM diabetes_data) d
JOIN 
    (SELECT age_group, stroke FROM stroke_data) s
ON d.age_group = s.age_group
GROUP BY d.age_group;

CREATE OR REPLACE VIEW diabetes_summary AS
SELECT 
    age_group,
    bmi_category,
    ROUND(AVG(diabetes)*100,2) AS diabetes_rate,
    ROUND(AVG(lifestyle_risk),2) AS avg_lifestyle_risk,
    ROUND(AVG(health_score),2) AS avg_health_score,
    COUNT(*) AS population
FROM diabetes_data
GROUP BY age_group, bmi_category;

CREATE OR REPLACE VIEW stroke_summary AS
SELECT 
    age_group,
    bmi_category,
    ROUND(AVG(stroke)*100,2) AS stroke_rate,
    COUNT(*) AS population
FROM stroke_data
GROUP BY age_group, bmi_category;

CREATE OR REPLACE VIEW final_risk_summary AS
SELECT 
    d.age_group,
    d.bmi_category,
    d.diabetes_rate,
    s.stroke_rate,
    d.avg_lifestyle_risk,
    d.avg_health_score,
    d.population
FROM diabetes_summary d
LEFT JOIN stroke_summary s
ON d.age_group = s.age_group 
AND d.bmi_category = s.bmi_category;
