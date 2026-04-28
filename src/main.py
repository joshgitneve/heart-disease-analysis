# This code is the main.py used to create instances from the Patient class defined in classplay.py. It imports the necessary classes and creates instances of patients with different attributes to represent various patients.
# and to demonstrate the functionality of the PatientRecord class by adding patients and identifying high-risk individuals based on their heart disease status and cholesterol levels.

from patient import Patient, PatientRecord, triage
# creates instances of the Patient class with different attributes to represent various patients.

p1 = Patient("Alice", 45, 250, "typical angina", True)
p2 = Patient("Bob", 50, 230, "atypical angina", False)
p3 = Patient("Charlie", 60, 260, "non-anginal pain", True)
p4 = Patient("Diana", 55, 220, "asymptomatic", False)
p5 = Patient("Eve", 65, 270, "typical angina", True)
# demonstrates the functionality of the PatientRecord class by adding patients and identifying high-risk individuals 

record = PatientRecord() # initialise empty patient record list
record.add_patient(p1) # calls add_patient method to add patient 1 the patient record list
record.add_patient(p2) # same for p2 and so on.
record.add_patient(p3)
record.add_patient(p4)
record.add_patient(p5)



print("patient triage:")
for patient in record.patients:
    print(f"{patient.name}: {triage(patient)}") # prints the triage results for each patient, showing their risk level based on their chest pain type.

high_risk = record.high_risk_patients() # calls the high_risk_patients method 
print("High-risk patients:") # prints a message indicating that the following output will be a triage of patients based on their risk level.
for patient in high_risk: # "patient" here is just the loop variable. This iterates through the list of high-risk patients and calls the risk_summary method for each patient 
    patient.risk_summary() # prints a summary of their risk factors and heart disease status.