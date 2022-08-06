y=str(input("What is your name?"))
x=float(input("Please enter your marks out of 100"))
if x>100:
  print("That is too high!")
elif x<0:
  print("Invalid Input!!!")
elif 0<=x<=50:
  print(y,",","you failed with a score of",x,"%. Oof.")
elif x>=80:
  print("Congratulations",y,"! You mastered the topic with a score of",x,"%")
else:
  print(y,"you got a score of",x,"%. At least you passed.")
