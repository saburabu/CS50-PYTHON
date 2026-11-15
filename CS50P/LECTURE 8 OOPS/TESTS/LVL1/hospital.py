class Patient:
    def __init__(self, patient_id, name, age, department, current_condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.department = department
        self.current_condition = current_condition
        self.consultation_status = "Incomplete"  # Begins as incomplete

    def update_condition(self, new_condition):
        self.current_condition = new_condition

    def assign_department(self, new_department):
        self.department = new_department

    def complete_consultation(self):
        self.consultation_status = "Completed"

    def display_info(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Current Condition: {self.current_condition}")
        print(f"Consultation Status: {self.consultation_status}")
        print("-" * 30)

# A list to hold our patient objects
hospital_patients = []

# 1. Registering 10 patients dynamically using a loop or manual instantiation
sample_data = [
    (101, "Amina Yusuf", 34, "Cardiology", "Hypertension"),
    (102, "Chidi Okafor", 45, "Emergency", "Fractured arm"),
    (103, "Tunde Adeleke", 28, "General Practice", "Mild fever"),
    (104, "Fatima Bello", 52, "Neurology", "Migraine"),
    (105, "Ikechukwu Eze", 39, "Orthopedics", "Back pain"),
    (106, "Zainab Ibrahim", 61, "Cardiology", "Arrhythmia"),
    (107, "David Mensah", 23, "Emergency", "Laceration"),
    (108, "Grace Nwosu", 48, "Pediatrics", "Asthma check"),
    (109, "Musa Danladi", 55, "General Practice", "Hypertension"),
    (110, "Kemi Balogun", 31, "Dermatology", "Allergic reaction"),
]

for p_id, name, age, dept, condition in sample_data:
    new_patient = Patient(p_id, name, age, dept, condition)
    hospital_patients.append(new_patient)

# 2. Updating a patient's condition (e.g., Patient ID 101)
hospital_patients[0].update_condition("Stabilized - Blood pressure normal")

# 3. Assigning a patient to a different department (e.g., Patient ID 102)
hospital_patients[1].assign_department("Surgery")

# 4. Marking a consultation as completed (e.g., Patient ID 103)
hospital_patients[2].complete_consultation()

# 5. Displaying all patients' complete information
for patient in hospital_patients:
    patient.display_info()
