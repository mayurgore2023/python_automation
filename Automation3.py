
# application for task schedular:

import schedule
import time
import datetime

def Task_Minute():
    print("Task based on minutes gets schedule at :",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour get scheduled at :",datetime.datetime.now())

def Task_Day():
    print("Task based on day gets schedule at:",datetime.datetime.now())


def main():
    print("Inside task schedule")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().tuesday.at("20:18").do(Task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()
