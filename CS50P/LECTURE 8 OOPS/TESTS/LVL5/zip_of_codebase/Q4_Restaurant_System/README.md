# Q4 — Restaurant System (Revised for your current OOP notes)

## Scenario
A small restaurant uses menu items, tables and orders. The program runs, but its order and table behaviour is unreliable. Fix the existing application without replacing its overall design.

## Run it
From this folder, run:

```bash
python main.py
```

No packages need to be installed.

## Files
- `menu.py` — abstract menu-item parent and food/drink child classes
- `restaurant.py` — tables, orders and restaurant operations
- `main.py` — demonstration

## Requirements
1. Every menu item must have a non-empty name and a price greater than zero.
2. Food and drink items must provide their own descriptions.
3. Different menu-item objects must work through the shared `description()` behaviour.
4. A restaurant must not register the same table twice.
5. A table can have only one open order at a time.
6. An order belongs to one table and starts with the status `"open"`.
7. A closed order cannot accept more items or be closed again.
8. Closing an order must update the order and the table's current-order state.
9. The bill must equal the sum of the prices of the items in that order.
10. The restaurant must reject attempts to close an order that it does not manage.
11. The table summary must correctly show whether the table has an open order.

## Boundaries
- Keep the existing abstract `MenuItem` design and its `FoodItem` and `DrinkItem` subclasses.
- Use concepts from your notes: ABCs, inheritance, overriding, polymorphism, composition, object references, and `__str__` / `__len__`.
- No database, API, file storage, advanced typing, or extra framework is required.
- You do not need to invent a customer-management system. Focus on the requirements above.
