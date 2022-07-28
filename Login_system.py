import re
import csv
import pandas as pd
import os

print('****Registration & Login System**** \n')
print("Press 1 for Registration \nPress 2 for Login \nPress 3 if Forgot Password\n")
choice=input("Enter Your Choice: ")

reg_user=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
reg_pswd=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'

reg_user_fl = False
reg_pswd_fl = False
login_fl = False
search_fl = False

if choice=="1":
  userName=input("Enter your email/username here: ")
  if (re.fullmatch(reg_user,userName)):
    reg_user_fl = True
  else:
    print("Invalid Email or User name")

  paswd=input("Enter your passward here: ")
  if (re.fullmatch(reg_pswd,paswd)):
    reg_pswd_fl = True
  else:
    print("Incorrect Password")
     
  if reg_user_fl == True and reg_pswd_fl == True:
    if (os.stat("reg_log.csv").st_size==0):
      with open("reg_log.csv", 'a',newline='')as f1:
        wr=csv.writer(f1)
        wr.writerow(["Email/Username","Password"])
        wr.writerow([userName,paswd])
      f1.close()
    else:
      with open("reg_log.csv", 'a',newline='') as f1:
        wr=csv.writer(f1)
        wr.writerow([userName,paswd])
      f1.close()
    print("Registration Successful...")
 
elif choice=="2":
  log_user=input("Enter Email/Username:  ")
  log_pswd=input("Enter Passward: ")
  with open('reg_log.csv','r') as f1:
    read_obj=csv.reader(f1)
    for row in read_obj:
      if [log_user,log_pswd]==row:
        login_fl = True        
  if login_fl == True:
    print("You are Logged in...!")
  else:
    print('"Login Failed!!!!"\n"Please Register..."')
  f1.close()

elif choice=="3":
  forgot_user=input("Enter Email/Username to Search:  ")
  with open('reg_log.csv','r') as f1:
    read_obj=csv.reader(f1)
    for i in read_obj:
      if i[0]==forgot_user:
        search_fl = True
        print("Password for User:{} is:{} ".format(i[0],i[1]))
    if search_fl == False:
      print("User not Registered\nPlease Register")
  f1.close()

else:
  print("Invalid Choice!!!!\nChoose 1 or 2 or 3")