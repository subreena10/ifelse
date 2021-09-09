score= int(input("Enter the score:"))
if score>100 and score<0:
    print("score is invalid")
elif  score>=50:
      print("you have passed your exams")
      print("congratulations")
else:
      print("sorry, you have failed your exam.")