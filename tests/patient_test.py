from src.patient import Patient, PatientRecord

def test_patient_instance_creation():

    patient_99 = Patient(999999, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'ASY', 'Normal', 'Up')
    assert patient_99.patient_id == 999999
    assert patient_99.age == 99
    assert patient_99.sex == 1
    assert patient_99.resting_bp == 99
    assert patient_99.cholesterol == 99
    assert patient_99.fasting_bs == 0
    assert patient_99.max_hr == 250
    assert patient_99.exercise_angina == 0
    assert patient_99.oldpeak == 1.5
    assert patient_99.heart_disease == 1
    assert patient_99.chest_pain_type == 'ASY'
    assert patient_99.resting_ecg == 'Normal'
    assert patient_99.st_slope == 'Up'

def test_risk_summary_diagnosed():
    patient_diagnosed = Patient(999998, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'ASY', 'Normal', 'Up')
    
    assert "diagnosed" in patient_diagnosed.risk_summary()
    assert "999998" in patient_diagnosed.risk_summary()
    
    
def test_risk_summary_clear():
    
    patient_clear = Patient(999997, 99, 1, 99, 99, 0, 250, 0, 1.5, 0, 'ASY', 'Normal', 'Up')
    
    assert "clear" in patient_clear.risk_summary()
    assert "999997" in patient_clear.risk_summary()

def test_triage_ASY_pain():
    patient_ASY = Patient(999998, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'ASY', 'Normal', 'Up')
    
    assert PatientRecord.triage(patient_ASY) == "Minimal risk"
    
def test_triage_ATA_pain():
    patient_ATA = Patient(999998, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'ATA', 'Normal', 'Up')

    assert PatientRecord.triage(patient_ATA) == "Moderate risk"

def test_triage_NAP_pain():
    patient_NAP = Patient(999998, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'NAP', 'Normal', 'Up')

    assert PatientRecord.triage(patient_NAP) == "Low risk"

def test_triage_TA_pain():
    patient_TA = Patient(999998, 99, 1, 99, 99, 0, 250, 0, 1.5, 1, 'TA', 'Normal', 'Up')

    assert PatientRecord.triage(patient_TA) == "High risk"


def test_load_from_csv():#integration test
    test_load = PatientRecord.load_from_csv("data/processed/heart_cleaned.csv")

    assert len(test_load.patients) == 917 

def test_high_risk_patients():#sets up a new instance of PatientRecord(), adds some controlled patients, and then tests high_risk_patients() on that instance
    record = PatientRecord()

    # definitely high risk - heart disease AND high cholesterol
    high_risk = Patient(111111, 60, 1, 120, 300, 0, 150, 0, 1.0, 1, 'ASY', 'Normal', 'Up')
    # heart disease but low cholesterol - should NOT appear
    not_high_risk_1 = Patient(222222, 60, 1, 120, 200, 0, 150, 0, 1.0, 1, 'ASY', 'Normal', 'Up')
    # high cholesterol but no heart disease - should NOT appear
    not_high_risk_2 = Patient(333333, 60, 1, 120, 300, 0, 150, 0, 1.0, 0, 'ASY', 'Normal', 'Up')

    record.add_patient(high_risk)
    record.add_patient(not_high_risk_1)
    record.add_patient(not_high_risk_2)
    
    result = record.high_risk_patients()

    assert len(result) == 1
    assert result[0].patient_id == 111111