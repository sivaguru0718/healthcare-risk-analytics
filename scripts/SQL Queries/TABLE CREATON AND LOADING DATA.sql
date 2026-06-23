CREATE DATABASE healthcare_project;
USE healthcare_project;

CREATE TABLE diabetes_data (
    diabetes INT,
    bmi FLOAT,
    age INT,
    HighBP INT,
    HighChol INT,
    Smoker INT,
    PhysActivity INT,
    Fruits INT,
    Veggies INT,
    HvyAlcoholConsump INT,
    GenHlth INT,
    MentHlth INT,
    PhysHlth INT,
    age_group VARCHAR(20),
    bmi_category VARCHAR(20),
    lifestyle_risk FLOAT,
    health_score FLOAT
);


CREATE TABLE stroke_data (
    gender VARCHAR(10),
    age FLOAT,
    hypertension INT,
    heart_disease INT,
    ever_married VARCHAR(10),
    work_type VARCHAR(20),
    Residence_type VARCHAR(20),
    glucose FLOAT,
    bmi FLOAT,
    smoking_status VARCHAR(20),
    stroke INT,
    age_group VARCHAR(20),
    bmi_category VARCHAR(20)
);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/diabetes_featured.csv'
INTO TABLE diabetes_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/stroke_featured.csv'
INTO TABLE stroke_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;