import time
import smtplib
import random
wordList=[]

engfile = open("EnglishWords.txt","r", encoding="utf-8")
for i in engfile:
    i = i.strip("\n")
    i = i.split(",")
    wordList.append(i)
engfile.close()

def sending_words():

    sender_email = "sender_email"
    rec_email = "reciever_email"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email, "sender_email_password")
    print("login success!")

    for i in wordList:

        message ="""
WORD: {}

DESCRIPTION: {}

EXAMPLES:

{}
{}
        """.format(i[0],i[1],i[2],i[3])
        random.shuffle(wordList)
        server.sendmail(sender_email,rec_email,message)
        time.sleep(5)
    print("email has been sent to", rec_email)

sending_words()