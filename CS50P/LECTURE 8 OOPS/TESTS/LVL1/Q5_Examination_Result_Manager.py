class Student:
    def __init__(self, name, reg_number):
        # Initialize basic student details
        self.name = name
        self.reg_number = reg_number
        # A dictionary to store subjects as keys and scores as values
        self.subject_scores = {}

    def add_subject_score(self, subject, score):
        """Adds a new subject and its score if it doesn't already exist."""
        if score < 0 or score > 100:
            print(f"Error: Score for {subject} must be between 0 and 100.")
            return

        # Normalize the subject name to avoid case-sensitive duplicates (e.g., "Math" vs "math")
        subject_key = subject.strip().title()

        if subject_key in self.subject_scores:
            print(f"Error: {subject_key} already exists. Use update_score() to modify it.")
        else:
            self.subject_scores[subject_key] = score
            print(f"Added {subject_key}: {score} for {self.name}.")

    def update_score(self, subject, new_score):
        """Updates the score of an existing subject."""
        if new_score < 0 or new_score > 100:
            print(f"Error: Score for {subject} must be between 0 and 100.")
            return

        subject_key = subject.strip().title()

        if subject_key in self.subject_scores:
            self.subject_scores[subject_key] = new_score
            print(f"Updated {subject_key} score to {new_score} for {self.name}.")
        else:
            print(f"Error: {subject_key} does not exist in {self.name}'s records.")

    def calculate_total(self):
        """Calculates and returns the total score across all subjects."""
        return sum(self.subject_scores.values())

    def calculate_average(self):
        """Calculates and returns the average score."""
        if not self.subject_scores:
            return 0.0
        return self.calculate_total() / len(self.subject_scores)

    def display_results(self):
        """Displays all subjects, scores, total, and average for the student."""
        print(f"\n======================================")
        print(f"EXAMINATION REPORT: {self.name}")
        print(f"Registration Number: {self.reg_number}")
        print(f"--------------------------------------")
        
        if not self.subject_scores:
            print("No subject records found.")
        else:
            for subject, score in self.subject_scores.items():
                print(f" {subject:<20} : {score}")
            print(f"--------------------------------------")
            print(f" Total Score          : {self.calculate_total()}")
            print(f" Average Score        : {self.calculate_average():.2f}")
        print(f"======================================")


# ==========================================
# Creating and Testing Three Student Objects
# ==========================================

# 1. Creating Student 1: Alice
student1 = Student("Alice Smith", "REG001")
student1.add_subject_score("Mathematics", 85)
student1.add_subject_score("English", 92)
student1.add_subject_score("Physics", 78)
# Testing rule validation (Invalid score)
student1.add_subject_score("Chemistry", 105) 
# Testing rule validation (Duplicate subject)
student1.add_subject_score("Mathematics", 90) 
student1.display_results()

# 2. Creating Student 2: Bob
student2 = Student("Bob Jones", "REG002")
student2.add_subject_score("History", 74)
student2.add_subject_score("Geography", 81)
student2.add_subject_score("English", 68)
# Testing updating an entry
student2.update_score("English", 75) 
student2.display_results()

# 3. Creating Student 3: Charlie
student3 = Student("Charlie Brown", "REG003")
student3.add_subject_score("Biology", 95)
student3.add_subject_score("Chemistry", 88)
student3.add_subject_score("Computer Science", 99)
student3.display_results()
