from booking_system import BookingSystem
from models import Attendee, Event


def main():
    system = BookingSystem()
    python_night = Event("Python Night", "City Hub", "12/03/2026", 2)
    system.register_event(python_night)

    ada = Attendee("Ada bello", "ada@example.com")
    bello = Attendee("Bello ada", "bello@example.com")

    first = system.make_booking(ada, python_night)
    second = system.make_booking(bello, python_night)

    print(first)
    print(second)
    print(system.event_report(python_night))

    system.cancel_booking(first.reference)
    print(first)
    print(system.event_report(python_night))


if __name__ == "__main__":
    main()
