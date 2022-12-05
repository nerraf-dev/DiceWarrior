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
  charType = "player"

class Enemy(Character):
  def __init__(self, name, health, strength, defence):
    super().__init__(name, health, strength, defence)
    self.currentHealth = health
  charType = "enemy"