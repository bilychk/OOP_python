# Order
 
An order class for managing items in a customer's order, with adding, removing, totaling, and finding the priciest item.
 
## `Order` class methods
- `add_item(title, price)` — add an item to the order; rejected if the price is zero or negative.
- `remove_item(title)` — remove an item by title; prints a message if no matching title is found.
- `show_order()` — print the customer's name and the full list of items with their prices, or a message that the order is empty.
- `get_total()` — return the sum of the prices of all items in the order.
- `most_expensive_item()` — print the item with the highest price in the order, or a message that the order is empty.
## Usage example
```python
order = Order("Anna")
 
order.add_item("Coffee", 4)
order.add_item("Cake", 6)
order.add_item("Tea", 3)
order.add_item("Sandwich", -2)
 
order.show_order()
print("---------------------")
 
print(order.get_total())
print("---------------------")
 
order.most_expensive_item()
 
order.remove_item("Tea")
order.remove_item("Pizza")
```
 
## Run
```bash
python main.py
```
 
 