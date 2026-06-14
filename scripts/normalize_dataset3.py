import pandas as pd
import os

RAW_FILE = '/app/data/raw/dataset.csv'
NORM_DIR = '/app/data/normalized/dataset3/'
DDL_FILE = '/app/sql/ddl/dataset3_schema.sql'

os.makedirs(NORM_DIR, exist_ok=True)
os.makedirs(os.path.dirname(DDL_FILE), exist_ok=True)

print("Normalización Hospitales Dataset 3 (dataset)")
df = pd.read_csv(RAW_FILE)

print("1. tabla de Pacientes (Patients): Los datos físicos y demográficos dependen exclusivamente del paciente (3FN) ")
 
patients_cols = ['patient_id', 'age', 'bmi', 'ethnicity', 'gender', 'height', 'weight']
patients_df = df[patients_cols].drop_duplicates(subset=['patient_id']).copy()
patients_df.fillna('Unknown', inplace=True)

print("2. tabla de Unidades Médicas (ICUs): La información del hospital depende de la unidad (ICU), no del paciente (3FN)")

icu_cols = ['icu_id', 'hospital_id', 'icu_type']
icus_df = df[icu_cols].drop_duplicates(subset=['icu_id']).copy()
icus_df.fillna('Unknown', inplace=True)

print("3. tabla de Encuentros Médicos (Encounters): El encuentro es la transacción que une al paciente con el hospital y su diagnóstico")

encounter_cols = ['encounter_id', 'patient_id', 'icu_id', 'elective_surgery', 'icu_admit_source', 'icu_stay_type', 'apache_2_diagnosis']
encounters_df = df[encounter_cols].copy()
encounters_df.fillna('Unknown', inplace=True)

print("Export CSVs data/normalized/dataset3")
patients_df.to_csv(os.path.join(NORM_DIR, 'patients.csv'), index=False)
icus_df.to_csv(os.path.join(NORM_DIR, 'icus.csv'), index=False)
encounters_df.to_csv(os.path.join(NORM_DIR, 'encounters.csv'), index=False)

print("script DDL de SQL")
ddl_script = """-- DDL Dataset 3: Hospitales normalizado a 3FN

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
"""

with open(DDL_FILE, 'w', encoding='utf-8') as f:
    f.write(ddl_script)

print("\nHospitales normalizado 'normalized/dataset3' y 'sql/ddl'")