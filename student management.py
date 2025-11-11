from pathlib import Path
import string
import json
import random
class subh:



    database='studentdata.json'
    data=[]
    
    try:
        with open(database,'r') as f:
            data=json.loads(f.read())

    except Exception as e:
        print("An error ocuured ",e)
            
    
    
    
    
    def usecreate(self):
        try:
            studata={
                "name":input("Enter your Name: "),
                "Class":input("Enter the class from I to VI: "),
                "Father's name":input("Enter your father's name: "),
                "mother's name":input("Enter your mother's name: "),
                "Age":input("Enter student's age: "),
                "Gender":input("Enter student's Gender ( M / F / m /f): ")
                
            }
            
            studata['Rollno']=subh.__rollgen(studata["Class"])
            
            print("Enter student's Marks")
            studata["marks"]={"math":int(input("Enter the math number out of 100: ")),
                            "Science":int(input("Enter the science number out of 100: ")),
                            "English":int(input("Enter the English number out of 100: ")),
                            "History":int(input("Enter the History number out of 100: ")),
                            "Geography":int(input("Enter the Geography number out of 100: ")),
                            "Social science":int(input("Enter the Social science number out of 100: ")),
                            "Hindi":int(input("Enter the Hindi number out of 100: "))} 
            
            subh.data.append(studata)
            subh.__updatedata() 
            print("student data has been created")
                       
        except Exception as e:
            print("An error occured ",e)
            
    
    def showdatails(self):
        roll=input("Enter student Rollno: ")
        studata=[i for i in  subh.data if i['Rollno']==roll]
        
        for i,j in studata[0].items():
            if i != 'marks':
                print(f"{i} : {j}")
        
    def showmarks(self):
        roll=input("Enter student rollno: ")
        studata=[i for i in subh.data if i['Rollno'] == roll]
        for i,j in studata[0]['marks'].items():
                print(f"{i} : {j}")
                
    def update_details(self):
        try:
            roll=input("Enter student's roll number: ")
            studata=[i for i in subh.data if i['Rollno'] == roll]
            if roll ==studata[0]['Rollno'] :
                newdata={
                    'name':input("Enter the name of the student you want to change or press enter if you want to skip the change: "),
                    'Class':input("Enter the class of the student you want to change or press enter if you want to skip the change: ")
                    
                }
                if newdata['name'] == "":
                    newdata['name']==studata[0]['name']
                    
                if newdata["Class"]=="":
                    newdata['Class']==studata[0]['Class']
                for i in studata[0]:
                    if i=='name' or i=='Class':
                        continue
                    else:
                        newdata[i]=studata[0][i]
                        
                
                
                for i in newdata:
                    if newdata[i]==studata[0][i] :
                        continue
                    else:
                        studata[0][i] = newdata[i]
                        
                subh.__updatedata()   
                print("Data has been updated")  
            
        except Exception as err:
            print("Some Error ocuured",err)
        
    def update_marks(self):
        try:
            roll=input("Enter Roll no of student you want to update: ")
            
            studata=[i for i in subh.data if i['Rollno']==roll]
            newdata={}
            if roll==studata[0]['Rollno']:
                newdata['marks']={"math":(input("Enter the math number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "Science":(input("Enter the science number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "English":(input("Enter the English number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "History":(input("Enter the History number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "Geography":(input("Enter the Geography number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "Social science":(input("Enter the Social science number out of 100 you want to change or press 'Enter' to Skip: ")),
                                "Hindi":(input("Enter the Hindi number out of 100 you want to change or press 'Enter' to Skip: "))
                    
                    
                }
                for i in newdata['marks'] :
                    if newdata['marks'][i]=="":
                        newdata['marks'][i]=studata[0]['marks'][i]
                        
                for i in newdata['marks'] :
                    if studata[0]['marks'][i] == int(newdata["marks"][i]):
                        
                        continue
                    else:
                        
                        studata[0]['marks'][i] = int(newdata['marks'][i]) 
                
                subh.__updatedata()
                
                print("Marks has been changed")
            else:
                print("please Enter the current roll no:")
                
        except Exception as err:
            print("Some error ocuured",err)
            
    def delete_stu(self):
        try:
            roll=input("Please Enter student roll number you want to delete: ")
            studata=[i for i in subh.data if i['Rollno'] == roll]
            if studata==[]:
                print("Data Doesn't Exist")
                
            else:
                index=subh.data.index(studata[0])
                subh.data.pop(index)
                subh.__updatedata()
                print("Data Has been Deleted")
        
        except Exception as e:
            print("Some Error ocuured",e)
                    
    
    @classmethod
    def __updatedata(cls):
        with open (cls.database,'w') as f:
            f.write(json.dumps(cls.data))
        
    @classmethod
    def __rollgen(cls,cll):
        
        cls.Class=cll
        
        roll=random.choices(string.digits,k=3)
        random.shuffle(roll)
        if cls.Class=='I':
            
            return f'01{"".join(roll)}' 
        if cls.Class=='II':
            return f'02{"".join(roll)}' 
        if cls.Class=='III':
            return f'03{"".join(roll)}' 

        if cls.Class=='IV':
            return f'04{"".join(roll)}' 
        if cls.Class=='V':
            return f'05{"".join(roll)}' 
        if cls.Class=='VI':
            return f'06{"".join(roll)}' 
        
        



print("Press 1 for to Add details of student")
print("Press 2 for to see details of student")
print("Press 3 for to show marks of student")
print("Press 4 for to update details of student")
print("Press 5 to update marks")
print("Press 6 for to delete details of student")

check=int(input("Enter your choice from 1 to 6: "))

ob=subh()

try:
        
    if check <7:    
        if check == 1:
            ob.usecreate()
        
        if check == 2:
            ob.showdatails()
            
        if check == 3:
            ob.showmarks()
        
        if check == 4:
            ob.update_details()
            
        if check == 5 :
            ob.update_marks()
            
        if check == 6:
            ob.delete_stu()
            
    
    else:
        print("Please enter a number from 1 to 6 ")
        

except Exception as err:
    print("please give a integer ",err)