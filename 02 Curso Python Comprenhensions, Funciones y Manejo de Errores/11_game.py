import random

def choose_options():
  
  options = ('Piedra', 'Papel', 'Tijera')

  user_option = input('Digite su elección: ')
  computer_option = random.choice(options)
  
  print (' ')
  
  print('User option: ', user_option.capitalize())
  print('Computer option: ', computer_option.capitalize())
  
  print (' ')
  
  user_option = user_option.lower()
  computer_option = computer_option.lower()

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a Tijera')
      print('User ganó')
      user_wins += 1
    else:
      print('Piedra pierde contra Papel')
      print('Computer ganó')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('User ganó')
      user_wins += 1
    else:
      print('Papel pierde contra Tijera')
      print('Computer ganó')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('User ganó')
      user_wins += 1
    else:
      print('Tijera pierde contra Piedra')
      print('Computer ganó')
      computer_wins += 1
  else:
    print('Elección no válida')

  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):

  if computer_wins == 2:
    print (' ')
    print('El ganador es la computadora')
    return True

  if user_wins == 2:
    print (' ')
    print('El ganador es el usuario')
    return True
  
  return False
  
def run_game():

  rounds = 1

  computer_wins = 0
  user_wins = 0
  
  print('')
  print('--------------------------- JUEGO ---------------------------')
  print('Piedra, Papel o Tijera:')

  while True:

    print('-' * 61)
    print('ROUND #', rounds)
    print('-' * 61)

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
    print (' ')
    print('Puntaje Usuario', user_wins)
    print('Puntaje Computadora', computer_wins)

    if check_winner(user_wins, computer_wins):
      break

    rounds += 1

run_game()
