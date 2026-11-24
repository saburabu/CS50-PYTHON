class Event:
    def __init__(self, title, venue, date, capacity):
        self.title = title
        self.venue = venue
        self.date = date
        self.capacity = capacity
        self.bookings = []

    def spaces_left(self):
        # BUG: cancelled bookings are still counted as occupying spaces.
        return self.capacity - len(self.bookings)

    def add_booking(self, booking):
        self.bookings.append(booking)

    def __str__(self):
        return f"{self.title} at {self.venue} on {self.date}"


class Attendee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Booking:
    def __init__(self, reference, attendee, event):
        self.reference = reference
        self.attendee = attendee
        self.event = event
        self.status = "confirmed"

    def cancel(self):
        self.status = "cancelled"

    def __str__(self):
        return f"{self.reference}: {self.attendee.name} — {self.event.title} ({self.status})"
