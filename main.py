import random

num = random.randint(0, 1000)

if(num < 500):
  print(num)
  print("this is a small number")
if(num > 500):
  print(num)
  print("this is a big number")