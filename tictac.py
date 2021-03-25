board = {1: ' ', 2: ' ', 3: ' ', 
         4: ' ', 5: ' ', 6: ' ', 
         7: ' ', 8: ' ', 9: ' '}


def printboard(board):
    print(board[1]+ '|' + board[2] + '|' +board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' +board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8] + '|' +board[9])
    print("\n")
printboard(board)
def checkDraw():
    for  key in board.keys():
        if board[key]== ' ':
            return False
    return True

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
def terminal(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


    


def spaceIsFree(position):
    if(board[position]==' '):
        return True
    else:
        return False
def insertLetter(letter,position):
    if spaceIsFree(position):
        board[position]=letter
        printboard(board)
        if(checkDraw()):
            print("draw")
            exit()
        if(checkWin()):
            if letter == 'X':
                print("AI wins")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("can't inster here")
        position = int(input("Enter new position: "))
        insertLetter(letter,position)
        return
player = '0'
bot = 'X'
def palyerMove():
    position = int(input("Enter the position for '0':"))
    insertLetter(player, position)
    return

def compMove():
    #position = int(input("Enter the position for 'X':"))
    #insertLetter(bot, position)
    bestScore = -1000
    bestMove=0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score=minimax(board,0,False)
            board[key]=' '
            if(score>bestScore):
                bestScore = score
                bestMove=key
    insertLetter(bot,bestMove)
    return

def minimax(board, depth, isMaximizing):
    if terminal(bot):
        return 100
    elif terminal(player):
        return -100
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if(board[key]==''):
                board[key]=bot
                score-minimax(board,0,False)
                board[key]=' '
                if(score>bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = -800
        for key in board.keys():
            if(board[key]==''):
                board[key]=bot
                score-minimax(board,depth+1,True)
                board[key]=' '
                if(score<bestScore):
                    bestScore = score
        return bestScore
            
while not checkWin():
    compMove()
    palyerMove()