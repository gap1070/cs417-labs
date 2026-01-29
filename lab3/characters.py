class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack_description(self):
        return f"attacks with {self.name} for {self.damage} damage"

class Character:
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
        self.weapon = None

    def __str__(self):
        return f"I am {self.name}, a {self.__class__.__name__}"

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack_description()}!"
        return f"{self.name} attacks with bare hands for 5 damage!"

    def get_status(self):
        weapon_info = self.weapon.name if self.weapon else "unarmed"
        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"

    def summon_power(self):
        raise NotImplementedError("Subclasses must implement summon_power()")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Berserker Rage")

    def summon_power(self):
        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Arcane Blast")

    def summon_power(self):
        return f"{self.name} channels {self.special_power}! Enemies are stunned!"
    
# Create a Character Subclass    
class Ranger(Character):
    def _init__(self, name):
        super().__init__(name, "Animal Partner")

    def summon_power(self):
        return f"{self.name} calls for his {self.special_power}! A wolf who helps him in battle!"

# Create weapons 
crossbow = Weapon("Rapid Crossbow", 15)
dagger = Weapon("Battle Dagger", 18)
sword = Weapon("Prestige Sword", 25)

# Build an army
army = [
    Warrior("Thorfin"), 
    Mage("Gandalf"),
    Ranger("Hercules")
]

# equip each character with a specific weapon 
army[0].eqiup_weapon(sword)             # Warrior gets a sword
army[1].equid_weapon(crossbow)          # Mage gets a crossbow
army[2].equip_weapon(dagger)            # Ranger gets a dagger

print("My Army")
for character in army:
    print(character)
    print(character.get_status())
    print(character.summon_power())
    print()

# weapon swapping demo
print("Weapon Swap Demo")
# takes the warrior, Thorfin, and swaps weapons 
demo_character = army[0]

# original weapon 
demo_character.equip_weapon(sword)
print(demo_character.attack())

# swap from sword to a dagger 
demo_character.equip_weapon(dagger)
print(demo_character.attack())

# Reflection Comment
# Equipment is modeled as composition instead of inheritance 
# because characters are able to change weapons way more efficiently. 
# Using inheritance would have it so you had to create seperate classes 
# for every single weapon and character combination. 
# Which leaves you with alot of classes, which is so unnessessary if you 
# just use composition. Composition allows you to be way more flexable with it, 
# since a character is allowed to equip, unequip, or swap their weapons, 
# without having to make seperate classes. Which just makes your code way more maintainable. 