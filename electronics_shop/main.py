class Product:
    def __init__(self,product_id,title,category,price,quantity):
        self.product_id = product_id
        self.title = title
        self.category = category
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Title: {self.title}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
        print(f"Amount: {self.quantity}")
        print(f"Total amount: {self.get_total_value()}")
        print("--------------------------")

        
    def increase_quantity(self,amount):
        if amount <= 0:
            print(f"Amount has to be positive")
        else:
            self.quantity += amount

        

    def decrease_quantity(self,amount):
        if amount <= 0:
            print(f"Amount has to be positive")
        else:
            self.quantity -= amount
    


    def get_total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        existing = self.find_product_by_id(product.product_id)
        if existing is not None:
            print(f"This product ID is already existing")
            return False
        

        self.products.append(product)

    def remove_product(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product with id {product_id} is deleted")
                return True
        print(f"Product with id {product_id} is not found")
        return False

    def find_product_by_id(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
        

    def find_products_by_category(self,category):
        result = []
        for product in self.products:
            if product.category == category:
                result.append(product)
        return result

    def show_all_products(self):
        if len(self.products) == 0:
            print("The Inventory is empry at the moment")
        else:
            for product in self.products:
                product.show_info()
    
    def show_low_stock_products(self,limit):
        for product in self.products:
            if product.quantity <= limit:
                print(f"Small amount: {product.title} only {product.quantity} left")
    
    def get_inventory_total_value(self):
        total = 0
        for product in self.products:
            total += product.get_total_value()
        return total

    def update_product_quantity(self,product_id,amount):
        product = self.find_product_by_id(product_id)
        if product is None:
            print("Product is not found")
            return False
        product.increase_quantity(amount)
        return True
    
    def sell_product(self,product_id,amount):
        product = self.find_product_by_id(product_id)
        if product is None:
            print(f"Product is not found")
            return False
        
        if product.quantity < amount:
            print(f"There is no {amount} left in stock, only {product.quantity} is left")
            return False
        product.decrease_quantity(amount)
        print(f"Succesfuly sold {amount} of {product.title} product")
        return True
    

class Sale:
    def __init__(self, sale_id, product_id,product_title,quantity,total_price):
        self.sale_id = sale_id
        self.product_id = product_id
        self.product_title = product_title
        self.quantity = quantity
        self.total_price = total_price

    def show_info(self):
        print(f"Sale ID: {self.sale_id}")
        print(f"Product ID: {self.product_id}")
        print(f"Product title: {self.product_title}")
        print(f"Quantity sold: {self.quantity}")
        print(f"Total price: {self.total_price}")


class StoreSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.sales = [] #Sale history
        self.sale_id = 1

    def add_product_to_inventory(self,product):
        self.inventory.add_product(product)
        
    def remove_product_from_inventory(self,product_id):
        self.inventory.remove_product(product_id)
        
    def show_products(self):
        self.inventory.show_all_products()
        
    def search_product(self,product_id):
        product = self.inventory.find_product_by_id(product_id)
        if product is None:
            print(f"Product is not found")
        else:
            product.show_info()
        return product


    def sell_product(self, product_id, amount):
        product = self.inventory.find_product_by_id(product_id)
        if product is None:
            print(f"Product is not found")
            return False
        
        price_unit = product.price
        success = self.inventory.sell_product(product_id, amount)

        if success:
            total_price = price_unit * amount
            new_sale = Sale(self.sale_id, product_id, product.title, amount, total_price)
            self.sales.append(new_sale)
            self.sale_id +=1

        return success


    def show_sales_history(self):
        if len(self.sales) == 0:
            print(f"There is no sales at the moment")
        else:
            for sale in self.sales:
                sale.show_info()
                print("-------")

    def show_sales_report(self):
        if len(self.sales) == 0:
            print(f"There is no sales at the moment")
            return

        revenue = 0
        items_sold = 0

        for sale in self.sales:
            sale.show_info()
            print("-" * 20)
            revenue += sale.total_price
            items_sold += sale.quantity

        print(f"All sales: {len(self.sales)}")
        print(f"Amount of products sold (pcs): {items_sold}")
        print(f"Total revenue: {revenue}")


    def show_low_stock(self,limit):
        self.inventory.show_low_stock_products(limit)

    def show_inventory_value(self):
        total  = self.inventory.get_inventory_total_value()
        print(f"Inventory total price: {total}")

    def run(self):
        while True:
            print("\n----- Electronics Shop Menu -----")
            print("1. Add product")
            print("2. Remove product")
            print("3. Show all products")
            print("4. Search product by ID")
            print("5. Restock product")
            print("6. Sell product")
            print("7. Show total inventory value")
            print("8. Show low stock products")
            print("9. Show sales history")
            print("10. Show sales report")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print(f"----Add product function----")
                product_id = int(input("Product ID: "))
                title = input("Title: ")
                category = input("Category: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                new_product = Product(product_id, title, category, price, quantity)
                self.add_product_to_inventory(new_product)

            elif choice == "2":
                product_id = int(input("Product ID to remove: "))
                self.remove_product_from_inventory(product_id)

            elif choice == "3":
                self.show_products()

            elif choice == "4":
                product_id = int(input("Product ID to search: "))
                self.search_product(product_id)

            elif choice == "5":
                product_id = int(input("Product ID to restock: "))
                amount = int(input("Amount to add: "))
                self.inventory.update_product_quantity(product_id, amount)

            elif choice == "6":
                product_id = int(input("Product ID to sell: "))
                amount = int(input("Amount to sell: "))
                self.sell_product(product_id, amount)
            
            elif choice == "7":
                self.show_inventory_value()

            elif choice == "8":
                limit = int(input("Show products with quantity below: "))
                self.show_low_stock(limit)

            elif choice == "9":
                self.show_sales_history()

            elif choice == "10":
                self.show_sales_report()

            elif choice == "0":
                print("Bye bye!")
                break

            else:
                print("Wrong choice, try again")



if __name__ == "__main__":
    store = StoreSystem()
    store.run()
