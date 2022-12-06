import time
from gameSetup import clearConsole

introText = [
  """
  You are standing in a strange room. 
  It is dark.
  It is cold.
  """,
  """
  You wonder where you are.
  You can't tell the size of the room.
  Is it a dungeon?
  """,
  """
  You hear a growl.
  Are you in a cave?
  
  """,
  """
  You look down. The floor...isn't stone or rock.
  It's not concrete.
  It has some weird lines...on....wood?
  """,
  """
  It's a gym!
  
  a school gym!!
  """,
  """
  There is a faint glow under a few doors around the edge.
  A flicker of light fills your eyes.
  The gym returns to darkness.
  """,
  """
  There is a low hum floating through the air...

  
  """,
  """
  A deep voice rumbles out...


  """,
  """
  THE VOICE: 
      \"Welcome Player. What should we call you?\"
  You stutter...your mouth is dry...
  """,
]


def intro():
  with open("intro.txt") as file:
    for line in file:
      line = line.replace("\n","")
      line = line.replace("\n","***")
      print(f"{line}")
      
  for item in range(0,len(introText)):
    print(f"""
{"=" * 64}
    
    {introText[item]}
    
{"=" * 28}{item + 1}/{len(introText)}{"=" * 30}

                -- Press ENTER to continue --

    """)
    input()
    clearConsole()
  print("""
  THE VOICE REPEATS: 
      \"Welcome Player. What should we call you?\"

  """)
  name = input(">> ")
  return name

def part2(player):
  introText = [
    f"""
  THE VOICE:
  
      Welcome {player.charType} {player.name}.
    
      You're about to fight. 
      You'll probably die, but you might not.
      Don't worry. 
    
  """,
    """
  Your mind suddenly snaps in to gear!!

  'What?! Fight?? Die?? WORRY?!!'

  """,
    f"""
  THE VOICE:
      \"Your current health is {player.currentHealth}. If this hits zero...that's it.
      
      Your current strength is {player.strength}. This is how hard you hit...not great right now.
      
      Your defense is {player.defence}. This is your protection...you have...none. Oh.\"

  """,
    """
  THE VOICE:
      \"We know what youre thinking
          'What?! Fight?? Die?? WORRY?!!'
          
      and those numbers...what are they?\"

      
  """,
    """
  THE VOICE:
      \"No time....get ready\"


  You are pushed to a door...it opens and in you stumble.

  """,
    """
  You hear something..somethings shuffle across the floor...

  lights begin to flicker on and you see...

  """,
    f"""
      a bunch of old Halloween Pumpkins in November.


      They're wilted, soft, and sad looking. 
    """,
    f"""
      Do you have to 'fight' these?

      You step back...tap a pumpkin...it falls into a mush
      
    """,
    """
      Better get started!!
    """
    
  ]

  clearConsole()
  for item in range(0, len(introText)):
    print(f"""
{"=" * 64}
    
    {introText[item]}
    
{"=" * 28}{item + 1}/{len(introText)}{"=" * 30}

                -- Press ENTER to continue --

    """)
    input()
    clearConsole()
    
  print(F"""
{"=" * 64}
    
   THE VOICE:
      \" - - FIGHT!!! -  - "
    
{"=" * 28}{item + 1}/{len(introText)}{"=" * 30}

                -- Press ENTER to continue --
  
  """)
  input()
  clearConsole()