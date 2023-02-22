
# Application for task schedular

import time
import datetime
import schedule


def Fun():
    print("Call to HR",datetime.datetime.now())


def main():

    print("Inside task shedular")
    print("Current time is:",datetime.datetime.now())

    schedule.every(1).minute.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
