chapter = True
while chapter:
  print('''Meny:
  
  1. Hello World
  2. Guess the Number
  3. Dragons
  4. Buggy
  5. Hangman
  6. Hangman 2
  7. Tic Tac Toe
  8. Master Mind
  9. Ubåtsjakt
  x. Exit
        ''')
  
  chapter = input('Välj kap: ')
  print()
  
  if chapter == '1':
    print('Running Kap_2_HelloWorld')
    print()
    from Kap_2_HelloWorld import Run
    Run()
    print()
  elif chapter == '2':
    print('Running Kap_3_GuessingGame')
    print()
    from Kap_3_GuessingGame import Run
    Run()
    print()
  elif chapter == '3':
    print('Running Kap_5_DragonGame')
    print()
    from Kap_5_DragonGame import Run
    Run()
    print()
  elif chapter == '4':
    print('Running Kap_6_Buggy')
    print()
    from Kap_6_Buggy import Run
    Run()
    print()
  elif chapter == '5':
    print('Running Kap_8_Hangman')
    print()
    from Kap_8_Hangman import Run
    Run()
    print()
  elif chapter == '6':
    print('Running Kap_9_Hangman2')
    print()
    from Kap_9_Hangman2 import Run
    Run()
    print()
  elif chapter == '7':
    print('Running Kap_10_TicTacToe')
    print()
    from Kap_10_TicTacToe import Run
    Run()
    print()
  elif chapter == '8':
    print('Running Kap_11_MasterMind')
    print()
    from Kap_11_MasterMind import Run
    Run()
    print()
  elif chapter == '9':
    print('Running Kap_13_Sonar')
    print()
    from Kap_13_Sonar import Run
    Run()
    print()
  elif chapter == 'x':
    break
  else:
    print('Invalid option!')
    print()
