noh=int(input("Enter the classes held:"))
noa=int(input("Enter the attended:"))
medical_cause=input("do you have medical_cause 'Y','N':")
attendance=(noa/noh)*100
if noa>=75:
    print("you are allowed to sit in exam.")
elif medical_cause=='Y':
    print("You are allowed to sit  in exam .")
else:
    print("You are not allowed to sit in exam.")