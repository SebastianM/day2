import random


play = True

while (play == True):
  win = False
  num = random.randint(1, 10)
  attemps = 5
  

  while (attemps > 0):
      ask = int(input("guess a number between 1 and 10:"))
  
      if (ask == num):
         win = True
         break
      else:
            print("wrong, try agian")
            win = False
            attemps -= 1
            print(f"you have {attemps} attemps left")
  if(win == True):
    print("you've got it")
  else:
    print("you've lost")
  ask2 = input("do you want to play again? ")
  if(ask2 == ("no")):
    break
  elif():
    play = True