import random

a = random.randint (1,100)

b = int (input ("Enter any number of your choice:"))

while a !=b:
 if abs (a - b) <=5 :
  print ("You are very close, try again")
 elif abs (a - b) < 15:
  print ("You are close,try again")
 elif abs (a - b) < 25:
  print ("You are a little too far,try again")
 elif abs (a - b) >30:
  print ("You are very far,try again")
 b = int (input ("Enter another number:"))
else:
 print ("Great job! You are correct")