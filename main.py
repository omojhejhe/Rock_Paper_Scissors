import random

input("Welcome to ROCK, PAPER, SCISSORS Game! Press ENTER to start.")
print()
PLAYER_wins = 0
CPU_wins = 0

choices = ["r", "p", "s"]

while True:
  random_index = random.randint(0,2)
  CPU_choice = choices[random_index]

  PLAYER_choice = input("R for Rock, P for Paper, or S for Scissors? ").lower()
  while PLAYER_choice not in choices:
    PLAYER_choice = input("That is not a valid choice. Please try again: ").lower()
  
  print()
  print("PLAYER choice:", PLAYER_choice)
  print("CPU's choice:", CPU_choice)
  print()

  if PLAYER_choice == 'r':
    if CPU_choice == 'r':
      print("It's a tie!")
    elif CPU_choice == 's':
      print("You win!")
      PLAYER_wins+=1
    elif CPU_choice == 'p':
      print("You lose!")
      CPU_wins+=1
  elif PLAYER_choice == 'p':
    if CPU_choice == 'p':
      print("It's a tie!")
    elif CPU_choice == 'r':
      print("You win!")
      PLAYER_wins+=1
    elif CPU_choice == 's':
      print("You lose!")
      CPU_wins+=1
  elif PLAYER_choice == 's':
    if CPU_choice == 's':
      print("It's a tie!")
    elif CPU_choice == 'p':
      print("You win!")
      PLAYER_wins+=1
    elif CPU_choice == 'r':
      print("You lose!")
      CPU_wins+=1

  print()
  print("You have "+str(PLAYER_wins)+" wins")
  print("The computer has "+str(CPU_wins)+" wins")
  print()

  repeat = input("Play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("That is not a valid choice. Please try again: ").lower()
  
  if repeat == 'n':
    break

  print("\n----------------------------\n")