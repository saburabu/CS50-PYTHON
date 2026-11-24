from models import Booking
import random
import re

class BookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def register_event(self, event):
        self.events.append(event)

    def make_booking(self, attendee, event):
        if event not in self.events:
            raise ValueError("Event is not registered in this system.")
        if event.spaces_left() <= 0:
            raise ValueError("This event is full.")

        for existing in event.bookings:
            if existing.attendee == attendee and existing.status == "confirmed":
                raise ValueError("Attendee is already booked for this event.")

        existing_refs = {b.reference for b in self.bookings}
        while True:
            reference = f"BK-{random.randint(1, 9999):04d}"
            if reference not in existing_refs:
                break

        booking = Booking(reference, attendee, event)
        event.add_booking(booking)
        attendee.add_booking(booking)
        self.bookings.append(booking)
        return booking

    def cancel_booking(self, reference):
        if not isinstance(reference, str) or not re.fullmatch(r"BK-\d{4}", reference):
            raise ValueError("Invalid reference format")
        for booking in self.bookings:
            if booking.reference == reference:
                booking.cancel()
                return
        raise LookupError("Booking not found.")

    def event_report(self, event):
        return f"{event}: {event.spaces_left()} space(s) left"
