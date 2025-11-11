from pathlib import Path
import os
def readfilefolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i , items in enumerate (items):
        print(f"{i+1}:{items}") 
    
    
def createfile():
    try:
        readfilefolder()
        name=input("please tell your file name: ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as f:
                data=input("What dou want to write ")
                f.write(data)
        
            print("file created successsfully")
        else:
            print("this file already exist") 
    except Exception as e:
        print("an error occcured",e)
        

def readfile():
    readfilefolder()
    name=input("ehich file you wnt to read: ")
    p=Path(name)
    try:
        if p.exists() and p.is_file():
            with open(p,'r') as f:
                data=f.read()
                print(data)
                
            print("file readed succesfully")
        
        else:
            print("file does'nt exist")
                
    except Exception as e:
        print("an error occoured",e)
        
        
def updatefile():
    readfilefolder()
    
    name=input("which file you want to edit: ")
    
    p =Path(name)
    try:
        if p.exists and p.is_file():
            print("press 1 for change name of file")
            print("press 2 for overwrite file")
            print("press 3 for append the file")
            res=int(input("Give your response:"))
            
            if res == 1:
                name2=input("tell your file name: ")
                p2=Path(name2)
                p.rename(p2)
                print("file edited succesfully")
            if res == 2:
                with open(p,'w') as f:
                    data=input("tell what you wnt top write: ")
                    f.write(data)
                    print("file edited succesfully")
                    
            if res == 3 :
                with open(p,'a') as f:
                    data=input("tell what you wnt top write: ")
                    f.write(data)
                    print("file appended succesfully")
    except Exception as err:
        print("Error occured ",e)
        
def deletefile():
    readfilefolder()
    try:    
        name=input("which file you want to delete: ")        
        p=Path(name)
    
        if p.exists and p.is_file():
            os.remove(p)
            print("file removed successfully")
        else:
            print("file doesnot exist")    
    except Exception as e:
        print("an error occured ",e)
        
        
print("press 1 for crating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")
check=int(input("Enter a number from 1 to 4: "))


if check == 1:
    createfile()
    
if check == 2:
    readfile()
    
if check == 3:
    updatefile()
    
if check == 4:
    deletefile()