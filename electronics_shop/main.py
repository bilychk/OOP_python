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

            


