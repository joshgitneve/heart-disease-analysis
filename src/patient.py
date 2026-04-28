# !/usr/bin/env python3
# defines a Patient class with attributes for name, age, cholesterol level, chest-pain type, and heart disease status.
class Patient:
    def __init__(self, name, age, cholesterol, chest_pain_type, has_heart_disease):
        self.name = name
        self.age = age
        self.cholesterol = cholesterol
        self.chest_pain_type = chest_pain_type
        self.has_heart_disease = has_heart_disease
# includes a method to summarize the patient's risk factors and heart disease status.    
    def risk_summary(self):
        status = 'diagnosed' if self.has_heart_disease else 'clear'
        print (f"{self.name} is {self.age} years old with a cholesterol level of {self.cholesterol} mg/dL, experiences {self.chest_pain_type} and with a heart disease status of {status}.")

# defines a PatientRecord class to manage multiple patients, allowing for adding patients and identifying high-risk individuals based on their heart disease status and cholesterol levels. 
class PatientRecord:
    def __init__(self):
        self.patients = []
    
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

    

    def high_risk_patients(self):
        return [p for p in self.patients if p.has_heart_disease and p.cholesterol > 240]
            

def triage(patient):
        match patient.chest_pain_type:
            case "typical angina":
                return "High risk"
            case "atypical angina":
                return "Moderate risk"
            case "non-anginal pain":
                return "Low risk"
            case "asymptomatic":
                return "Minimal risk"
            case _:
                return "Unknown risk" 