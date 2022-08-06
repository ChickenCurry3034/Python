import random
import sys
print("welcome to Fedral bank! Thank you for choosing us ")
data={}
count=0

while True:
    print("what operation you want to perform it")
    print("choose 1 to open an account")
    print("choose 2 for deposit")
    print("choose 3 for withdrawal")
    print("choose 4 for balance check")
    x=int(input("Choose the optn from above"))

    if x==1:
      sbal=0
      a=input("pls enter your name: ")
      for i in range(3):
        b=int(input("pls enter you contact number: "))
        if len(str(b))==10:
          break
        else:
          print("Invalid contact number, please try again")
      d=input("pls enter your address: ")
      for i in range(3):
        e=input("pls enter your email id: ")
        if "@" in e and "." in e:
          break
        else:
          print("Invalid contact number, please try again")
      print("congratulations for opening an account with HDFC bank! Below are the following information:")
      print("Account Holder name:",a)
      print("Account Holder contact no:",b)
      print("Account Holder address:",d)
      print("Account Holder email_id:",e)
      acc=random.randint(10000000,99999999)
      print("Account Holder security no",acc)
      pas=random.randint(1000,9999)
      print("Account Holder pin no",pas)
      data[acc]=[sbal,a,b,d,e,pas]

    elif x==4:
      for i in range(3):
        j=int(input("Enter the security no"))
        if j not in data:
          print("Account doesn't exist")
        else:
          k=int(input("Enter your pin"))
          for i in range(3):
            if data[j][-1]==k:
              print(data[j][1],"balance in your account is",data[j][0])
              break
            else:
              print("Incorrect pin")
        break

    elif x==2:
      count=0
      while count<3:
          if count<3:
              g=int(input("please enter the account number in which you want to deposit: "))
              depo=int(input("Enter the amount which you want to desposit"))
              if g in dict1:
                  fbal=data[j][0]+depo
                  data[j][0]=fbal
                  print("Thank you",data[j][1],"for depositing",depo)
                  print("Updated balance is",fbal)
              else:
                  count=count+1
                  if count==3:
                    break
                  else:
                    print("Account not found,please re enter the correct account number again..")

    elif x==3:
      count=0
      for i in range(3):
        j=int(input("Enter the security no"))
        if j not in data:
          print("Account doesn't exist")
          count=count+1
        else:
          count=0
          k=int(input("Enter your pin"))
          withdraw=float(input("How much money would you like to withdraw?"))
          for i in range(3):
            if data[j][-1]==k:
              if 0<withdraw<=data[j][0]-100:
                print(data[j][1],withdraw,"withdrawed, now balance in your account is",data[j][0]-withdraw)
                data[j].insert(0,data[j][0]-withdraw)
                data[j].remove(data[j][1])
                break
              else:
                print("Please enter a valid amount that can be withdrawed")
                count=count+1
            else:
              print("Incorrect pin")
              count=count+1
        break

    if count>=3:
      print("Limit exceeded, thank you for banking with us!")
      sys.exit()

    n=0
    while n<3:
      ans=input("Do you want to perform more operation yes/no")
      if ans.lower()=='yes':
        break
      if ans.lower()=='no':
        print("Thank you for banking with us, have a nice day!")
        sys.exit()
      else:
        print("Please try again")
        n=n+1
      if n>=3:
        print("Limit exceeded, thank you for banking with us!")
        sys.exit()
