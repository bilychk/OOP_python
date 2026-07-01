class Order:
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.item = []


    def add_item(self,title,price):
        if price <= 0:
            print(f"Price can't be negative")
            return
        
        self.item.append([title, price])
        print(f"Item '{title}' was added to the order")



    def remove_item(self,title):
        for item in self.item:
            if item[0] == title:
                self.item.remove(item)
                print(f"Item '{title}' has been deleted")
                return

        print("Item is not found")
        # if title in self.item:
        #     self.item.remove(title)
        #     print(f"This item was removed from your order: {self.title}")
        # else:
        #     print(f"This item is not in your order: {self.title}")



    def show_order(self):
        if len(self.item) == 0:
            print(f"Your order is empty, order something")
        else:
            print(f"Customer name: {self.customer_name}")
            print(f"Order:")
            for item in self.item:
                print(f" {item[0]} and price {item[1]}$")



    def get_total(self):
        total = 0
        for item in self.item:
            total += item[1]
        return total
    

    def most_expensive_item(self):
        if len(self.item) == 0:
            print(f"Your order is empty, order something")
            return
        
        else:
            most_expensive = self.item[0]
            for a in self.item:
                if a[1] > most_expensive[1]:
                    most_expensive = a

            print(f"The most expensive item in your order is: {most_expensive[0]} and price is {most_expensive[1]}$")

    

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
