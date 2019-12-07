import smtplib
s=smtplib.SMTP(host="192.168.56.104",port="25")
s.sendmail("root@localhost","vaishakh183@gmail.com","sdfsd")

#a=[]
#contacts=open("contact.txt","r")
#print(contacts.readlines())
#for i in contacts.readlines():
#    a.append(i)

#print(a)


