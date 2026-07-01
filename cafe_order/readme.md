# Order
 
A simple OOP example: an order class for managing items, prices, and totals.
 
## `Order` class features
 
- `add_item(title, price)` — add an item to the order (price must be positive).
- `remove_item(title)` — remove an item from the order by title.
- `show_order()` — print the customer name and all items in the order.
- `get_total()` — return the total price of the order.
- `most_expensive_item()` — find and print the most expensive item in the order.
## Usage example
 
```python
order = Order("Anna")
order.add_item("Coffee", 4)
order.add_item("Cake", 6)
order.show_order()
print(order.get_total())
order.most_expensive_item()
```
 
## Run
 
```bash
python main.py
```
 