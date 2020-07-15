import schedule
import time
import os
import random
import playsound


def job():
    print("DJ Khaled Motivation")
    randomfile = random.choice(os.listdir("./audio"))
    file = 'audio/' + randomfile
    playsound.playsound(file, block=True)


schedule.every(30).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
