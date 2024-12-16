from playsound import playsound
import time
import datetime
import os

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

local_time = datetime.datetime.now()
formato = "%H:%M:%S"
fecha_hora_formateada = local_time.strftime(formato)
print("Fecha y hora formateada:", fecha_hora_formateada)

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds :
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left//3600
        minutes_left = hours_left // 60
        seconds_left = hours_left % 60

        print(f'{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}')
    #playsound('alarm.mp3')
    print(local_time)
    time.sleep(4)
    os.system('clear')
hours = int(input('hora'))
minutes = int(input('Enter the number of minutes : '))
seconds = int(input('Enter the number of seconds : '))
total_seconds = hours*3600 + minutes*60 + seconds

alarm(total_seconds)





