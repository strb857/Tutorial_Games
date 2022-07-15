def Run():

  import random
  number1 = random.randint(1, 10)
  number2 = random.randint(1, 10)
  print('What is ' + str(number1) +' + ' + str(number2) + '?')
  answer = input()

  #Denna rad är fel eftersom answer är str och övrigt är int -> alltid False
  if answer == number1 + number2:
    print('Correct!')
  else:
    print('Nope! The answer is ' + str(number1 + number2))
    