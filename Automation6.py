
# application for scheduling mail:

import smtplib as smt
import schedule
import time
import datetime



def Email():
    # create object to call server:
    Server = smt.SMTP('smtp.gmail.com', 587)

    # to connect server:
    Server.ehlo()
    # to start server:
    Server.starttls()
    # to login email:
    Server.login('sender@gmail.com', 'password@gmail.com')  # sender email,pasword =app password of sender email

    # to make sub and body:
    Subject = "Reminder for passport appointment"
    Body = " It's reminder for you your passport appointment will be scheduled on 13th Feb,so please follow the schedule  "
    # email format
    Massage = " Subject:{} \n\n {}".format(Subject, Body)

    # to send email oo particular email adress
    # add multiple emailadress in the list
    To = ['mail@gmail.com',']

    # send mail:
    Server.sendmail('sender@gmail.com', To, Massage)  #sender email
    print("Mail is send at " ,datetime.datetime.now())
    # close server
    Server.quit()


def main():
    print("------Application to Sending of email---------")
    print()

    schedule.every().sunday.at("10:00").do(Email)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
