num1=int(input("Enter a num:"))
num2=int(input("Enter a num:"))
num3=int(input("Enter a num:"))
num4=int(input("Enter a num:"))
num5=int(input("Enter a num:"))
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("biggest num",num1)
elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
    print("biggest num",num2)
elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
    print("biggest num",num3)
elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
    print("bigget num",num4)
elif num5>num1 & num5>num2 & num5>num3 &num5>num4:
    print("Enter a num",num5) 
else:
    print("All are same.")