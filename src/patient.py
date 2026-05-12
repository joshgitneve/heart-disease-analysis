# !/usr/bin/env python3
# defines a Patient class with attributes for name, age, cholesterol level, chest-pain type, and heart disease status.
import pandas as pd

class Patient:
    """Patient class: blueprint for patients entering the cardiovascular unit.
:param patient_id: unique identifier for the patient
:type patient_id: int
:param age: patient age in years
:type age: int
:param sex: biological sex, binary encoded (1 = M, 0 = F)
:type sex: int
:param resting_bp: resting blood pressure in mmHg
:type resting_bp: int
:param cholesterol: serum cholesterol in mg/dL
:type cholesterol: float
:param fasting_bs: fasting blood sugar, binary encoded (1 = > 120mg/dL, 0 = normal)
:type fasting_bs: int
:param max_hr: maximum heart rate achieved
:type max_hr: int
:param exercise_angina: exercise induced angina, binary encoded (1 = Yes, 0 = No)
:type exercise_angina: int
:param oldpeak: ST depression induced by exercise
:type oldpeak: float
:param heart_disease: heart disease diagnosis, binary encoded (1 = diagnosed, 0 = clear)
:type heart_disease: int
:param chest_pain_type: chest pain type (ASY, ATA, NAP, TA)
:type chest_pain_type: str
:param resting_ecg: resting ECG results (Normal, LVH, ST)
:type resting_ecg: str
:param st_slope: slope of peak exercise ST segment (Up, Flat, Down)
:type st_slope: str
"""
    def __init__(self, patient_id, age, sex, resting_bp, cholesterol, fasting_bs, max_hr, exercise_angina, 
                 oldpeak, heart_disease, chest_pain_type, 
                 resting_ecg, st_slope):
        self.patient_id = patient_id
        self.age = age
        self.sex = sex
        self.resting_bp = resting_bp
        self.cholesterol = cholesterol
        self.fasting_bs = fasting_bs
        self.max_hr = max_hr
        self.exercise_angina = exercise_angina
        self.oldpeak = oldpeak
        self.heart_disease = heart_disease
        self.chest_pain_type = chest_pain_type
        self.resting_ecg = resting_ecg
        self.st_slope = st_slope
# includes a method to summarize the patient's risk factors and heart disease status.    
    def risk_summary(self):
        status = 'diagnosed' if self.heart_disease == 1 else 'clear'
        return(f"Patient {int(self.patient_id)} | Age: {int(self.age)} | "
          f"Cholesterol: {self.cholesterol} mg/dL | "
          f"Chest pain: {self.chest_pain_type} | "
          f"Heart disease: {status}")

    def __repr__(self):
        # repr is used when Python needs to represent the object in a list, notebook, or debugger - to unambiguously identify an object
        return f"Patient ({self.patient_id}, {self.age}, {self.chest_pain_type}, {self.heart_disease})"
    
# defines a PatientRecord class to manage multiple patients, allowing for adding patients and identifying high-risk individuals based on their heart disease status and cholesterol levels. 
class PatientRecord:
    def __init__(self):
        self.patients = [] # initializes an empty list to store patient records.
    
    #class method that reads the csv and adds its contents as an instance of PatientRecord
    @classmethod
    def load_from_csv(cls, filepath): # cls is like self but refers to the class rather than an instance
        
        df = pd.read_csv(filepath)# read the csv into a dateframe
        record = cls()  # creates a new empty PatientRecord
        for _, row in df.iterrows():
            #need to prepare the one-hot coded values first - for e.g. chest_pain_type there are four columns and for each row just one has 1 and the others 0 )
            chest_pain_cols = ['ChestPainType_ASY', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA']
            chest_pain_type = row[chest_pain_cols].idxmax().replace('ChestPainType_', '')
            resting_ECG_cols = ['RestingECG_LVH', 'RestingECG_Normal',  'RestingECG_ST']
            resting_ECG_type = row[resting_ECG_cols].idxmax().replace('RestingECG_', '')
            st_slope_cols = ['ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up']
            st_slope_type = row[st_slope_cols].idxmax().replace('ST_Slope_', '')
            patient = Patient(patient_id=row["PatientID"], age = row["Age"], sex = row["Sex"], resting_bp = row["RestingBP"], cholesterol = row["Cholesterol"], fasting_bs = row["FastingBS"], max_hr = row["MaxHR"], exercise_angina = row["ExerciseAngina"], oldpeak = row["Oldpeak"], heart_disease = row["HeartDisease"], chest_pain_type = chest_pain_type, resting_ecg = resting_ECG_type, st_slope = st_slope_type)
            record.add_patient(patient)
        return record
    
# includes two methods, add_patient, high_risk_patients, 
    def add_patient(self, patient):
        self.patients.append(patient)
# the following method incorporates a list comprehension, which is a compact way of building a list based on an existing iterable. It iterates through the list of patients and selects those who have heart disease and a cholesterol level greater than 240, returning a new list of high-risk patients.
# the same could be achieved with def high_risk_patients(self):
#    result = []
#   for p in self.patients:
#        if p.has_heart_disease and p.cholesterol > 240:
#            result.append(p)
#    return result

    

    def high_risk_patients(self): #returns patients at high risk based on their heart disease status and cholesterol levels. This method uses a list comprehension to filter the patients in the record.
        return [p for p in self.patients if p.heart_disease == 1 and p.cholesterol > 240]
            
# uses match to apply a risk tag to patients for which this method is called
    @staticmethod
    def triage(patient):
            match patient.chest_pain_type:
                case "TA":
                    return "High risk"
                case "ATA":
                    return "Moderate risk"
                case "NAP":
                    return "Low risk"
                case "ASY":
                    return "Minimal risk"
                case _:
                    return "Unknown risk" 