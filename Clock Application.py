from datetime import datetime
import pytz
import time
from google.colab import output
import sys

while True:
  output.clear()
  x=int(input("Would you like to set a timer (1), a stopwatch (2), or see the world clock (3)?"))

  if x==1:
    output.clear()
    hours=int(input("How many hours do you want your timer to be?"))
    output.clear()
    mins=int(input("How many additional minutes do you want your timer to be?"))
    output.clear()
    seconds=int(input("How many additional seconds do you want your timer to be?"))
    output.clear()
    totalseconds= (hours*3600)+(mins*60)+seconds
    while True:
      totalseconds=totalseconds-1
      time.sleep(1)
      output.clear()
      print((totalseconds-(totalseconds%3600))/3600,"Hours",(totalseconds-(totalseconds%60))/60,"Minutes",totalseconds%60,"Seconds left")
      if totalseconds==0:
        output.clear()
        print("Timer done")
        time.sleep(5)
        break

  if x==3:
    while True:
      output.clear()
      print("New York time:", datetime.now(pytz.timezone('America/New_York')).strftime("%m-%d-%Y %H:%M:%S"))
      print("London time:", datetime.now(pytz.timezone('Europe/London')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Mumbai time:", datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Australia time:", datetime.now(pytz.timezone('Australia/Melbourne')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Tokyo time:", datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Paris time:", datetime.now(pytz.timezone('Europe/Paris')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Moscow time:", datetime.now(pytz.timezone('Europe/Moscow')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Rome time:", datetime.now(pytz.timezone('Europe/Rome')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Egypt time:", datetime.now(pytz.timezone('Egypt')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Singapore time:", datetime.now(pytz.timezone('Singapore')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Portugal time:", datetime.now(pytz.timezone('Portugal')).strftime("%m-%d-%Y %H:%M:%S"))
      print("Poland time:", datetime.now(pytz.timezone('Poland')).strftime("%m-%d-%Y %H:%M:%S"))
      time.sleep(1)
      stop=input("Would you like to stop (y if so) or would you like to continue/refresh (press enter if so)?")
      if stop.lower()=='y':
        break
  
  if x==2:
    while True:
      output.clear()
      input("Press Enter to start")
      start_time = time.time()
      output.clear()
      input("Press Enter to stop")
      end_time = time.time()
      output.clear()
      time_lapsed = end_time - start_time
      print((time_lapsed-(time_lapsed%3600))/3600,"Hours",(time_lapsed-(time_lapsed%60))/60,"Minutes",time_lapsed%60,"Seconds passed")
      question=input("Would you like to repeat? (yes=y, no=any other text)")
      if question is not "y":
        break

  n=0
  while n<3:
    ans=input("Do you want to perform more operation yes/no")
    if ans.lower()=='yes':
      break
    if ans.lower()=='no':
      output.clear()
      print("Have a nice day!")
      sys.exit()
    else:
      print("Please try again")
      n=n+1
    if n>=3:
      output.clear()
      print("Limit exceeded, have a nice day!")
      sys.exit()
