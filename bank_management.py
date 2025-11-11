import json
import random
from pathlib import Path
import string



class bank:
    database="data.json"
    data=[]
    try:
        with open(database,"r") as f:
            data=json.loads(f.read())

    except Exception as e:
        print("an exception occured",e)


    def crerateaccount(self):
        info={
            "name":input("enter your name"),
            "age":int(input("enter your age")),
            "email":input("enter your email"),
            "pin":int(input("enter your pin")),
            "accountNo":bank.__accountgenerate(),
            "balance":0
        }
        if info["age"] <18 or len(str(info["pin"])) != 4:
            print("invalid pin")

        else:
            print("acccount created successfully")
            for i in info:
                print(f"{i} : {info[i]}")

            bank.data.append(info)
            
            bank.__update()
            
            
    def deposit(self):
        accnu=input("please tell your account number")
        pin=int(input("pllese enter your pin"))
        
        userdata=[i for i in bank.data if i["accountNo"]==accnu and i["pin"]== pin]
        if userdata == False:
            print("sorry no data found")
            
        else:
            amount=int(input("How much you want to print"))    
            if amount > 10000 or amount<0:
                print("give amount  below 10000")
                
            else:
                userdata[0]['balance'] +=amount
                bank.__update()
                print("amount deposited succesfully")

    def  withdraw(self):
        accnu=input("please tell your account number")
        pin=int(input("pllese enter your pin"))
        
        userdata=[i for i in bank.data if i["accountNo"]==accnu and i["pin"]== pin]
        if userdata == False:
            print("sorry no data found")
            
        else:
            amount=int(input("How much you want to withdraw"))    
            if amount > userdata[0]["balance"]:
                print("not enough balance")
                
            else:
                userdata[0]['balance'] -=amount
                bank.__update()
                print("amount deposited succesfully")

    
    def show(self):
        accnu=input("please tell your account number")
        pin=int(input("pllese enter your pin"))
        
        userdata=[i for i in bank.data if i["accountNo"]==accnu and i["pin"]== pin]
        if userdata == False:
            print("sorry no data found")
        
        print("you details are \n\n\n")
        for i,j in userdata[0].items():
            
            print(i,":",j)
            
            
    def update(self):
        account=input("please enter your account number: ")
        pin=int(input("please enter your account pin: "))
        try:
         userdata=[i for i in bank.data if i["accountNo"]==account and i["pin"] == pin ]
         if userdata ==False:
            print("sorry no data found")
            
         else:
             newdata={"name":input("Enter a new name: "),
                     "email":input("enter your email: "),
                     "pin" :int(input("enter new pin: "))
                
             }
            
             if newdata["name"] =="":
                newdata["name"]=userdata[0]["name"]   
            
             if newdata["email"] =="":
                newdata["email"]=userdata[0]["email"]            
            
             if newdata["pin"] =="":
                newdata["pin"]=userdata[0]["pin"]  
                
                
             newdata["age"]=userdata[0]["age"]
             newdata["balance"]=userdata[0]["balance"]
             newdata["accountNo"]=userdata[0]["accountNo"] 
            
             for i in newdata:
                if newdata[i] == userdata[0][i]:
                    
                    continue
                else:
                    userdata[0][i]=newdata[i]
                    
                
            
             bank.__update()
             print("Data updated succesfully")
                         
        except Exception as e:
            print("an error occured ",e)   
            
            
    def delete(self):
        accountno=input("Enter the account number: ")
        pin=int(input("Enter the pin: "))
        try:
            userdata=[i for i in bank.data if i["accountNo"]==accountno and i["pin"] == pin ]
            
            if userdata == False:
                print("data doesnt exist")
                
            else:
                check=input("check if you real wnt to delete if yes ythe press y else press n: ")
                if check =="y" or check=="Y":
                    index=bank.data.index(userdata[0])
                    
                    bank.data.pop(index)
                else:
                    print("something went wrong")    
            
            bank.__update()
            
            print("data deleted successfully")
                
                    
        except Exception as e:
            print("error occured",e)
                
                      
        
                        
    @classmethod
    def __update(cls):
        with open(cls.database,"w") as f:
            f.write(json.dumps(cls.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spe=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spe
        random.shuffle(id)
        
        return "".join(id)    



print("press 1 for creating an account")
print("press 2 for depositing money")
print("press 3 for withdrawing money")
print("press 4 for details")
print("press 5 for updating detail")
print("press 6 for deleting account")


check=int(input("enter your choice:"))

user=bank()

if check == 1:
    user.crerateaccount()
    
    
if check == 2:
    user.deposit() 
    
if check == 3:
    user.withdraw()  
    
if check == 4:
    user.show() 
    
if check == 5:
    user.update()

if check == 6:
    user.delete()
