from models import Booking


class BookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []
        self._next_reference = 100

    def register_event(self, event):
        self.events.append(event)

    def make_booking(self, attendee, event):
        # BUG: this allows a booking when the event has exactly zero spaces left.
        if event.spaces_left() < 0:
            raise ValueError("This event is full.")

        # BUG: the same attendee can book the same event more than once.
        reference = f"BK-{self._next_reference}"
        self._next_reference += 1

        booking = Booking(reference, attendee, event)
        event.add_booking(booking)
        attendee.add_booking(booking)
        self.bookings.append(booking)
        return booking

    def cancel_booking(self, reference):
        for booking in self.bookings:
            if booking.reference == reference:
                booking.cancel()
                return
        raise LookupError("Booking not found.")

    def event_report(self, event):
        return f"{event}: {event.spaces_left()} space(s) left"
