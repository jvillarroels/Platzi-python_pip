import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    #user_option = input('Piedra, papel o tijera => ').lower()
    user_option = input('Piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Esa opción no es válida')
        # continue
        return None, None
    
    computer_option = random.choice(options)
    
    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('\n')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('\n')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('\n')
            print('Computer wins!')
            computer_wins += 1

    print('\n')
    return user_wins, computer_wins

def check_winners(user_wins, computer_wins):
    if computer_wins == 2:
        print('-' * 39)
        print('COMPUTER WINS THE GAME WITH ', computer_wins, ' POINTS !!!')
        # exit()
        
    if user_wins == 2:
        print('-' * 39)
        print('USER WINS THEN GAME WITH ', user_wins, ' POINTS !!!')
        # exit()
        
    print('-' * 39)
    

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1    
    while True:        
        print('*' * 10)
        print('ROUND: ', rounds)
        print('COMPUTER_WINS: ', computer_wins)
        print('USER_WINS: ', user_wins)
        print('\n')
        rounds += 1
    
        user_option, computer_option = choose_options() 
        user_wins, computer_wins = check_rules(user_option, computer_option,\
                                               user_wins, computer_wins)
        
        check_winners(user_wins, computer_wins)    
        if user_wins == 2 or computer_wins == 2:
            break
    
run_game()

# LECCIÓN 16 - RETO
# Tienda de Tecnología
'''
def message_creator(text):
   # Escribe tu solución 👇
   respuestas = {
      'computadora': 'Con mi computadora puedo programar usando Python',
      'celular': 'En mi celular puedo aprender usando la app de Platzi',
      'cable': '¡Hay un cable en mi bota!'
      }
   if text in respuestas.keys():
      return respuestas[text]   
   else:   
      return 'Artículo no encontrado' 

text = 'computadora'
response = message_creator(text)
print(response)
'''
