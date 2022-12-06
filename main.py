# Dice battle game
# roll a 6 sided die to fight the enemy
# Enemies come in waves, each wave has n rounds
# 

from gameSetup import Player, Enemy, diceTypes, clearConsole
import random, time, os, intro

playerWin = False
# SETUP Characters

# Enemy(name, health, str, def, diceHigh)
badGuy = Enemy("Halloween Pumpkin in November", 5, 0, 0, 2)
badGuy2 = Enemy("Fly", 5, 1, 0, 4)
enemies = [badGuy, badGuy2, Enemy("Fly", 5, 1, 0, 4)]

# *** INTRO ***

name = intro.intro()
# do some validation here (no blanks, etc)
# Player(name, health, str, def, )
player = Player(name, 10, 1, 1)
intro.part2(player)


time.sleep(0.5)

for enemy in enemies:
  playerWin = False
  turnNumber = 0
  print(f"player {player.name} attacks {enemy.name}\n")
  while enemy.currentHealth > 0 and player.currentHealth > 0:
    turnNumber += 1
    
    playerAtk = random.randint(player.dice[0][0], player.dice[0][1])
    enemyAtk = random.randint(enemy.dice[0][0], enemy.dice[0][1])
    # attackScore = attack - defend
    print(f"Turn {turnNumber} ")
    print(f"Player Rolls: {playerAtk} ")
    print(f"Enemy Rolls: {enemyAtk} ")
    if playerAtk > enemyAtk :
      print("Attack wins") 
      enemy.currentHealth -= player.strength
      if enemy.currentHealth < 1:
        print("You killed it! ")
      # print(f"Enemy health: {enemy.currentHealth} ")
    elif enemyAtk > playerAtk:
      print("Enemy wins")
      if enemy.strength > 0:
        player.currentHealth -= enemy.strength
      else:
        print("Lucky! This enemy can't hit!")
      if player.currentHealth < 1:
        print("You're dead! ")
      # print(f"Your health: {player.currentHealth} ")
    else:
      print("Draw")
      enemy.currentHealth -= 1
      player.currentHealth -= 1
    print(f"Player health: {player.currentHealth} ")
    print(f"Enemy health: {enemy.currentHealth} ")
    print()
    time.sleep(1)
  if player.currentHealth < 1:
    print("Enemy WINS!")
  elif enemy.currentHealth < 1:
    print("Player WINS!")
    playerWin = True
  else:
    print("Probably an error. Something else happened...check it out!")

  input("Next>>")
if playerWin:
  print("You won")
else:
  print("Game over!")
print("Byeeee!")