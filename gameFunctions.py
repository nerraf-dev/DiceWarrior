import random, time
def fight(turnNumber, player,  enemy):
  playerWin = False
  
  
  while enemy.currentHealth > 0 and player.currentHealth > 0:
    turnNumber += 1
    
    # result = fight(turnNumber, enemy)

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
  return playerWin