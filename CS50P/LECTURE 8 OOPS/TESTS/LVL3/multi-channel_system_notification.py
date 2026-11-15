import re

class EmailNotification:
    @staticmethod
    def validate_email(email: str) -> bool:
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(email_pattern, email))

    def __init__(self, recipient_email: str, message: str):
        if not all(isinstance(x, str) for x in [recipient_email, message]):
            raise TypeError("Recipient email and message must both be strings!")

        recipient_email = recipient_email.strip()
        message = message.strip()

        if not message:
            raise ValueError("Notification message cannot be empty!")

        if self.validate_email(recipient_email):
            self.recipient_email = recipient_email.lower()
            self.message = message
        else:
            raise ValueError(f"Invalid email format: '{recipient_email}'")

    def send(self):
        print(f"[Email] To: {self.recipient_email} | Message: '{self.message}'")


class SMSNotification:
    @staticmethod
    def validate_number(phone_number: str) -> bool:
        pattern = r"^(?:\+234|234|0)(?:70|80|81|90|91)\d{8}$"
        return bool(re.fullmatch(pattern, phone_number))

    def __init__(self, phone_number: str, message: str):
        if isinstance(phone_number, str) and isinstance(message, str):
            phone_number = phone_number.strip()
            message = message.strip()

            if not message:
                raise ValueError("Please message cannot be empty")

            if self.validate_number(phone_number):
                self.number = phone_number
                self.message = message
            else:
                raise ValueError("Phone number format doesnt exist")
        else:
            raise TypeError("Phone number and message must both be strings")

    def send(self):
        print(f"[SMS] To: {self.number} | Message: '{self.message}'")


class WhatsAppNotification:
    @staticmethod
    def validate_number(phone_number: str) -> bool:
        pattern = r"^(?:\+234|234|0)(?:70|80|81|90|91)\d{8}$"
        return bool(re.fullmatch(pattern, phone_number))

    def __init__(self, phone_number: str, message: str):
        if isinstance(phone_number, str) and isinstance(message, str):
            phone_number = phone_number.strip()
            message = message.strip()

            if not message:
                raise ValueError("Please message cannot be empty")

            if self.validate_number(phone_number):
                self.number = phone_number
                self.message = message
            else:
                raise ValueError("Phone number format doesnt exist")
        else:
            raise TypeError("Phone number and message must both be strings")

    def send(self):
        print(f"[WhatsApp] To: {self.number} | Message: '{self.message}'")


class PushNotification:
    @staticmethod
    def validate_recipient(recipient: str) -> bool:
        token_pattern = r"^[A-Za-z0-9_-]{6,64}$"
        return bool(re.fullmatch(token_pattern, recipient))

    def __init__(self, recipient: str, message: str):
        if not isinstance(recipient, str) or not isinstance(message, str):
            raise TypeError("Both recipient and message must be strings!")

        recipient = recipient.strip()
        message = message.strip()

        if not message:
            raise ValueError("Push notification message cannot be empty!")

        if self.validate_recipient(recipient):
            self.recipient = recipient
            self.message = message
        else:
            raise ValueError(f"Invalid device token or recipient ID: '{recipient}'")

    def send(self):
        print(f"[Push Notification] Device: {self.recipient} | Alert: '{self.message}'")


class Smth:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message


def notify_user(notification):
    if hasattr(notification, "send") and callable(notification.send):
        notification.send()
    else:
        print(f"[Skipped] '{type(notification).__name__}' cannot send notifications.")


# --- TEST EXECUTION ---
email = EmailNotification("sabur@wigwe.edu.ng", "Welcome to the semester!")
sms = SMSNotification("08012345678", "Your OTP is 492011")
whatsapp = WhatsAppNotification("+2348012345678", "Your receipt is ready")
push = PushNotification("DEV-TOKEN-99481A", "New login detected on your account")
smth = Smth("ij2eije2e22e", "hi")

for alert in [email, sms, whatsapp, push, smth]:
    notify_user(alert)
