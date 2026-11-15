class Lecturer:
    def __init__(self, name, subject):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Lecturer's name must be a non-empty string")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject must be a non-empty string")
        self.name = name
        self.subject = subject

    def __repr__(self):
        return f"Lecturer({self.name!r}, {self.subject!r})"


class Department:
    def __init__(self, department_name, list_lecturers):
        if not isinstance(department_name, str) or not department_name.strip():
            raise ValueError("Department name must be a non-empty string")
        if not isinstance(list_lecturers, list) or not all(isinstance(l, Lecturer) for l in list_lecturers):
            raise ValueError("list_lecturers must be a list of Lecturer objects")
        
        self._department = department_name
        # Create a shallow copy so modifying the department doesn't mutate external lists
        self._lecturers = list(list_lecturers)

    def __repr__(self):
        return f"Department({self._department!r}, lecturers={self._lecturers!r})"

    def add_lecturer(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            raise ValueError("Must provide a Lecturer object")
        self._lecturers.append(lecturer)

    def remove_lecturer(self, lecturer_name):
        if not isinstance(lecturer_name, str) or not lecturer_name.strip():
            raise ValueError("Lecturer name must be a non-empty string")
        for index, value in enumerate(self._lecturers):
            if value.name == lecturer_name:
                del self._lecturers[index]
                return
        raise ValueError(f"Lecturer {lecturer_name} not found in {self._department}")

    def display_lecturers(self):
        print(f"Lecturers in {self._department}:")
        for lecturer in self._lecturers:
            print(f"- {lecturer.name} ({lecturer.subject})")

    def __len__(self):
        return len(self._lecturers)


# --- Testing Aggregation ---
# 1. Created independently of any department
l1 = Lecturer("sabur", "computer science")
l2 = Lecturer("samira", "Medicine")
l3 = Lecturer("ashra", "engineering")
l4 = Lecturer("mahira", "law")

# 2. Passed as a list of objects into the department
dep = Department("CS", [l1, l2])
dep.add_lecturer(l3)
dep.remove_lecturer("samira")

dep.display_lecturers()
print("Total lecturers:", len(dep))

# 3. Proof of Aggregation: Samira still exists even after being removed from CS
print("Independent object still exists:", l2)
