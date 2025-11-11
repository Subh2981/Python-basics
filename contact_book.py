from pathlib import Path 
import json


class phone:
    
    database='contact.json'
    data=[]
    try:
        with open(database,'r') as f:
            data=json.loads(f.read())
            
    except Exception as ex:
        print("Some Error Occured 1",ex)

    
    def Addcontact(self):
        try:
            details={
                'Name':input("Enter name of the contact: "),
                'Number':int(input("Enter ten digit number: "))
            }
            
            if len(str(details["Number"])) != 10:  
                print("Enter Ten Digit number")
            
            elif details["Name"]=="":
                print("Please Give a name")
            else:
                phone.data.append(details)
                phone.__updatedetail()
                print("Contact Has been Added")
        except Exception as e:
            print('2',e)
            
    def editcontact(self):
        name=input("Enter the name you want to change: ")
        
        con=[i for i in phone.data if i["Name"] == name ]
        
        if con == False:
            print("Data not found")
            
        else:
            newd={
                'Name':input("Enter the name you want to edit: "),
                'Number': int(input("Enter the number you want to change: "))
            }
            if newd["Name"]=="":
                newd["Name"]=con[0]["Name"]
                
            if newd["Number"]=="":
                newd["Number"]=con[0]["Number"]
                
            for i in newd:
                if con[0][i] == newd[i]:
                    continue
                else:
                    con[0][i] = newd[i]
                    
                    
            phone.__updatedetail()
            print("Contact has been updated")
    
    
    def serachcontact(self):
        try:
            name=input("please Enter the name you want to search: ")
            con=[i for i in phone.data if i ["Name"] == name]
            if con==False:
                print("data not found")
            else:
                print(f"The contact number of{con[0]['Name']} is {con[0]['Number']}")
        except Exception as e:
            print("Contact doesn't exist")
    
    
    def deletecontact(self):
        try:
            name=input("please Enter the name you want to delete: ")
            con=[i for i in phone.data if i ["Name"] == name]
            if con==False:
                print("data not found")
                
            else:
                index=phone.data.index(con[0])
                
                phone.data.pop(index)
                
                phone.__updatedetail()
                print("Data has been deleted")
                
        except Exception as e:
            print("Some Error Occured ",e)
            
        
            
    @classmethod
    def __updatedetail(cls):
        try:
            with open(cls.database,'w') as f:
                f.write(json.dumps(cls.data))
                
        except Exception  as s:
            print("Some Error occured 3",s)



print("Press 1 for Add contacts")
print("Press 2 for Edit contacts ")
print("Press 3 for search contacts")
print("Press 4 for delete contacts")
check = int(input("Enter Your Choice: "))

a=phone()

if check == 1:
    a.Addcontact()
    
if check == 2:
    a.editcontact()

if check == 3:
    a.serachcontact()

if check == 4:
    a.deletecontact()
    
    