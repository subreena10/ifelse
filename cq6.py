first=int(input("Enter first age:"))
second=int(input("Enter second age:"))
third=int(input("Enter third age:"))
if first>second and first>third:
    print("First is oldest.")
elif second>first and second>third:
    print("Second is oldest.")
elif third>first and third>second:
    print("Third is oldest.")
else:
    print("all are equal.")