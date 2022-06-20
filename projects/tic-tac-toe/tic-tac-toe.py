

board=[' 'for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def spaceIsfree(pos):
    return
def printBoard(board):
    print('   |  |   ')
    print(' '+ board[1]+'|' + board[2]+ ' |' +board[3])
    print('   |  |   ')
    print('----------')
    print('   |  |   ')
    print(' '+ board[4]+'|' + board[5]+ ' |' +board[6])
    print('   |  |   ')
    print('----------')
    print('   |  |   ')
    print(' '+ board[7]+'|' + board[8]+ ' |' +board[9])

def isBoardFull(board):
    if board.count(' ')>1:

        return False
    else:
        return True


def IsWinner(b,l):
    return (b[1]==l and b[2]==l and b[3]==l)or
    (b[4]==l and b[5]==l and b[6]==l) or 
    (b[7]==l and b[8]==l and b[9]==l) or 
    (b[1]==l and b[4]==l and b[7]==l) or 
    (b[2]==l and b[5]==l and b[8]==l) or 
    (b[3]==l and b[6]==l and b[9]==l) or 
    (b[1]==l and b[5]==l and b[9]==l) or 
    (b[3]==l and b[5]==l and b[7]==l) 


