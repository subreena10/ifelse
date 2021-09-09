num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
oper=input("Enter a operation:")

if oper=="+":
    print(num1+num2,"addition")
elif oper=="-":
    print(num1-num2,"substraction")
elif oper=="*":
    print(num1*num2,"multiplication")
elif oper=="/":
    print(num1/num2,"divide")
elif oper=="%":
    print(num1%num2,"modulus division")
elif oper=="//":
    print(num1//num2,"float division")
elif oper=="**":
    print(num1**num2,"exponent")
else:
    print("invalid")