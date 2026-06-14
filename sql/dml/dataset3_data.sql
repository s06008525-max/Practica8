
- INSERTS tabla patients
INSERT INTO patients (patient_id, age, bmi, ethnicity, gender, height, weight) VALUES ('25312', '68.0', '22.73', 'Caucasian', 'M', '180.3', '73.9');
INSERT INTO patients (patient_id, age, bmi, ethnicity, gender, height, weight) VALUES ('59342', '77.0', '27.42', 'Caucasian', 'F', '160.0', '70.2');
INSERT INTO patients (patient_id, age, bmi, ethnicity, gender, height, weight) VALUES ('50777', '25.0', '31.95', 'Caucasian', 'F', '172.7', '95.3');
INSERT INTO patients (patient_id, age, bmi, ethnicity, gender, height, weight) VALUES ('46918', '81.0', '22.64', 'Caucasian', 'F', '165.1', '61.7');
INSERT INTO patients (patient_id, age, bmi, ethnicity, gender, height, weight) VALUES ('34377', '19.0', 'Unknown', 'Caucasian', 'M', '188.0', 'Unknown');

- INSERTS tabla icus
INSERT INTO icus (icu_id, hospital_id, icu_type) VALUES ('92', '118', 'CTICU');
INSERT INTO icus (icu_id, hospital_id, icu_type) VALUES ('90', '81', 'Med-Surg ICU');
INSERT INTO icus (icu_id, hospital_id, icu_type) VALUES ('93', '118', 'Med-Surg ICU');
INSERT INTO icus (icu_id, hospital_id, icu_type) VALUES ('91', '33', 'Med-Surg ICU');
INSERT INTO icus (icu_id, hospital_id, icu_type) VALUES ('95', '83', 'Med-Surg ICU');

- INSERTS tabla encounters
INSERT INTO encounters (encounter_id, patient_id, icu_id, elective_surgery, icu_admit_source, icu_stay_type, apache_2_diagnosis) VALUES ('66154', '25312', '92', '0', 'Floor', 'admit', '113.0');
INSERT INTO encounters (encounter_id, patient_id, icu_id, elective_surgery, icu_admit_source, icu_stay_type, apache_2_diagnosis) VALUES ('114252', '59342', '90', '0', 'Floor', 'admit', '108.0');
INSERT INTO encounters (encounter_id, patient_id, icu_id, elective_surgery, icu_admit_source, icu_stay_type, apache_2_diagnosis) VALUES ('119783', '50777', '93', '0', 'Accident & Emergency', 'admit', '122.0');
INSERT INTO encounters (encounter_id, patient_id, icu_id, elective_surgery, icu_admit_source, icu_stay_type, apache_2_diagnosis) VALUES ('79267', '46918', '92', '1', 'Operating Room / Recovery', 'admit', '203.0');
INSERT INTO encounters (encounter_id, patient_id, icu_id, elective_surgery, icu_admit_source, icu_stay_type, apache_2_diagnosis) VALUES ('92056', '34377', '91', '0', 'Accident & Emergency', 'admit', '119.0');
