def Run():

# Tic Tac Toe
  
  import random
  
  def drawBoard(board):
    #This function prints out the board that it was passed. 
  
    #Board is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
  
  def inputPlayerLetter():
    #Lets player choose side
    #Returns a list w/players letter first and computers letter as second. 
    letter = ''
    while not(letter == 'X' or letter == 'O'):
      print('Vill du spela som X eller O?')
      letter = input().upper()
  
    #The first element in list is players letter; second is comp letter
    if letter == 'X':
      return['X', 'O']
    else:
      return['O', 'X']
  
  def whoGoesFirst():
    #Randomly choose who goes first.
    if random.randint(0, 1) == 0:
      return 'computer'
    else:
      return 'player'
  
  def makeMove(board, letter, move):
    board[move] = letter
  
  def isWinner(bo, le):
    #Given state of board and players letter, function returns True if player won
    #We use bo and le so we dont have to type as much
  
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across top
      (bo[1] == le and bo[2] == le and bo[3] == le) or #across bottom
      (bo[4] == le and bo[5] == le and bo[6] == le) or #middle
      (bo[2] == le and bo[5] == le and bo[8] == le) or #middle2            
      (bo[1] == le and bo[4] == le and bo[7] == le) or #left
      (bo[3] == le and bo[6] == le and bo[9] == le) or #right
      (bo[1] == le and bo[5] == le and bo[9] == le) or #diag1
      (bo[7] == le and bo[5] == le and bo[3] == le)) #diag2
  
  def getBoardCopy(board):
    #Make copy of board list and return it. 
    boardCopy = []
    for i in board:
      boardCopy.append(i)
    return boardCopy
  
  def isSpaceFree(board, move):
    #Returns True if the passed move is free on the passed board. 
    return board[move] == ' '
  
  def getPlayerMove(board):
    #Let player enter move. 
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
      print('Vad är ditt drag? (1-9)')
      move = input()
    return int(move)
  
  def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passed list on the passed board
    #Returns None if there is no valid move. 
  
    possibleMoves = []
    for i in movesList:
      if isSpaceFree(board, i):
        possibleMoves.append(i)
  
    if len(possibleMoves) != 0:
      return random.choice(possibleMoves)
    else:
      return None
  
  def getComputerMove(board, computerLetter):
    #Given state of board and computer letter, determine move and return it. 
    if computerLetter == 'X':
      playerLetter = 'O'
    else:
      playerLetter = 'X'
  
    #Tic Tac Toe AI
    #1st - Check if win possible on next move
    for i in range(1, 10):
      boardCopy = getBoardCopy(board)
      if isSpaceFree(boardCopy, i):
        makeMove(boardCopy, computerLetter, i)
        if isWinner(boardCopy, computerLetter):
          return i
  
    #Check if players next move wins and block that
    for i in range(1, 10):
      boardCopy = getBoardCopy(board)
      if isSpaceFree(boardCopy, i):
        makeMove(boardCopy, playerLetter, i)
        if isWinner(boardCopy, playerLetter):
          return i
  
    #Try to take a corner if it is free. 
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
      return move
  
    #Try to take center if free
    if isSpaceFree(board, 5):
      return 5
  
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
  
  def isBoardFull(board):
    #Return True if every space on the board has been taken, othewise return False
    for i in range(1, 10):
      if isSpaceFree(board, i):
        return False

    return True
  
  
  #***** Here starts the code *****
  
  print('Välkommen till Luffarschack!')

  while True:
    #Reset board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' börjar.')
    gameIsPlaying = True

    while gameIsPlaying:
      if turn == 'player':
        #Players turn
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)

        if isWinner(theBoard, playerLetter):
          drawBoard(theBoard)
          print('Hurra! Du vann!')
          gameIsPlaying = False
        else:
          if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('Oavgjort!')
            break
          else:
            turn = 'computer'
      else:
        #Computers turn
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)

        if isWinner(theBoard, computerLetter):
          drawBoard(theBoard)
          print('Datorn har besegrat dig! Du är en förlorare!')
          gameIsPlaying = False
        else:
          if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('Oavgjort!')
            break
          else:
            turn = 'player'

    print('Vill du spela igen? J/N')
    if not input().upper().startswith('J'):
      break
                      
    
