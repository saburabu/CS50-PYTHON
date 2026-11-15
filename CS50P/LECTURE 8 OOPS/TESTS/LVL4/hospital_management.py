class Doctor:
    def __init__(self, name, specialty, license_id):
        if not all([name, specialty, license_id]) or not all(isinstance(x, str) for x in [name, specialty, license_id]):
            raise ValueError("Hafa doctor no dey fuck up ooo na men")

        self.name = name
        self._specialty = specialty
        self.license_id = license_id  # Matched this to your find_doctor logic

    def __str__(self):
        return f"Dr. {self.name} | Specialty: {self._specialty} | ID: {self.license_id}"


class Hospital:
    def __init__(self, doctors=None):
        # Allows passing existing doctors at initialization (Requirement 2)
        self._doctors = []
        if doctors:
            for doc in doctors:
                self.add_doctor(doc)

    def add_doctor(self, doctor):
        if not isinstance(doctor, Doctor):
            raise ValueError("Doctor must be an object from the Doctor class")
        
        if doctor not in self._doctors:
            self._doctors.append(doctor)

    def remove_doctor(self, doctor_name):
        if not doctor_name or not isinstance(doctor_name, str):
            raise ValueError("Omo you sef ehh")

        for index, doc in enumerate(self._doctors):
            if doc.name == doctor_name:
                del self._doctors[index]
                return
        raise ValueError("Omo doctor no dey for here")

    def find_doctor(self, license_id):
        if not license_id or not isinstance(license_id, str):
            raise ValueError("Omo you dey fuck up")

        for doc in self._doctors:
            if doc.license_id == license_id:
                return doc  
        return None

    # Requirement 6: Return the number of doctors
    def __len__(self):
        return len(self._doctors)

    # Requirement 7: Display all doctors working in the hospital
    def display_doctors(self):
        if not self._doctors:
            print("No doctors currently working here.")
            return
        
        for doc in self._doctors:
            print(doc)


# --- Testing the Code ---
doc1 = Doctor("Chinedu", "Cardiology", "DOC-001")
doc2 = Doctor("Amina", "Neurology", "DOC-002")

# Requirement 2: Pass existing doctors on creation, or add them later
hospital = Hospital([doc1])
hospital.add_doctor(doc2)

print(f"Total doctors: {len(hospital)}")  # Uses __len__()
hospital.display_doctors()

# Requirement 5: Find by ID
found = hospital.find_doctor("DOC-002")
print(f"Found: {found}")

# Requirement 4: Doctor still exists after removal/hospital deletion
hospital.remove_doctor("Chinedu")
print(f"Still independent: {doc1}")
