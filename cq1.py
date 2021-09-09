salary=int(input("Enter salary:"))
service_yrs=int(input("Enter the year of service:"))
i=salary*5
if service_yrs>5:
    print("bonus is:",i)
    print("The net bonus amount.")
else:
    print(" Sorry, You are not eligible for bonus, your service of year is less than 5 years.")