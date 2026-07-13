# Electronics Store — Warehouse Management System
 
A console-based warehouse management system for an electronics store, built in Python using Object-Oriented Programming principles.
 
## Description
 
This project simulates the day-to-day operations of an electronics store's warehouse: managing stock, processing sales, and generating reports — all through a simple text-based menu.
 
## Features
 
- Add new products to the warehouse
- Remove products from the warehouse
- Search for a product by ID
- Update product quantity (restock)
- Sell products (with stock validation)
- Display all products currently in stock
- Calculate the total value of the inventory
- Display products with low stock
- Track a full history of sales
- Generate a sales report (total items sold, total revenue)
## Project Structure
 
The project is built around 4 core classes:
 
### `Product`
Represents a single item in the warehouse.
- **Attributes:** `product_id`, `title`, `category`, `price`, `quantity`
- **Methods:** `show_info()`, `increase_quantity()`, `decrease_quantity()`, `get_total_value()`
### `Inventory`
Manages the full collection of `Product` objects.
- **Attributes:** `products` (list of `Product` objects)
- **Methods:** `add_product()`, `remove_product()`, `find_product_by_id()`, `find_products_by_category()`, `show_all_products()`, `show_low_stock_products()`, `get_inventory_total_value()`, `update_product_quantity()`, `sell_product()`
### `Sale`
Represents a single completed sale (a receipt).
- **Attributes:** `sale_id`, `product_id`, `product_title`, `quantity`, `total_price`
- **Methods:** `show_info()`
### `StoreSystem`
The main system that connects `Inventory` and `Sale` together, and runs the console menu.
- **Attributes:** `inventory` (an `Inventory` object), `sales` (list of `Sale` objects)
- **Methods:** `sell_product()`, `show_sales_history()`, `show_sales_report()`, plus delegate methods for all inventory operations, and `run()` for the interactive menu
## How It Works
 
`StoreSystem` doesn't manage products or sales directly — it delegates that work to `Inventory` and `Sale` objects. For example, when a sale happens:
 
1. `StoreSystem` asks `Inventory` to find and sell the product.
2. If the sale succeeds, `StoreSystem` creates a new `Sale` object and stores it in the sales history.
3. Later, `show_sales_report()` loops through all `Sale` objects to build a summary.
This demonstrates object interaction: separate classes with clear responsibilities working together rather than one class doing everything.
 
## How to Run
 
```bash
python3 main.py
```
 
Then follow the on-screen menu with multiple choices to manage the warehouse.
 