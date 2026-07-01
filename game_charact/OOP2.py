class GameCharacter:
    def __init__(self,name,health,level):
        self.name = name
        self.health = health
        self.level = level
        self.inventory = []
    


    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Level: {self.level}")
        print(f"Inventory: {self.inventory}")



    def take_damage(self, damage):
        if damage < 0:
            print("Damage has to be positive")
            return
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and now has {self.health} health")




    def heal(self, amount):
        if amount <= 0:
            print("Healing amount has to be positive")
            return
        self.health += amount
        print(f"{self.name} healed {amount} and now has {self.health} health")




    def level_up(self):
        self.level += 1
        print(f"{self.name} Yay! new level is:  {self.level}")




    def add_item(self, item):
        self.inventory.append(item) 
        print(f"The item: {item} has been added to {self.name} inventory")



    def remove_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"The item: {item} has been removed from {self.name} inventory")
        else:
            print(f"The item: {item} is not in {self.name} inventory. Try again")



    def show_inventory(self):
        if len(self.inventory) == 0:
            print(f"The player {self.name} inventory is empty")
        else:
            print(f"The player {self.name} inventory: {self.inventory}")



hero = GameCharacter("Knight", 100, 1)

hero.show_info()
hero.take_damage(30)
hero.heal(20)
hero.level_up()
hero.add_item("Sword")
hero.add_item("Shield")
hero.add_item("Potion")

hero.show_inventory()  

hero.remove_item("Potion")
hero.remove_item("Bow")

hero.show_info()
hero.show_inventory()


print("-----------------------")

hero2 = GameCharacter("Creeper", 85, 2)

hero2.show_info()
hero2.take_damage(30)
hero2.heal(20)
hero2.level_up()
hero2.add_item("Sword")
hero2.add_item("Shield")
hero2.add_item("Potion")

hero2.show_inventory()  

hero2.remove_item("Potion")
hero2.remove_item("Bow")

hero2.show_info()
hero2.show_inventory()