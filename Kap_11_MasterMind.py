def Run():

  import random
  NUM_DIGITS = 3
  MAX_GUESS = 10

  def getSecretNum():
    #Returns a string of unique random digits that is NUM_DIGITS long. 
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
      secretNum += str(numbers[i])
    return secretNum

  def getClues(guess, secretNum):
    #Returns a string of clues to user based on guess
    if guess == secretNum:
      return 'Du klarade det!'

    clues = []
    for i in range(len(guess)):
      if guess[i] == secretNum[i]:
        clues.append('Svart')
      elif guess[i] in secretNum:
        clues.append('Vit')
    if len(clues) == 0:
      return '-'

    #clues.sort()
    random.shuffle(clues)
    return ' '.join(clues)

  def isOnlyDigits(num):
    #Returns True if num is string of only digits. Otherwise False.
    if num == '':
      return False

    for i in num:
      if i not in '0 1 2 3 4 5 6 7 8 9'.split():
        return False

    return True

  print('*** M A S T E R  M I N D ***')
  print()
  print('Jag tänker på ett %s-siffrigt tal. Försök gissa vilket.' % (NUM_DIGITS))
  print()
  print('Ledtrådarna är:')
  print('"-" betyder att ingen siffra är rätt')
  print('"Vit" betyder att en siffra är rätt men på fel plats')
  print('"Svart" betyder att en siffra är på rätt plats')
  print()

  while True:
    secretNum = getSecretNum()
    print('Jag har tänkt ut ett nummer. Du har %s gissningar att lista ut det.' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
      guess = ''
      while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
        print('Gissning #%s: ' % (guessesTaken))
        guess = input()

      print(getClues(guess, secretNum))
      guessesTaken += 1

      if guess == secretNum:
        break
      if guessesTaken > MAX_GUESS:
        print('Du har slut på gissningar. Svaret var %s.' % (secretNum))

    print('Vill du spela igen? (J/N)')
    if not input().upper().startswith('J'):
      break