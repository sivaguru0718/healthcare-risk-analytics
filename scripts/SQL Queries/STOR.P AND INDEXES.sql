DELIMITER $$

CREATE PROCEDURE get_high_risk_groups()
BEGIN
    SELECT *
    FROM final_risk_summary
    WHERE avg_lifestyle_risk >= 2.5
    ORDER BY diabetes_rate DESC;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE age_risk_analysis()
BEGIN
    SELECT 
        age_group,
        AVG(diabetes_rate) AS diabetes_rate,
        AVG(stroke_rate) AS stroke_rate
    FROM final_risk_summary
    GROUP BY age_group;
END $$

DELIMITER ;

CREATE INDEX idx_diabetes_age ON diabetes_data(age_group);
CREATE INDEX idx_diabetes_bmi ON diabetes_data(bmi_category);

CREATE INDEX idx_stroke_age ON stroke_data(age_group);
CREATE INDEX idx_stroke_bmi ON stroke_data(bmi_category);