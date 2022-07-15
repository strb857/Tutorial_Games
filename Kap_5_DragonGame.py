def Run():
  
  import random
  import time
  
  def displayIntro():
    print('''You see two caves in the land of dragons.
Inside the might be a friendly or it might might be hungry dragon.
Which cave do you choose?''')
    print()
  
  def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
      print('Which cave will you go into? (1 or 2)')
      cave = input()
  
    return cave
  
  def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon appears...')
    print()
    time.sleep(2)
  
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
      print('...and gives you his treasure!')
    else:
      print('...and eats you whole!')
  
  playAgain = 'yes'
  while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
  
    print('Do you want to play again? (Yes or No)')
    playAgain = input()
  
  