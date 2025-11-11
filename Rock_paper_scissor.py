import random as rs
a=['Rock','Paper','Scissor']
attempts=3
try:
    while True:
        choice=rs.choice(a)
        num=int(input("Enter 1 for Rock enter 2 for paper enter 3 for scissor: "))
        
        if num > 3:
            print("Please Enter the number between 1 to 3")
            continue
            
        if attempts!=1 :
            if num == 1 and choice =='Rock':
                print("You Won! ",choice)
                break
        
            elif num == 2 and choice =='Paper':
                print("You Won! ",choice)
                break
        
            elif num == 3 and choice =='Scissor':
                print("You Won! ",choice)
                break
            else:
                print("Wrong guess ", choice)
                attempts-=1
                print('attempts= ',attempts)
        
        else:
            print("Sorry You Lose")
            break
            
except Exception as e:
    print("please Enter between 1 to 3 " ,e)