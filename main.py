# Dice battle game
# roll a 6 sided die to fight the enemy
# Enemies come in waves, each wave has n rounds
# 

from gameFunctions import fight
from gameSetup import Player, Enemy, diceTypes, clearConsole, setupEnemies
import random, time, os, intro

playerWin = False
play = True
# SETUP Characters
# enemies = setupEnemies()
# # *** INTRO ***
# name = intro.intro()
# # do some validation here (no blanks, etc)
# # Player(name, health, str, def, )
# player = Player(name, 10, 1, 1)
# intro.part2(player)
# time.sleep(0.5)

# TESTING: uncomment 13 - 20
player = Player('Bob', 10, 1, 1)


# MAIN
  # fight loop
fightNum = 0
wave = 0

while play:
  wave += 1
  enemies = setupEnemies()
  print(f"""    Get ready player {player.name}.
  *** Wave {wave} - START! ***""")

  print(f"""{enemies}""")
  for i in range(0, len(enemies)):
    enemy = enemies[i]
  # for enemy in enemies:
    fightNum += 1
    print(f"Fight number {fightNum}: player {player.name} attacks {enemy.name}\n")
    turnNumber = 0
    playerWin = fight(turnNumber, player, enemy)
    if playerWin and i != len(enemies):
      input("Next>>")
    elif playerWin == False:
      print(f"You died on wave {wave}")
  if playerWin:
    print("You beat the wave!")
  else:
    print("Game over!")
    print(f"You completed {wave -1} wave(s)")
    play = False
  print("Byeeee!")