# This code is the main.py used to create instances from the Patient class defined in classplay.py. It imports the necessary classes and creates instances of patients with different attributes to represent various patients.
# and to demonstrate the functionality of the PatientRecord class by adding patients and identifying high-risk individuals based on their heart disease status and cholesterol levels.

from patient import Patient, PatientRecord
# creates instances of the Patient class with different attributes to represent various patients.

p1 = Patient("Alice", 45, 250, "typical angina", True)
p2 = Patient("Bob", 50, 230, "atypical angina", False)
p3 = Patient("Charlie", 60, 260, "non-anginal pain", True)
p4 = Patient("Diana", 55, 220, "asymptomatic", False)
# demonstrates the functionality of the PatientRecord class by adding patients and identifying high-risk individuals based on their heart disease status and cholesterol levels.

record = PatientRecord() # creates a new instance of the PatientRecord class, setting up self.patients a list to be filled with patients
record.add_patient(p1) # calls add_patient method to add patient 1 the patient record list
record.add_patient(p2) # same for p2 and so on.
record.add_patient(p3)
record.add_patient(p4)

high_risk = record.high_risk_patients() # calls the high_risk_patients method to get a list of patients who are at high risk based on their heart disease status and cholesterol levels. This method uses a list comprehension to filter the patients in the record.
print("High-risk patients:") # prints a message indicating that the following output will be a triage of patients based on their risk level.
for patient in high_risk: # "patient" here is just the loop variable. This iterates through the list of high-risk patients and calls the risk_summary method for each patient 
    patient.risk_summary() # prints a summary of their risk factors and heart disease status.