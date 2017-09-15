"""
Alarm Clock

A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
"""
import pygame
import datetime
import time

def play_sound():
    """
    Open pygame window initially :(
    Sound plays for 10 sec

    :return: void
    """
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode((100, 200))
    pygame.mixer.music.load('../../resources/Wake-up-sounds.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    clock.tick(5)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(5)
    pygame.mixer.music.stop()
    pygame.display.quit()

def get_input_time():
    option = int(input("Enter after what time should alarm start [1] or at what time [2]?"))
    while option != 1 and option != 2:
        option = int(input("Choose one option: after what time should alarm start [1] or at what time [2]?"))
        print(option)
    if option==1:
        days = int(input("Enter days: "))
        hours= int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        return datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    else:
        date_entry = input('Enter a date in YY-MM-DD-hh-mm-ss format: ')
        year, month, day, hours, minutes, seconds= map(int, date_entry.split('-'))
        date_to_wakeup = datetime.datetime(year, month, day, hours, minutes, seconds)
        return date_to_wakeup - datetime.datetime.now()



if __name__ == '__main__':
    after_time_alarm = get_input_time()
    start_time_alarm = datetime.datetime.now()
    while (start_time_alarm + after_time_alarm) > datetime.datetime.now():
        time.sleep(1)
    play_sound()
