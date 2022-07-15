def Run():

  #Sonar Treasure Hunt

  import random
  import math
  import sys

  def getNewBoard():
    #Create new 60x15 board data structure
    board = []
    for x in range(60): #Main list is a list of 60 lists
      board.append([])
      for y in range(15): #Each list in main list has 15 single char strings
        #Use different char for the ocean to make it more readable
        if random.randint(0, 1) == 0:
          board[x].append('~')
        else:
          board[x].append('`')
    return board

  def drawBoard(board):
    # Draw the board data structure
    tensDigitsLine = '    ' #Initial space for the numbers down left side of board
    for i in range(1, 6):
      tensDigitsLine += (' ' * 9) + str(i)

    #Print numbers across top of board
    print(tensDigitsLine)
    print('    ' + ('0123456789' * 6))
    print()

    #Print each of the 15 rows
    for row in range(15):
      #Single digit numbers need to be padded w/extra space
      if row < 10:
        extraSpace = ' '
      else:
        extraSpace = ''

      # Create the string for this row on the board
      boardRow = ''
      for column in range(60):
        boardRow += board[column][row]

      print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    #Print the numbers across the bottom of the board
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

  def getRandomChests(numChests):
    #Create list of chest data structures (two-item lists of x, y coordinates)
    chests = []
    while len(chests) < numChests:
      newChest = [random.randint(0, 59), random.randint(0, 14)]
      if newChest not in chests: #checks for duplicate chests
        chests.append(newChest)
    return chests

  def isOnBoard(x, y):
    #Return True if coordinates are on the board
    return x >= 0 and x<=59 and y >= 0 and y <= 14

  def makeMove(board, chests, x, y):
    #Change board data structure with a sonar device char
    #Remove trasure chest from chests list as they are found
    #Returns False if move is invalid
    #Otherwise returns string of the result of this move

    smallestDistance = 100 #Any chest will be closer than 100
    for cx, cy in chests:
      distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

      if distance < smallestDistance: #We want closest chest
        smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
      #xy on chest!
      chests.remove([x, y])
      return 'Du har sänkt en ubåt!'
    else:
      if smallestDistance < 10:
        board[x][y] = str(smallestDistance)
        return 'Ubåt upptäkt på ett avstånd av %s från sonarbojen.' % (smallestDistance)
      else:
        board[x][y] = '?'
        return 'Ingenting upptäkt på sonar. Ubåtarna är för långt borta.'

  def enterPlayerMove(previousMoves):
    #Let player enter move. Return a two-item list of int xy coordinates
    print('Var vill du släppa nästa sonarboj? (0-59 0-14) (eller skriv "avluta"')
    while True:
      move = input()
      if move.lower == 'avluta':
        print('Du gav upp. Bättre lycka nästa gång!')
        sys.exit()

      move = move.split()
      if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
        if [int(move[0]), int(move[1])] in previousMoves:
          print('Du har redan släppt en boj där.')
          continue
        return [int(move[0]), int(move[1])]

      print('Skriv ett nummer 0-59, mellanslag, sen ett nummer 0-14')

  def showInstructions():
    print('''Instruktioner:
          
Du är kapten på Spaningsbåten HMS Djärv, med uppdrag att spana efter och sänka ryska ubåtar i Stockholms skärgård. Till din hjälp har du sonarboj 111 och sjunkbomb m/33.
Sonarbojarna kan enbart ange avstånd, inte bäring.
Ange koordinaterna för att släppa dina motmedel. Koordinaterna på kartan uppdateras med avstånd till närmaste mål, eller ett "X" om sjunkbomben träffat rätt.

          Tryck Enter för att fortsätta...''')
    input()

    print('''När du sänkt en ubåt, uppdateras övriga bojar för att visa var den nästa närmaste ubåten är. Om närmaste ubåt är utom räckhåll markeras bojen med "?".
Sonarbojarna har en räckvidd på 9 rutor.
Försök sänka alla ubåtar innan du får slut på bojar och bomber.
          
          Lycka till!
          
          Tryck Enter för att fortsätta...''')
    input()


  print('*** S O N A R - U B Å T S J A K T ***')
  print()
  print('Vill du läsa instruktionerna? (J/N)')
  if input().upper().startswith('J'):
    showInstructions()

  while True:
    #Game Setup
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
      #Show sonar devices and chest status
      print('Du har %s bojar/bomber kvar. %s Ubåtar är fortfarande på fri fot!' % (sonarDevices, len(theChests)))
      x, y = enterPlayerMove(previousMoves)
      previousMoves.append([x, y]) #We must track all moves so that sonar devices can be updated

      moveResult= makeMove(theBoard, theChests, x, y)
      if moveResult == False:
        continue
      else:
        if moveResult == 'Du har sänkt en ubåt!':
          #update all sonar devices on map
          for x, y in previousMoves:
            makeMove(theBoard, theChests, x, y)
        drawBoard(theBoard)
        print(moveResult)

      if len(theChests) == 0:
        print('Du har sänkt alla ryska ubåtar i skärgården! Grattis och bra jobbat!')
        break

      sonarDevices -= 1

    if sonarDevices == 0:
      print('Du har slut på bojar och sjunkbomber. De kvarvarande ryska ubåtarna smet undan med svansen mellan benen. Bättre lycka nästa agång')
      print('De sista ubåten/ubåtarna var här:')
      for x, y in theChests:
        print('    %s, %s' % (x, y))

    print('Vill du spela igen? (J/N)')
    if not input().upper().startswith('J'):
      sys.exit()
      