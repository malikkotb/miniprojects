import time
import schedule
import pyautogui as pg

def play_liked_songs():
    pg.hotkey('command')
    pg.hotkey('command', 'space')
    pg.typewrite('Spotifz') # z cause of the german keyboard
    pg.keyDown('enter')
    time.sleep(2)
    pg.hotkey('command', 'L')
    time.sleep(2)
    pg.typewrite('Drake')
    time.sleep(1)
    pg.keyDown('enter')
    pg.hotkey('tab', 'tab')
    pg.keyDown('enter')
    time.sleep(1)
    pg.hotkey('command', 'S') # shuffle

    #pg.hotkey('command', 'w') # close window

play_liked_songs()
#schedule.every().day.at("8:30").do(play_liked_songs())
