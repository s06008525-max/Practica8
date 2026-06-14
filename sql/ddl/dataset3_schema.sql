-- DDL Dataset 3: Hospitales normalizado a 3FN

CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age VARCHAR(20),
    bmi VARCHAR(50),
    ethnicity VARCHAR(100),
    gender VARCHAR(20),
    height VARCHAR(50),
    weight VARCHAR(50)
);

CREATE TABLE icus (
    icu_id INT PRIMARY KEY,
    hospital_id INT,
    icu_type VARCHAR(100)
);

CREATE TABLE encounters (
    encounter_id INT PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    icu_id INT REFERENCES icus(icu_id),
    elective_surgery VARCHAR(20),
    icu_admit_source VARCHAR(100),
    icu_stay_type VARCHAR(100),
    apache_2_diagnosis VARCHAR(100)
);
