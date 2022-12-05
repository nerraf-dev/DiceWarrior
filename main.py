# Dice battle game
# roll a 6 sided die to fight the enemy
# Enemies come in waves, each wave has n rounds
# 

from gameSetup import Player, Enemy
import random

# SETUP Characters

# Enemy(name, health, str, def)
badGuy = Enemy("Pumpkin", 5, 0, 0)
badGuy2 = Enemy("Fly", 5, 1, 0)
enemies = [badGuy, badGuy2]

print(f"""
*******
Enemy:
{badGuy.name} ({badGuy.strength})
******
""")

print("Welcome Player. What should we call you? ")
name = input()
# do some validation here (no blanks, etc)
# Player(name, health, str, def)
player = Player(name, 10, 1, 1)

print(f"""Welcome {player.charType} {player.name}.

You're about to fight. 
You'll probably die, but you might not.
Don't worry. 

Your current health is {player.currentHealth}. If this hits zero...that's it.

Your current strength is {player.strength}. This is how hard you hit...not great right now.

Your defense is {player.defence}. This is your protection...you have...none. Oh.

""")

turnNumber = 0

"""

"""



for enemy in enemies:
  print(f"player {player.name} attacks {enemy.name}")
  while enemy.currentHealth > 0 and player.currentHealth > 0:
    turnNumber += 1
    playerAtk = random.randint(1,6)
    enemyAtk = random.randint(1,6)
    # attackScore = attack - defend
    print(f"Turn {turnNumber} ")
    print(f"Player Rolls: {playerAtk} ")
    print(f"Enemy Rolls: {enemyAtk} ")
    if playerAtk > enemyAtk :
      print("Attack wins") 
      enemy.currentHealth -= player.strength
      if enemy.currentHealth < 1:
        print("You killed it! ")
      print(f"Enemy health: {enemy.currentHealth} ")
    elif enemyAtk > playerAtk:
      print("Enemy wins")
      if enemy.strength > 0:
        player.currentHealth -= enemy.strength
      else:
        print("Lucky! This enemy can't hit!")
      if player.currentHealth < 1:
        print("You're dead! ")
      print(f"Your health: {player.currentHealth} ")
    else:
      print("Draw")
      enemy.currentHealth -= 1
      player.currentHealth -= 1
      print(f"Player health: {player.currentHealth} ")
      print(f"Enemy health: {enemy.currentHealth} ")
  if player.currentHealth < 1:
    print("Enemy WINS!")
  elif enemy.currentHealth < 1:
    print("Player WINS!")
  else:
    print("Probably an error. Something else happened...check it out!")

  input()