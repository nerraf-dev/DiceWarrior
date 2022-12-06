# Dice battle game
# roll a 6 sided die to fight the enemy
# Enemies come in waves, each wave has n rounds
# 

from gameFunctions import fight
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

# MAIN
  # fight loop
fightNum = 0
for enemy in enemies:
  fightNum += 1
  print(f"Fight number {fightNum}: player {player.name} attacks {enemy.name}\n")
  turnNumber = 0
  playerWin = fight(turnNumber, player, enemy)

  input("Next>>")
if playerWin:
  print("You won")
else:
  print("Game over!")
print("Byeeee!")