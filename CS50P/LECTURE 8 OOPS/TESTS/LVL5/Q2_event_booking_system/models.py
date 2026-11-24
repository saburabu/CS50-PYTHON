import re

class Event:
    def __init__(self, title, venue, date, capacity):
        # Check isinstance FIRST so Python short-circuits before calling .strip()
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Title must be a non-empty string, not {title}")

        if not isinstance(venue, str) or not venue.strip():
            raise ValueError(f"Venue must be a non-empty string, not {venue}")

        if not isinstance(date, str) or not re.fullmatch(r"\d{2}/\d{2}/\d{4}", date):
            raise ValueError('Date must be a string in the format "12/03/2026"')


        if (not isinstance(capacity, int) or 
            isinstance(capacity, bool) 
            or capacity <= 0):
            raise ValueError("Capacity must be an integer and must be greater then 0")
        
        self.title = title
        self.venue = venue
        self.date = date
        self.capacity = capacity
        self.bookings = []

    def spaces_left(self):
        return self.capacity - sum(1 for b in self.bookings if b.status == "confirmed")


    def add_booking(self, booking):
        self.bookings.append(booking)

    def __str__(self):
        return f"{self.title} at {self.venue} on {self.date}"


class Attendee:
    def __init__(self, name, email):
        if not name.strip().lower() or not isinstance(name, str) or not re.fullmatch(r"[a-z]+(?:\s[a-z]+){1,2}", name, re.IGNORECASE):
            raise ValueError("Name must be in this format 'e.g: Sabur Osimua Abu' if you have a middle name and your value must be a string")

        if not isinstance(email, str) or not re.fullmatch(r"[a-zA-Z0-9_%+'-]+(?:\.[a-zA-Z0-9_%+'-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}", email):
            raise ValueError("Invalid email try again")

        
        self.name = name
        self.email = email
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Booking:
    def __init__(self, reference, attendee, event): # reference is like the serial number for the booking 
        self.reference = reference
        self.attendee = attendee
        self.event = event
        self.status = "confirmed"

    def cancel(self):
        self.status = "cancelled"

    def __str__(self):
        return f"{self.reference}: {self.attendee.name} — {self.event.title} ({self.status})"
