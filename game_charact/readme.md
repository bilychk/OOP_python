# Game Character
 
A simple OOP example: a game character class with health, level, and inventory.
 
## `GameCharacter` class features
 
- `show_info()` — print the character's name, health, level, and inventory.
- `take_damage(damage)` — reduce health by the given amount (won't go below 0).
- `heal(amount)` — restore health.
- `level_up()` — increase the character's level.
- `add_item(item)` — add an item to the inventory.
- `remove_item(item)` — remove an item from the inventory (if present).
- `show_inventory()` — display the inventory contents.
## Usage example
 
```python
hero = GameCharacter("Knight", 100, 1)
hero.take_damage(30)
hero.heal(20)
hero.level_up()
hero.add_item("Sword")
hero.show_inventory()
```
 
## Run
 
```bash
python main.py
```
 