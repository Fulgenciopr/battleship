import time
import random as rand

print('''
    H         H  U         U  NN      N  DDDDDDDDD    IIIIIIIIIII  RRRRRRRRR
    H         H  U         U  N N     N  D        D        I       R        R 
    H         H  U         U  N  N    N  D         D       I       R         R
    HHHHHHHHHHH  U         U  N   N   N  D         D       I       RRRRRRRRRR        
    H         H  U         U  N    N  N  D         D       I       R         R
    H         H  U         U  N     N N  D        D        I       R          R
    H         H  UUUUUUUUUUU  N      NN  DDDDDDDDD    IIIIIIIIIII  R           R
    ''')    
print('''
                                L                   AAA
                                L                  A   A
                                L                 A     A
                                L                A       A
                                L               AAAAAAAAAAA
                                L              A           A
                                LLLLLLLLLLL   A             A
''')                      
print('''
                 FFFFFFFF  L            OOOOOOOOOOO  TTTTTTTTTTTT      AAA 
                 F         L            O         O       T           A   A
                 F         L            O         O       T          A     A
                 FFFFFF    L            O         O       T         A       A
                 F         L            O         O       T        AAAAAAAAAAA
                 F         L            O         O       T       A           A  
                 F         LLLLLLLLLLL  OOOOOOOOOOO       T      A             A 
''')       

print('-----------------------------------------------------------------------------------------------')
time.sleep(3.5)
print('\n'*50)

user_table = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]

bot_table = [
    ['O', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]

game_bot_table = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]

columns_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}



class BotAssignment:

    def bot_ship_assignment(self):

        self.repeated_nums = []
        

        ships_count = sum(row.count('O') for row in bot_table)

        while ships_count < 5:
            bot_row = rand.randint(0, 4)
            bot_col = rand.randint(0, 4)
            ships_count = sum(row.count('O') for row in bot_table)
            if bot_table[bot_row][bot_col] == ' ':
                bot_table[bot_row][bot_col] = 'O'
            

    def enemy_attack(self):
        bot_row = rand.randint(0, 4)
        bot_col = rand.randint(0, 4)
        check_temp = [bot_row, bot_col]

        if check_temp in self.repeated_nums:
            while True:
                bot_row = rand.randint(0, 4)
                bot_col = rand.randint(0, 4)
                check_temp = [bot_row, bot_col]
                if check_temp not in self.repeated_nums:
                    self.repeated_nums.append(check_temp)

                    if user_table[bot_row][bot_col] == 'B':
                        print('COMPUTER HA ACERTADO')
                        user_table[bot_row][bot_col] = 'H'
                    elif user_table[bot_row][bot_col] == ' ':
                        print('COMPUTER HA FALLADO')
                        user_table[bot_row][bot_col] = 'M'
                    
                    break

            
        else:
            self.repeated_nums.append(check_temp)
            if user_table[bot_row][bot_col] == 'B':
                print('COMPUTER HA ACERTADO')
                user_table[bot_row][bot_col] = 'H'
            elif user_table[bot_row][bot_col] == ' ':
                print('COMPUTER HA FALLADO')
                user_table[bot_row][bot_col] = 'M'
            
        


        
            
            

       


                


class UserElection:

    def sink_election(self):
        print('Porfavor, elija fila y columna')
        bot_row = None
        bot_col = None
        while bot_row == None:
            try:
                bot_row = int(input('Elija fila (1-5): '))
                if bot_row < 1 or bot_row > 5:
                    bot_row = None
                    raise Exception()
            except ValueError:
                print('Eso no es un numero, pruebe otra vez!')
            except Exception:
                print('Ese numero esta fuera del rango')
        
        while bot_col == None:
            try:
                bot_col = str(input('Elija columna (A-E): '))
                bot_col = bot_col.upper()
                if bot_col != 'A' and bot_col != 'B' and bot_col != 'C' and bot_col != 'D' and bot_col != 'E':
                    bot_col = None
                    raise Exception
            except Exception:
                print('La letra elegida esta fuera del rango A-E')
        
        
        bot_row -= 1
        bot_col = columns_to_numbers[bot_col]

        

        

        return bot_row, bot_col

    
    def ship_assignment(self, user_ask):
        bot_row, bot_col = user_ask()
        
        if user_table[bot_row][bot_col] == 'B':
            print('Ya hay un barco aqui, escoja otro sitio!')
        else:
            user_table[bot_row][bot_col] = 'B'



    def check_hit(self, user_ask):
        bot_row, bot_col = user_ask()

        if bot_table[bot_row][bot_col] == 'O':
            print('Has acertado!')
            print('\n')
            bot_table[bot_row][bot_col] = 'X'
            game_bot_table[bot_row][bot_col] = 'H'
        elif game_bot_table[bot_row][bot_col] == 'H' or game_bot_table[bot_row][bot_col] == 'W':
            print('Ya has lanzado un misil aqui...')
            print('\n')
        else:
            print('Has dado en agua!')
            print('\n')
            game_bot_table[bot_row][bot_col] = 'W'

      
        

        
        
            

        
        
print('BIENVENIDO A HUNDIR LA FLOTA!')
time.sleep(1)
        


        





enemy = BotAssignment()
enemy.bot_ship_assignment()
for i in bot_table:
    print(i)
player = UserElection()

count_b = sum(row.count('B') for row in user_table)
print('PRIMERO ASIGNE SUS 6 BARCOS DISPONIBLES EN SU TABLERO')

#PERMITE AL JUGADOR PONER SUS SEIS FLOTAS EN EL TABLERO DE JUEGO
while count_b < 6:
    print(f'Barcos restantes: {6-count_b}')
    count_b = sum(row.count('B') for row in user_table)
    player.ship_assignment(player.sink_election)
    count_b += 1
    for line in user_table:
        print(line)

time.sleep(0.5)
    

print('---------------------------------------------')
print('YA HAS ASIGNADO TUS BARCOS')
print('---------------------------------------------')
time.sleep(1)


print('\n'*50)
print('AHORA QUE EMPIEZA LA BATALLA NAVAL!')
print('\n'*50)
time.sleep(1)


count_x = sum(row.count('O') for row in bot_table)
count_b_enemy = sum(row.count('B') for row in user_table)

#PERMITE AL JUGADOR HUNDIR LAS FLOTAS HASTA QUE NO HAYAN MAS
while count_x > 0 and count_b_enemy > 0:
    print('-TURNO DEL JUGADOR-')
    print('\n')
    player.check_hit(player.sink_election)
    count_x = sum(row.count('O') for row in bot_table)
    print('TABLA DEL USUARIO\n')
    for j in user_table:
        print(j)
    print('\n')
    print('TABLA DEL ENEMIGO\n')
    for k in game_bot_table:
        print(k)
        
    
  
    time.sleep(4)
    print('\n'*50)

    print('-TURNO DE COMPUTER-')
    enemy.enemy_attack()
    count_b_enemy = sum(row.count('B') for row in user_table)
    print('TABLA DEL USUARIO\n')
    for j in user_table:
        print(j)
    print('\n')
    print('TABLA DEL ENEMIGO\n')
    for k in game_bot_table:
        print(k)

if count_x == 0:
    print('EL USUARIO GANA!')
elif count_b_enemy == 0: 
    print('COMPUTER GANA!')