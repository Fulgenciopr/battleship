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


#INSTANTIATES A ENEMY WHICH AUTO ASSIGNS AND ATTACK BOTH SHIPS AND PLAYER
class BotAssignment:

    #ASSIGNS AUTOMATICALY SHIPS INSIDE THE TABLE
    def bot_ship_assignment(self):

        self.repeated_nums = []
        

        ships_count = sum(row.count('O') for row in bot_table)

        while ships_count < 5:
            bot_row = rand.randint(0, 4)
            bot_col = rand.randint(0, 4)
            ships_count = sum(row.count('O') for row in bot_table)
            if bot_table[bot_row][bot_col] == ' ':
                bot_table[bot_row][bot_col] = 'O'
            

    #ATTACKS DIFFERENT COORDINATES RANDOMLY AND DOES NOT REPEAT ANY COORDINATES
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
                        print('COMPUTER MADE A HIT!')
                        user_table[bot_row][bot_col] = 'H'
                    elif user_table[bot_row][bot_col] == ' ':
                        print('COMPUTER HAS MISSED')
                        user_table[bot_row][bot_col] = 'M'
                    
                    break

            
        else:
            self.repeated_nums.append(check_temp)
            if user_table[bot_row][bot_col] == 'B':
                print('COMPUTER MADE A HIT!')
                user_table[bot_row][bot_col] = 'H'
            elif user_table[bot_row][bot_col] == ' ':
                print('COMPUTER HAS MISSED')
                user_table[bot_row][bot_col] = 'M'
            
        


        
            
            

       


                

#INSTATIATES A INSTANCE OF THE PLAYER
class UserElection:
    
    #METHOD THAT ASKS THE PLAYER FOR ROW AND COLUMN
    def sink_election(self):
        print('PLEASE, SELECT LINE AND COLUMN')
        bot_row = None
        bot_col = None
        while bot_row == None:
            try:
                bot_row = int(input('SELECT LINE (1-5): '))
                if bot_row < 1 or bot_row > 5:
                    bot_row = None
                    raise Exception()
            except ValueError:
                print('THAT IS NOT A NUMBER, TRY AGAIN!!')
            except Exception:
                print('THAT NUMBER IS OUT OF RANGE!')
        
        while bot_col == None:
            try:
                bot_col = str(input('SELECT A COLUMN (A-E): '))
                bot_col = bot_col.upper()
                if bot_col != 'A' and bot_col != 'B' and bot_col != 'C' and bot_col != 'D' and bot_col != 'E':
                    bot_col = None
                    raise Exception
            except Exception:
                print('THE SELECTED LETTER IS OUT OF THE RANGE (A-E)')
        
        
        bot_row -= 1
        bot_col = columns_to_numbers[bot_col]

        

        

        return bot_row, bot_col

    
    #ACCESES SINK_ELECTION METHOD AND ASKS FOR PLACEMENT OF PLAYER'S SHIPS
    def ship_assignment(self, user_ask):
        bot_row, bot_col = user_ask()
        
        if user_table[bot_row][bot_col] == 'B':
            print('THERE IS ALREADY A SHIP HERE, CHOOSE ANOTHER SPOT!!')
            while user_table[bot_row][bot_col] == 'B': 
                bot_row, bot_col = user_ask()
            user_table[bot_row][bot_col] = 'B'

            
        else:
            user_table[bot_row][bot_col] = 'B'


    #CHECKS IF USER HAS HIT A ENEMY'S SHIP
    def check_hit(self, user_ask):
        bot_row, bot_col = user_ask()

        if bot_table[bot_row][bot_col] == 'O':
            print('YOU MADE A HIT!!')
            print('\n')
            bot_table[bot_row][bot_col] = 'X'
            game_bot_table[bot_row][bot_col] = 'H'
        elif game_bot_table[bot_row][bot_col] == 'H' or game_bot_table[bot_row][bot_col] == 'W':
            print('YOU ALREADY HAVE THROWN AN ATTACK HERE ...')
            print('\n')
        else:
            print('YOU HITTED WATER!')
            print('\n')
            game_bot_table[bot_row][bot_col] = 'W'

      
        

        
        
            

        
        
print('WELCOME TO BATTLESHIP!')
time.sleep(1)
        


        




#INSTANTIATES THE ENEMY INSTANCE
enemy = BotAssignment()
enemy.bot_ship_assignment()

#INSTATIATES THE PLAYER INSTANCE
player = UserElection()

count_b = sum(row.count('B') for row in user_table)
print('FIRST, ASSIGN YOUR 6 AVAILABLE SHIPS ON THE BOARD')

#CHECKS THE AMAOUNT OF SHIPS THE PLAYER HAS LOCATED AND CHECKS THAT THE 6 SHIP LIMIT HASN'T BEEN SURPASED
while count_b < 6:
    print(f'SHIPS REMAINING: {6-count_b}')
    count_b = sum(row.count('B') for row in user_table)
    player.ship_assignment(player.sink_election)
    count_b += 1
    for line in user_table:
        print(line)

time.sleep(0.5)
    

print('---------------------------------------------')
print('YOU HAVE ASSIGNED YOUR SHIPS SUCCESSFULY')
print('---------------------------------------------')
time.sleep(1)


print('\n'*50)
print('NOW, MAY THE BATTLESHIP BEGIN!!')
print('\n'*50)
time.sleep(1)


count_x = sum(row.count('O') for row in bot_table)
count_b_enemy = sum(row.count('B') for row in user_table)

#CHECKS CONSTANTLY HOW MANY SHIPS DOES PLAYER AND ENEMY HAVE REMAINING
while count_x > 0 and count_b_enemy > 0:
    print("-PLAYER'S TURN-")
    print('\n')
    player.check_hit(player.sink_election)
    count_x = sum(row.count('O') for row in bot_table)
    print("PLAYER'S BOARD\n")
    for j in user_table:
        print(j)
    print('\n')
    print("ENEMY'S BOARD\n")
    for k in game_bot_table:
        print(k)
        
    
  
    time.sleep(4)
    print('\n'*50)

    print("ENEMY'S TURN")
    enemy.enemy_attack()
    count_b_enemy = sum(row.count('B') for row in user_table)
    print("PLAYER'S BOARD\n")
    for j in user_table:
        print(j)
    print('\n')
    print("ENEMY'S BOARD\n")
    for k in game_bot_table:
        print(k)

if count_x == 0:
    print('PLAYER TAKES THE WIN!')
elif count_b_enemy == 0: 
    print('COMPUTER WINS!')