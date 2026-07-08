


import time


class Character:
      def __init__(self, name, health, level):
          self.name = name
          self.health = health
          self.level = level
          
      def introduce(self):
          print(f"Name: {self.name}, Health: {self.health}HP, Level: {self.level}")
          
      def heal(self, amount):
          self.health = self.health + amount
          print(f"Health restored of {self.name}: {self.health}HP")
          
      def take_damage(self, amount):
          self.health = self.health - amount
          print(f"Damage taken by {self.name}: {self.health}HP remaining")
          
      def level_up(self):
          self.level = self.level + 1
          print(f"{self.name} has Leveled up: {self.level}lvl")
          
      def show_health(self):
          print(f"{self.name}'s Health: {self.health}")

character1 = Character("Aayush", 100, 50)
character2 = Character("Kim", 1000, 1000)

character1.introduce()
time.sleep(1)
character2.introduce()
time.sleep(1)
character2.heal(100)
#
character1.take_damage(99)
character1.heal(90)
time.sleep(1)
#
character1.level_up()
time.sleep(1)
character2.level_up()


