# Game Character
 
A game character class with health, level, and inventory.
 
## `GameCharacter` class methods
- `show_info()` — print the character's name, health, level, and inventory.
- `take_damage(damage)` — reduce health by the given amount; rejected if the amount is negative, and health won't drop below 0.
- `heal(amount)` — restore health by the given amount; rejected if the amount is zero or negative.
- `level_up()` — increase the character's level by 1.
- `add_item(item)` — add an item to the inventory.
- `remove_item(item)` — remove an item from the inventory if it's present, otherwise print a message that it wasn't found.
- `show_inventory()` — print the inventory contents, or a message that it's empty.
## Usage example
```python
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
```
 
## Run
```bash
python main.py
```
