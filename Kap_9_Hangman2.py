def Run():

  import random
  HANGMAN_PICS = ['''
                  +---+
                      |
                      |
                      |
                     ===''', '''
                  +---+
                  o   |
                      |
                      |
                     ===''', '''
                  +---+
                  o   |
                  |   |
                      |
                     ===''', '''
                  +---+
                  o   |
                 /|   |
                      |
                     ===''', '''
                  +---+
                  o   |
                 /|\  |
                      |
                     ===''', '''
                  +---+
                  o   |
                 /|\  |
                 /    |
                      |
                     ===''', '''
                  +---+
                  o   |
                 /|\  |
                 / \  |
                      |
                     ===''', '''
                  +---+
                 [o   |
                 /|\  |
                 / \  |
                      |
                     ===''', '''                  
                  +---+
                 [o]  |
                 /|\  |
                 / \  |
                     ===''']

  words = {
    'djur':'brunbjörn bäver ekorre fladdermus grävling hare igelkott mullvad rådjur räv vildsvin älg'.split(),
    'former':'kvadrat rektangel triangel cirkel cylinder kub rätblock kon'.split(), 
    'frukter':'ananas apelsin aprikos banan carambola citron citrusfrukt clementin granatäpple grapefrukt kaktusfikon kumquat kiwi lime mandarin mango melon nektarin papaya passionsfrukt persika plommon päron satsuma sharon äpple'.split(), 
    'färger':'akvamarin azur beige blå brun bärnsten cerise cinnober cyan ecru elfenben falurödfärg ftaloblått fuchsia grå grön gul guld indigo isabella karmin karmosin kastanj khaki korall kornblå lavendel lila lime lime marinblå ockra olivgrön orange purpur rosa rost röd scharlakansröd sepia sienna silver smaragdgrön svart teal terrakotta titanvitt turkos ultramarin vinröd violett vit zinkvitt'.split()
          }
  
  def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary of lists of strings and its keys. 
    # First, randomly select a key from the dictionary:
    # Slumpar fram en key ur listan av wordDict keys ex. former
    wordKey = random.choice(list(wordDict.keys()))
    # Secondly, randomly select a word from the keys list in the dictionary:
    # Väljer ett ord ur den lista som valdes ovan. len(wordDict[wordKey]) är antalet ord i listan som valdes.
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    #returnerar 2 saker - ett ord (wordIndex ur wordDict[wordKey]) och en nyckel wordKey ex "djur"
    return [wordDict[wordKey][wordIndex], wordKey]
  
  def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
  
    print('Missade bokstäver:', end=' ')
    for letter in missedLetters:
      print(letter, end=' ')
    print()
  
    blanks= '_' * len(secretWord)
    
    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters. 
      if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
  
    for letter in blanks: # Show the secret word with spaces in between each letter
      print(letter, end=' ')
    print()

  def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function mask sure the player entered a single letter and not something else. 
    while True:
      print('Gissa en bokstav.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
        print('Gissa högst en bokstav.')
      elif guess in alreadyGuessed:
        print ('Du har redan gissat den bokstaven. Gissa igen.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyzåäö':
        print('Gissa bara bokstäver.')
      else:
        return guess

  def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False. 
    print('Vill du spela en gång till? (ja eller nej) ')
    return input().lower().startswith('j')

  print(' H Ä N G A  G U B B E')
  
  difficulty = ' '
  while difficulty not in 'LMS':
    print('Vilken svårighetsgrad vill du ha? (L)ätt (M)edel (S)vår')
    difficulty = input().upper()
    
  if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]

  if difficulty == 'S':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    
  missedLetters = '' 
  correctLetters = ''
  secretWord, secretSet = getRandomWord(words)
  gameIsDone = False
  
  while True:
    print('Det hemliga ordet är i kategorin: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter. 
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
      correctLetters = correctLetters + guess
  
      # Check if the player has won. 
      foundAllLetters = True
      for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
          foundAllLetters = False
          break
  
      if foundAllLetters:
        print('Snyggt! Det hemliga ordet är "' + secretWord + '"! Du har vunnit!')
        gameIsDone = True
  
    else:
      missedLetters = missedLetters + guess 
  
      # Check if player has guessed too many times and lost. 
      if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Du har slut på gissningar!\nEfter ' + str(len(missedLetters)) + ' missade gissningar och ' + str(len(correctLetters)) + ' korrekta gissningar.\nOrdet var: "' + secretWord + '"')
        gameIsDone = True
  
    # Ask player if they want to play again (but only if the game is over). 
    if gameIsDone:
      if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord, secretSet = getRandomWord(words)
      else:
        break
        