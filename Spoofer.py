#------------------------------------+
# This tool is..                     |   
#   Developed by #Canihelpyou        |
#   For send spoofed mms worldwide.. |
#   Education purposes only!!        |
#   { By changing deverloper's       |
#     codename you don't make a      |
#     Hacker!!! } Remember!!         |                           
#------------------------------------+

# banners..lol...
bold="\033[1m"
banner= """ 
              _____                    __          
             / ____|                  / _|         
            | (___  _ __   ___   ___ | |_ ___ _ __ 
             \___ \| '_ \ / _ \ / _ \|  _/ _ \ '__|
             ____) | |_) | (_) | (_) | ||  __/ |   
            |_____/| .__/ \___/ \___/|_| \___|_|   
                   | |                                   
                   |_|  </> Code By : #canihelpyou    
                            Version : 1.0.2
                                             
                                             
"""

# import all stuff that we need
from termcolor import colored
import smtplib 
import getpass
import sys

# print banner...
print colored(bold+banner,"green")


# Define functions.... 

def mail_login():
   global server
   # Establish a secure session with outgoing SMTP server using your account
   password=getpass.getpass("[$] Email Password:")
   server = smtplib.SMTP( "mail.messagingengine.com", 587 )
   server.starttls()
   server.login( '<email address>', password )
   print colored('Server Connected!', 'green')
   

def mail_config():

   global from_
   global to
   global text
   global message

   # Getting from ,to and message 
   from_=str(raw_input("[$] From(spoofed):"))
   to=str(raw_input("[$] To :"))
   text = str(raw_input("[$] Message:"))

   
   # FailSafe mode for absolute receving..
   print colored("\nIf there is any MMS config trouble in your recevier's device, \nactive FailSafe mode.\nThen we will copy message body to subject.\n ","yellow")
   failsafe=raw_input("[$] Do you want to active FailSafe mode?(y/n):")
   if failsafe =="y" or failsafe=="Y" or failsafe=="yes" or failsafe=="Yes":
      subject=text
   else:
      subject=""
   message = 'Subject: %s\n\n%s' % (subject, text)


   

def mail_confirm():

   # Display from to and message to user 
   print "\n\tFrom    :",colored(from_,"red")
   print "\tTo      :",colored(to,"red")
   print "\tMessage :",colored(text,"red")
   print "\n"
   pause=raw_input("Press Return to continue...")


#############################################
## Global process..
#############################################
try: 

   # call main_login()
   mail_login()
    
   # Asking user does he need to send a single mms or more....
   print "\n1.Single MMS"
   print "2.Mass MMS attack\n"
   choice=raw_input("[$] Choose:")

   if choice=="1":
     
      while True:
         # here we call mail_config() for send single mms.. its simple
         mail_config()
      
         # confirm again!!
         mail_confirm()


         # Send mail and dispaly sent..
         server.sendmail( from_, to, message)
         print colored('Sent!', 'green')

  
   # if user wants to do a mass mms attack we have ready!
   if choice=="2":
      #Little advice
      print colored("\nSave your number list as 'num.txt' in /root\nWhen ask 'to', press Return\n","yellow")

      # we are calling 
      mail_config()
      
      # Do some file  handling
      num_file=open("/root/num.txt")
      nums=num_file.readlines()
      to= "/root/num.txt"

      # confirm again!!
      mail_confirm()
    
      # int mms_count for count sent mms.
      mms_count=0
      for num in nums:
         num_ok=num.strip()
         #send continously..
         server.sendmail( from_, num_ok, message)
         print colored('Sent to:','green') , colored(num_ok ,"green")
         mms_count+=1
      print colored("\nSuccessfully sent","green"),colored(mms_count,"green"),colored("messages....","green")


except KeyboardInterrupt:
        print colored("\nExiting program .. \n\n","green")
        sys.exit()






