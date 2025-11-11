a=int (input("Enter First Number: "))
b=int(input("Enter Second Number: "))
oper=input("Enter the operstion yoyu wnt to perform ( +, -, /, *, %, //) : ")

if oper=='+':
    print("a + b = ",a+b)
    
elif oper=='-':
    print('a - b = ',a-b)

elif oper=='/':
    print(f"a / b= {a/b}")
    
elif oper == '*':
    print(f"a x b= {a*b}")
    
elif oper == '%':
    print(f"a % b = {a%b}")
    
elif oper == '//':
    print(f"a // b = {a//b}")
    