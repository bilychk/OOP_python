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

        
    def increase_quantity(self,amount):
        if amount <= 0:
            print(f"Amount has to be positive")
        else:
            self.quntity += amount

        

    def decrease_quantity(self,amount):
        if amount <= 0:
            print(f"Amount has to be positive")
        else:
            self.quntity -= amount
    


    def get_total_value(self):
        return self.price * self.quantity

