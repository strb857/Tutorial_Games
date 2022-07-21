#Reversi
import random
import sys
WIDTH = 8 #Board dimentions
HEIGHT = 8
def drawBoard(board):
    #Return None - draws the boars as passed in "board"
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    #Returns blank board - Create blank board data structure
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    #Return False if player move on xstart, ystart is invalid.
    #If move is valid, Return list of coordinates that becomes the players. 
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection #First step in the x-direction
        y += ydirection #First step in the y-direction
        while isOnBoard(x, y) and board[x][y] == otherTile:
            #keep moving in this x/y-direction
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                #There are pieces to flip. Go in reverse direction until original space, noting all tiles along the way.
                while True:
                    x -= xdirection
                    y-= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: #if no tiles are flipped, this is not a valid move.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    #Return True if coordinates is on the game board
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
    #Return a new board periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    #Retrun a list of [x, y] lists of valid moves for the given player on the given board
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    #Determine the score by counting the tiles. Return a Dictionary with keys 'X' and 'O'
    xscore = 0
    yscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'Y':
                yscore += 1
    return {'X':xscore, 'Y':yscore}

def enterPlayerTile():
    #Let player enter which tile they want to play
    #Retruns a list with the players tile as the first item and the comuters as the second
    tile = ''
    while not (tile == 'X' or tile == '0'):
        print('Do you want to be X or O?')
        tile = input().upper()
    
    #The first element in the list is the players tile and the second is the computers tile
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #randomly choose who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    #Place the tile on the board at xstart and ystart and flip any of opponents pieces.
    #Return False if this is an invalid move, True if Valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    #Return a duplicate of the board list
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in (HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy

def isOnCorner(x, y):
    #return True if the position is in one of the four corners
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getplayerMove(board, playerTile):
    # Let player enter move
    # Return the move as [x, y] (or return the strings 'hints' or 'quit')
    DIGITS1TO8 = '1, 2, 3, 4, 5, 6, 7, 8'.split()
    while True:
        print('Skriv in ditt drag, "avbryt" för att avsluta, eller "tips" för ledtråd om bästa drag.')
        move = input().lower()
        if move == 'avbryt' or move == 'tips':
            return move
        
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Detta är inte ett giltigt drag. Skriv in Kolumn 1-8 och Rad 1-8.')
            print('Till ex 81 lägger längst upp till höger.')

    return [x, y]

def getComputerMove(board, computerTile):
    # Given the board and computers tile, determine where to
    # move andr Return that move as an [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # Randomize the order of the moves

    # Always go for the corner if possible
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Find the heighest scoring move that is possible.
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy) [computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('Du: %s poäng. Datorn: %s poäng,' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn + ' spelar först.')

    # Clear the board and place starting pieces
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and getComputerMove == []:
            return board # No one can move - game ends

        elif turn == 'player': # Players turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getplayerMove(board, playerTile)
                if move == 'avsluta':
                    print('Tack för att du spelat.')
                    sys.exit()
                elif move == 'tips':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Tryck enter för att se datorns drag.')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'player'



print('Välkommen till Reversi')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    #Display the final score
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X tog %s poäng och O tog %s poäng' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('Du slog datorn med %s poäng. Grattis!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('Datron besegrade dig med %s poäng. Bättre lycka nästa gång.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('Matchen slutade oavgjort!')

    print('Vill du spela igen? J/N')
    if not input().lower().startswith('j'):
        break