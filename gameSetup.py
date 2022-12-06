import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


diceTypes = {
  "tetrahedron" : 4,
  "cube": 6,
  "Octahedron": 10,
  "Pentagonal trapezohedron": 10,
  "Dodecahedron": 12,
  "Icosahedron": 20
            }

class Character:
  def __init__(self, name, health, strength, defence):
    self.name = name
    self.baseHealth = health
    self.strength = strength
    self.defence = defence
  # charType = ""   # character type/class - what?
  baseHealth = 10
  strength = 1
  defence = 0
  items = []

class Player(Character):
  def __init__(self, name, health, strength, defence):
    super().__init__(name, health, strength, defence)
    self.currentHealth = health
    self.dice = [[1,6]]# SETUP Characters
  charType = "player"
  

class Enemy(Character):
  def __init__(self, name, health, strength, defence, diceHigh):
    super().__init__(name, health, strength, defence)
    self.currentHealth = health
    self.dice = [[1,diceHigh]]# SETUP Characters
  charType = "enemy"


def setupEnemies():
   
# Enemy("Halloween Pumpkin in November", 5, 0, 0, 2)
# Enemy(name, health, str, def)
  pumpkin = Enemy("Pumpkin", 5, 0, 0, 4)
  badGuy2 = Enemy("Fly", 5, 1, 0, 4)
  enemies = [pumpkin, badGuy2, Enemy("Fly", 5, 1, 0, 4)]
  return enemies