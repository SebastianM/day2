import random


while(True):
  grade = int(input("what is your grade: "))

  if (grade >= 90):
    print("you got an A")

  elif (grade >= 75):
    print("you got a B")

  elif (grade >= 50):
    print("you got an F")
  else:
    print("Meet me after class")