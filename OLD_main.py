#create a 2 player battle game
# each player rolls a 6 sided die
# player 1 attacks, player 2 defends
# the higher score wins. If the attacker wins the score is deducted from the defenders health 
# if the defender wins the score stay the same. 


import random

players = ["One", "Two"]
playerHealth = [10,10]
turnNumber = 0

currentPlayer = 0

attackHealth = 10
defendHealth = 10


# Get current player 

print(f"player {currentPlayer + 1}: {players[currentPlayer]} attacks")

while playerHealth[currentPlayer] > 0:
  turnNumber += 1
  attack = random.randint(1,6)
  defend = random.randint(1,6)

  print(f"Turn {turnNumber} ")
  
  print(f"Attack: {attack} ")
  print(f"Defend: {defend} ")
  if attack > defend :
    print("Attack wins") 
    playerHealth[currentPlayer] -= attack - defend
    if playerHealth[currentPlayer] < 1:
      print("You died! ")
    print(f"Defend health: {playerHealth[currentPlayer]} ")
  elif defend > attack:
    print("Defend wins")
  else:
    print("Draw")
    playerHealth[currentPlayer] -= 1
    print(f"Defend health: {playerHealth[currentPlayer]} ")