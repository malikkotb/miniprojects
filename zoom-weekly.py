import time
import schedule
import pyautogui as pg

def start_meeting(meeting_id, passcode):
    pg.hotkey('command')
    pg.hotkey('command', 'space')
    pg.typewrite('Yoom') # Y cause of the german keyboard
    pg.keyDown('enter')
    time.sleep(3) # wait to load
    pg.hotkey('command', 'J')
    pg.typewrite(meeting_id)
    pg.keyDown('enter')
    time.sleep(1)
    pg.typewrite(passcode)
    pg.keyDown('enter')


schedule.every().day.at("10:30").do(start_meeting(12313123123, 123456))
