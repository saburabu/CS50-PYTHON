# Q2 — Event Booking System (Revised for your current OOP notes)

## Scenario
You inherited a small event-booking program. It runs, but some of its rules are wrong. Your job is to inspect the existing objects, fix the behaviour, and keep the demonstration working.

## Run it
From this folder, run:

```bash
python main.py
```

No packages need to be installed. The code intentionally uses ordinary classes and familiar lists. It does not require advanced typing or dataclass features.

## Files
- `models.py` — Event, Attendee and Booking objects
- `booking_system.py` — coordinates booking and cancellation
- `main.py` — demonstration

## Requirements
1. Event title, venue and date must not be empty. Capacity must be a positive number.
2. Attendee name and email must not be empty. The email must contain a basic `@` and a dot after it.
3. An attendee may have only one active booking for the same event.
4. A booking can only be created when the event has an available space.
5. Confirmed bookings must never exceed event capacity.
6. Cancelling a booking must change its status and make the space available again.
7. Cancelling a booking must not delete the historical booking record.
8. The attendee's booking history and the event's booking history must remain accurate.
9. Reports and booking summaries must show the correct current information.
10. Keep objects as the program's core state. Do not replace the objects with parallel dictionaries or lists of unrelated values.

## Boundaries
- Use concepts from your OOP notes: classes, objects, methods, properties if useful, object references, and encapsulation.
- No database, API, files, decorators, custom iterators, or advanced architecture is required.
- You may add or change methods when there is a good reason, but don't rebuild the whole application unnecessarily.
