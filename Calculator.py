def factorial(number):
  product=1
  for e in range(1,number+1):
    product=product*e
  print("jagfjjf")
  print("Thanks for using Our Service")

def pyth():
  yn=input("Do you know the value of the Hypotenuse?")
  if yn=="Yes":
    leg1=float(input("What is the value of the leg?"))
    hypotenuse=float(input("What is the value of the hypotenuse?"))
    print("The second leg's value is",((hypotenuse**2)-(leg1**2))**0.5)
  if yn=="No":
    leg1=float(input("What is the value of one of the legs?"))
    leg2=float(input("What is the value of the other leg?"))
    print("The hypotenuse's value is",((leg2**2)+(leg1**2))**0.5)

def quad():
   avalue=float(input("What is the a value?"))
   bvalue=float(input("What is the b value?"))
   cvalue=float(input("What is the c value?"))
   disc=(bvalue**2)-(4*avalue*cvalue)
   sqrt_val = disc**0.5
   if disc<0:
     print("The answers are",- bvalue / (2 * avalue)," + i",sqrt_val,"and",- bvalue / (2 * avalue)," - i",sqrt_val)
   if disc>0:
     print("The answers are",(-bvalue + sqrt_val)/(2 * avalue),"and",(-bvalue - sqrt_val)/(2 * avalue))
   if disc==0:
     print("The answer is",-bvalue / (2 * avalue))

def compint():
  p=float(input("What is the initial principal balance?"))
  r=float(input("What is the interest rate (using decimals)?"))
  n=float(input("How many times is the interest applied over a certain time period?"))
  t=float(input("How many time periods do you want this to last?"))
  print("Your final amount will be",p*((1+(r/n))**(n*t)))

while True:
  operation=input("What operation would you like to do (+, -, *, /, ^, √, %, !, Pythagorean theorem, Quadratic Formula, or Compound Interest)?")
  if operation=="+":
    number1=float(input("What is your first number?"))
    number2=float(input("What is your second number?"))
    print("Your answer is",number1+number2)
  if operation=="-":
    number1=float(input("What is your first number?"))
    number2=float(input("What is your second number?"))
    print("Your answer is",number1-number2)
  if operation=="*":
    number1=float(input("What is your first number?"))
    number2=float(input("What is your second number?"))
    print("Your answer is",number1*number2)
  if operation=="/":
    number1=float(input("What is your dividend?"))
    number2=float(input("What is your divisor?"))
    print("Your answer is",number1/number2)
  if operation=="^":
    number1=float(input("What is your base?"))
    number2=float(input("What is your power?"))
    print("Your answer is",number1**number2)
  if operation=="√":
    number1=float(input("What is your radicand?"))
    number2=float(input("What is the power of your root?"))
    print("Your answer is",number1**(1/number2))
  if operation=="%":
    number1=float(input("What is your percent?"))
    number2=float(input("What is the value started with?"))
    print("Your answer is",number1*number2/100)
  if operation=="!":
    x=int(input("Insert a number"))
    factorial(x)
  if operation=="Pythagorean theorem":
    pyth()
  if operation=="Quadratic Formula":
    quad()
  if operation=="Compound Interest":
    compint()
