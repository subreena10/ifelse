mark=int(input("Enter your marks:"))
if mark<25:
     print("Sorry,you are not qualified.")
elif mark>25 and mark<45:
      print("Your grade is E.")
elif mark>45 and mark<50:
      print("Your grade is D.")
elif mark>50 and mark<60:
      print("Your grade is C.")
elif mark>60 and mark<80:
      print("Your grade is B.")
else:
     print("your grade is A.")