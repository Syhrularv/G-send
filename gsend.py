import os, sys, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
###########################################################
#pake pake aja kentod gausah di recode juga ea babyk
###########################################################
GR='\033[37m'
DG='\033[90m'
R='\033[91m'
G='\033[92m'
Y='\033[93m'
B='\033[94m'
PINK='\033[95m'
C='\033[96m'

##############################################################
print DG + "       ___________________________________________"
print "      |                                           |"
print "      |          Author by : @Syhrularv           |"
print "      |                                           |"
print "      |                Thx to :                   |"
print "      |     Python indonesia, google, youtube     |"
print "       \_________________________________________/"
print " "
print "         ______            _____ _______   ______"
print "        / ____/           / ___// ____/ | / / __ \."
print "       / / __   ______    \__ \/ __/ /  |/ / / / /"
print "      / /_/ /  /_____/   ___/ / /___/ /|  / /_/ /"
print "      \____/            /____/_____/_/ |_/_____/"
print GR + "\n "

gimel = raw_input("masukkan gmail lu > ")
pwd = raw_input("masukkan password gmail lu > ")
target = raw_input("masukkan gmail target > ")
pesan = raw_input("masukkan pesan > ")
subjek = raw_input("masukkan subject > ")
jumlah = input("masukkan jumlah pesan > ")

def gsend():
   fromaddr=(gimel)
   toaddr=(target)
   msg =MIMEMultipart()
   msg['from']=fromaddr
   msg['To']=toaddr
   msg['Subject']=(subjek)
   body=(pesan)

   try:
      msg.attach(MIMEText(body,'plain'))
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login((gimel), (pwd))
      for i in range(1, jumlah+1):
         server.sendmail(fromaddr,toaddr, msg.as_string())
         print "\nSending succesfull :)"
      server.quit()
      print "\n[*] DONE NYET!!!"
   except smtplib.SMTPAuthenticationError:
      print "\n[!] username or password lu salah goblok."
      sys.exit()
   except KeyboardInterrupt:
      print "[!] Exiting..."
      sys.exit()

gsend()
