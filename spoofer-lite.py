#
# spoofer-lite.py
# -Lite version for Spoofer.py- 
# 
# By 	: @_hddananjaya
#


import smtplib

# define variables

mailServer = ""
serverPort = 
email = ""
password = ""

# print banner
print (""" 
-------------------------------
	spoofer-lite
-Lite version for Spoofer.py-
-------------------------------
""")


server = smtplib.SMTP( mailServer, serverPort )
server.starttls()
server.login( email, password )
print ("Server Connected!")

def main():

   # Getting from ,to and message 
   from_=str(input("\n[$] From(spoofed):"))
   #to=str(raw_input("[$] To :"))
   to = ""
   #to = ""
   text = str(input("[$] Message:"))

   subject=text
   message = "Subject: %s\n\n%s" % (subject, text)


   # Send mail and dispaly sent..
   server.sendmail( from_, to, message)
   print ("Sent!")


while __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
        print ("\nExiting program..")









