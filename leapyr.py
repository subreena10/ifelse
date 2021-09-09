year=int(input("enter a year:"))
if year%4==0:
    print("A year is leap")
elif year%100==0 and year%400==0:
    print("A year is leap")
else:
    print("A year is not leap")