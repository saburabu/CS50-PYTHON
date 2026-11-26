from __future__ import annotations
from pathlib import Path as P
import random, time, json, re, uuid
from datetime import datetime, timedelta
from cards import generate_member_card_pdf, generate_trainer_card_pdf
start_time = time.perf_counter()

BASE_DIR = P(__file__).resolve().parent
MEMBERS_FILE = BASE_DIR / "members.json"
TRAINERS_FILE = BASE_DIR / "trainers.json"

class Member:
    members = []
    statuses = ["in progress", "completed", "cancelled"]
    REG_FEE = 20000.0
    programs = {
        "Weight Loss / Fat Loss",
        "Muscle Gain",
        "Body Recomposition",
        "Toning & Definition",
        "Facial Definition",
        "Healthy Weight Gain",
        "General Strength",
        "Athletic Performance & Power",
        "Muscular Endurance",
        "Cardio & Stamina",
        "General Health & Longevity",
        "Stress Relief & Mental Health",
        "Flexibility & Mobility",
        "Posture & Core Stability",
        "Event or Milestone Prep",
    }

    @staticmethod
    def generate_member_id() -> str:
        members = Member.load_json()
        existing_ids = {
            m.get("membership_id") if isinstance(m, dict) else m.membership_id
            for m in members
        }
        while True:
            # :04d ensures IDs are always 4 digits (e.g., MEM-0042)
            new_id = f"MEM-{random.randint(1, 9999):04d}"
            if new_id not in existing_ids:
                return new_id

    def __init__(
        self,
        full_name: str,
        dob: str,
        number: str,
        email: str,
        gender: str,
        emergency_contact: str,
        weight: float,
        height: float,
        program: str,
        goals: str,
        status: str,
        amount: float,
    ):
        if not isinstance(full_name, str) or not re.fullmatch(
            r"[A-Za-z]+(?:\s+[A-Za-z]+){1,2}", full_name.strip()
        ):
            raise ValueError(
                "Invalid name format: provide first name plus 1 or 2 other names"
            )

        try:
            parsed_dob = datetime.strptime(dob, "%d/%m/%Y")
        except (TypeError, ValueError):
            raise ValueError("Invalid date of birth format e.g: '23/09/2010'")

        phone_pattern = r"(?:\+234|234|0)[0-9]{10}"
        if not isinstance(number, str) or not re.fullmatch(phone_pattern, number):
            raise ValueError(
                "Invalid phone number format e.g: '+2349099999999', '2349099999999', or '09099999999'"
            )

        email_pattern = r"[a-zA-Z0-9_%+'-]+(?:\.[a-zA-Z0-9_%+'-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}"
        if not isinstance(email, str) or not re.fullmatch(
            email_pattern, email, re.IGNORECASE
        ):
            raise ValueError("Invalid email format e.g: 'user9099@gmail.com'")

        if not isinstance(gender, str) or not re.fullmatch(r"[FM]", gender, re.IGNORECASE):
            raise ValueError("Invalid gender format e.g: 'M' or 'F'")

        if not isinstance(emergency_contact, str) or not re.fullmatch(
            phone_pattern, emergency_contact
        ):
            raise ValueError(
                "Invalid emergency contact format e.g: '+2349099999999', '2349099999999', or '09099999999'"
            )

        if (
            not isinstance(weight, (int, float))
            or isinstance(weight, bool)
            or not 25.0 <= weight <= 300.0
        ):
            raise ValueError("Invalid weight: must be between 25.0kg and 300.0kg")

        if (
            not isinstance(height, (int, float))
            or isinstance(height, bool)
            or not 150.0 <= height <= 230.0
        ):
            raise ValueError("Invalid height: must be between 150.0cm and 230.0cm")

        if not isinstance(program, str) or program not in Member.programs:
            raise ValueError(
                "Selected program doesn't exist. Available: "
                + ", ".join(Member.programs)
            )

        if not isinstance(goals, str) or not (
            20 <= sum(c.isalpha() or c == "." for c in goals) <= 100
        ):
            raise ValueError(
                "Goals must contain between 20 and 100 letters or periods."
            )
        
        if amount != self.REG_FEE:
            raise ValueError("Gym fee is 20k nothing more nothing less.")

        # Inside Member.__init__ (after validating phone & email formats):
        existing_members = Member.load_json()
        clean_email = email.strip().lower()

        for m in existing_members:
            if m.get("email") == clean_email:
                raise ValueError(f"A member with email '{clean_email}' already exists.")
            if m.get("phone_number") == number:
                raise ValueError(f"A member with phone number '{number}' already exists.")

        self.membership_id = self.generate_member_id()
        self.full_name = full_name.strip().title()
        self.dob = dob
        self.number = number
        self.email = email.strip().lower()
        self.gender = gender.upper()
        self.emergency_contact = emergency_contact
        self.weight = float(weight)
        self.height = float(height)
        self.program = program
        self.status = status if status else "in progress"
        self.registration_date = datetime.now().strftime("%Y-%m-%d")
        self.start_date = datetime.now().strftime("%Y-%m-%d")
        self.goals = goals.strip().title()

        today = datetime.now()
        self.age = int((today - parsed_dob).days // 365.25)

        self.members_dict = {
            "membership_id": self.membership_id,
            "full_name": self.full_name,
            "dob": self.dob,
            "phone_number": self.number,
            "email": self.email,
            "gender": self.gender,
            "emergency_contact": self.emergency_contact,
            "weight": self.weight,
            "height": self.height,
            "program": self.program,
            "goals": self.goals,
            "age": self.age,
            "status": self.status,
            "registration_date": self.registration_date,
            "start_date": self.start_date,
        }
        self.members.append(self.members_dict)
        generate_member_card_pdf

    @staticmethod
    def save_json(member: Member) -> None:
        if not isinstance(member, Member):
            raise ValueError("Expected a valid Member object")

        existing_members = Member.load_json()

        # Replace existing entry if ID already exists
        for i, m in enumerate(existing_members):
            if m.get("membership_id") == member.membership_id:
                existing_members[i] = member.members_dict
                break
        else:
            # Only runs if the loop didn't find a match
            existing_members.append(member.members_dict)

        with open(MEMBERS_FILE, "w", encoding="utf-8") as file:
            json.dump(existing_members, file, indent=4)


    @staticmethod
    def load_json() -> list:
        if not MEMBERS_FILE.exists() or MEMBERS_FILE.stat().st_size == 0:
            return []
        try:
            with open(MEMBERS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def is_plan_active(self) -> bool:
        start = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        expiry_date = start + timedelta(days=7)
        return datetime.now().date() <= expiry_date

    def renew_plan(self, amount: float) -> None:
        if amount != self.REG_FEE:
            raise ValueError("Gym fee is 20k nothing more nothing less.")
        self.start_date = datetime.now().strftime("%Y-%m-%d")
        self.members_dict["start_date"] = self.start_date

    def __str__(self) -> str:
        return (
            f"[{self.membership_id}] Name: {self.full_name}, Age: {self.age}, "
            f"Phone: {self.number},\nProgram: {self.program}, Goals: {self.goals}"
        )

    def create_pdf_card(self) -> P:
        return generate_member_card_pdf(self)

class Session:
    DAILY_HOURS = 3  # Universal 3-hour limit per session

    def __init__(self, member_id: str):
        if not isinstance(member_id, str) or not re.fullmatch(
            r"MEM-\d{4}", member_id, re.IGNORECASE
        ):
            raise ValueError("Invalid membership id format e.g: 'MEM-9999'")

        self.session_code = f"SES-{uuid.uuid4().hex[:6].upper()}"
        self.member_id = member_id.upper()
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=self.DAILY_HOURS)

    def is_running(self) -> bool:
        """True if the 3-hour timer is still counting down."""
        return datetime.now() < self.end_time

    def time_left(self) -> str:
        """Returns remaining minutes or 'Time Over'."""
        if not self.is_running():
            return "Time Over"
        remaining = self.end_time - datetime.now()
        mins = int(remaining.total_seconds() // 60)
        return f"{mins // 60}h {mins % 60}m left"

    def __str__(self):
        status = self.time_left()
        return (
            f"[{self.session_code}] Member: {self.member_id} | "
            f"Start: {self.start_time.strftime('%H:%M')} | "
            f"End: {self.end_time.strftime('%H:%M')} | Status: {status}"
        )

class Trainer:
    trainers = []
    salary = 30000

    @staticmethod
    def generate_trainer_id() -> str:
        existing_trainers = Trainer.load_json()
        existing_ids = {t.get("trainer_id") for t in existing_trainers}
        while True:
            new_id = f"TRN-{random.randint(1, 9999):04d}"
            if new_id not in existing_ids:
                return new_id

    def __init__(
        self,
        full_name: str,
        number: str,
        email: str,
        gender: str,
        specialty: str,
        account_number: str,
        is_available: bool = True,
    ):
        if not isinstance(full_name, str) or not re.fullmatch(
            r"[A-Za-z]+(?:\s+[A-Za-z]+){1,2}", full_name.strip()
        ):
            raise ValueError("Invalid name format: provide first name plus 1 or 2 other names")

        phone_pattern = r"(?:\+234|234|0)[0-9]{10}"
        if not isinstance(number, str) or not re.fullmatch(phone_pattern, number):
            raise ValueError("Invalid phone number format e.g: '+2349099999999' or '09099999999'")

        email_pattern = r"[a-zA-Z0-9_%+'-]+(?:\.[a-zA-Z0-9_%+'-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}"
        if not isinstance(email, str) or not re.fullmatch(email_pattern, email, re.IGNORECASE):
            raise ValueError("Invalid email format e.g: 'user9099@gmail.com'")

        if not isinstance(gender, str) or not re.fullmatch(r"[FM]", gender, re.IGNORECASE):
            raise ValueError("Invalid gender format e.g: 'M' or 'F'")

        if not isinstance(specialty, str) or specialty not in Member.programs:
            raise ValueError("Trainer must specialize in one of: " + ", ".join(Member.programs))

        if not isinstance(is_available, bool):
            raise ValueError("Availability must be a boolean value")

        if not isinstance(account_number, str) or not re.fullmatch(r"[0-9]{10}", account_number):
            raise ValueError("Invalid account number: must be 10 digits e.g: '0022112211'")

        # Inside Member.__init__ (after validating phone & email formats):
        existing_members = Trainer.load_json()
        clean_email = email.strip().lower()

        for m in existing_members:
            if m.get("email") == clean_email:
                raise ValueError(f"A member with email '{clean_email}' already exists.")
            if m.get("phone_number") == number:
                raise ValueError(f"A member with phone number '{number}' already exists.")


        self.trainer_id = self.generate_trainer_id()
        self.full_name = full_name.strip().title()
        self.phone_number = number
        self.email = email.strip().lower()
        self.gender = gender.upper()
        self.specialty = specialty
        self.is_available = is_available
        self.account_number = account_number

        now = datetime.now()
        self.reg_date = now.strftime("%Y-%m-%d")
        self.pay_day = (now + timedelta(days=30)).strftime("%Y-%m-%d")

        self.trainer_dict = {
            "trainer_id": self.trainer_id,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "gender": self.gender,
            "specialty": self.specialty,
            "is_available": self.is_available,
            "reg_date": self.reg_date,
            "pay_day": self.pay_day,
            "account_number": self.account_number,
        }

        self.trainers.append(self.trainer_dict)


    @staticmethod
    def save_json(trainer: Trainer) -> None:
        if not isinstance(trainer, Trainer):
            raise ValueError("Expected a valid Member object")

        existing_members = Trainer.load_json()

        # Replace existing entry if ID already exists
        for i, m in enumerate(existing_members):
            if m.get("trainer_id") == trainer.trainer_id:
                existing_members[i] = trainer.trainer_dict
                break
        else:
            # Only runs if the loop didn't find a match
            existing_members.append(trainer.trainer_dict)

        with open(TRAINERS_FILE, "w", encoding="utf-8") as file:
            json.dump(existing_members, file, indent=4)


    @staticmethod
    def load_json() -> list:
        if not TRAINERS_FILE.exists() or TRAINERS_FILE.stat().st_size == 0:
            return []
        try:
            with open(TRAINERS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def pay_salary(self) -> None:
        today = datetime.now().date()
        pay_date = datetime.strptime(self.pay_day, "%Y-%m-%d").date()

        if today < pay_date:
            raise ValueError(f"It's not yet time for salary. Next payday: {self.pay_day}")

        print(f"Processing transfer of ₦{self.salary:,} to {self.full_name}, account: {self.account_number}...")
        time.sleep(0.5)
        print(f"Done! Transfer made to {self.full_name}.")

        # Update this object in memory
        self.pay_day = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.trainer_dict["pay_day"] = self.pay_day

        # Update this trainer's record in trainers.json without creating a duplicate
        trainers = self.load_json()
        for t in trainers:
            if t.get("trainer_id") == self.trainer_id:
                t["pay_day"] = self.pay_day
                break

        with open(TRAINERS_FILE, "w", encoding="utf-8") as file:
            json.dump(trainers, file, indent=4)


    def create_pdf_card(self) -> P:
        return generate_trainer_card_pdf(self)
