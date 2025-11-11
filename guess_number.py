import random as rs
number=rs.randint(1,100)
print("Welcome To Guess The Number Game!")
attempt=10
while True:
   a=int ( input( "Take your guess: "))
   if attempt !=1:
    if a>number:
        print("Too high!")
        attempt -=1
        print("attempts = ",attempt)
    elif a<number:
        print("Too low!")
        attempt-=1
        print("attempts = ",attempt)
    else:
        print("Congratulation You Won!")
        print("attempts = ",attempt-1)
        break
        
   else:
       print("Sorry You lose The Game")
       break