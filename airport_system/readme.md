# Flight
 
A flight class for managing passengers, with adding, removing, searching, and counting.
 
## `Flight` class methods
- `show_flight_info()` — print the flight number, destination, and how many seats are filled out of `max_passengers`.
- `add_passenger(name, passport, age)` — add a passenger to the flight; rejected if the flight is already full, the age is negative, or a passenger with the same passport number is already registered.
- `remove_passenger(passport)` — remove a passenger by passport number; prints a message if no matching passport is found.
- `show_passengers()` — print the total passenger count and the full list of passengers with their details.
- `find_passenger(passport)` — search for a passenger by passport number and print their name, passport, and age, or a "not found" message.
- `count_adults()` — return the number of passengers aged 18 or older.
- `count_children()` — return the number of passengers younger than 18.
- `is_full()` — return `True` if the number of passengers has reached `max_passengers`.
## Usage example
```python
flight = Flight("AZ101", "Istanbul", 5)
flight.show_flight_info()
 
flight.add_passenger("Anna", "A123", 23)
flight.add_passenger("Mark", "B456", 17)
flight.add_passenger("Kate", "C789", 30)
flight.add_passenger("John", "D111", 12)
 
flight.show_passengers()
 
flight.find_passenger("B456")
flight.find_passenger("X999")
 
print(flight.count_adults())
print(flight.count_children())
 
flight.remove_passenger("C789")
 
flight.show_flight_info()
flight.show_passengers()
```
 
## Run
```bash
python main.py
```
 