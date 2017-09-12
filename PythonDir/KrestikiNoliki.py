X = 'X'
O = 'O'
empty = ' '
TIE = 'Ничья'
SQUAR_NUMBER = 9
def hello():
    print("Преветствую тебя, Человек!")
    print("Это Игра - Крестики-нолики")
    print('''
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
''')
    print("Да начнется игра!")

def first_yes_no(question):
    answer = None
    while answer not in ('y','n'):
        answer = input(question).lower()
    return answer

def pieces(response):
    go_first = first_yes_no('Будешь первым ходить? (y/n): ')
    if go_first == 'y':
        human = X
        computer = O
    else:
        human = O
        computer = X
    return human, computer

def new_board(moved):
    board = []
    for square in range(SQUAR_NUMBER):
        board.append(empty)
    return board

def display_board(board):
    '''Отображает доску на экране'''
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8])

def legal_moves(board):
    moves = []
    for square in SQUAR_NUMBER:
        if board[square] == empty:
            moves.append(square)
    return moves

def ask_number(question, low, high):
    '''Просит ввести число из диапазона'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def winner(board):
    '''пути к победе'''
    WAYS_TO_WIN = ((0,1,2),(3,4,5),
            (6,7,8),(0,3,6),(1,4,7),
            (2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
        elif empty not in board:
            return TIE
        else: return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Твой ход. Выбери одно из полей (0-8):', 0, SQUAR_NUMBER)
        if move not in legal:
            print('\nЭто поле уже занято. Выбери другое.\n')
    print('ладно')
    return move

def computer_move(board, computer, human):
    '''Делате ход за компьютерного противника'''
    board = board[:]
    legal = legal_moves(board)
    move = None
    WAYS_TO_WIN = ((0,1,2),(3,4,5),
            (6,7,8),(0,3,6),(1,4,7),
            (2,5,8),(0,4,8),(2,4,6))
    for way in WAYS_TO_WIN:
        if board[way[0]] == board[way[1]] and board[way[2]] == empty:
            board[way[2]] = computer
            move = board[way[2]]
            print(move)
            break
        elif board[way[0]] == board[way[2]] and board[way[1] == empty:
            board[way[1]] = computer
            move = board[way[1]]
            print(move)
            break
        elif board[way[1]] == board[way[2]] and board[way[0] == empty:
            board[way[0]] = computer
            move = board[way[0]]
            print(move)
            break
        elif board[way[0]] == computer and board[way[1]] == board[way[2]] == empty:
            board[way[2]] = computer
            move = board[way[2]]
            print(move)
            break
        elif board[way[1]] == computer and board[way[0]] == board[way[2]] == empty:
            board[way[0]] = computer
            move = board[way[0]]
            print(move)
            break
        elif board[way[2]] == computer and board[way[0]] == board[way[1]] == empty:
            board[way[0]] = computer
            move = board[way[0]]
            print(move)
            break
        elif board[way[0]] == board[way[1]] == board[way[2]] == empty:
            board[way[1]] = computer
            move = board[way[1]]
            print(move)
            break
    
            
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner,computer, human):
    if the_winner != TIE:
        print('Три', the_winner, 'в ряд\n')
    else:
        print('Ничья')
    if the_winner == computer:
        print('компьютер победил')
    elif the_winner == human:
        print('Победил человек')
    elif the_winner == TIE:
        print('Ничья, сынок')

def main():
    hello()
    computer, human = pieces()
    turn = X
    board = new_board
    while not winner(board):
        if turn == human:
            move = human_move(board,computer,human)
            board[move] = computer
        display_board()
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

#Запуск программы
main()
