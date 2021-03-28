import pyautogui # pylint: disable=import-error
import random

# like-button location safari: x=980 y=750
# not_like-button location safari: x=830 y=750

def run():
    while(True):
        random1 = random.random()
        if random1 > 0.30:
            like()
            handle_match()
        else:
            not_like()
        




def like():
    #move to like heart button
    pyautogui.moveTo(980, 750, 2)
    pyautogui.sleep(0.5)
    #press mouse
    pyautogui.leftClick()
    
    pyautogui.sleep(2)



def not_like():
    #move to not like button
    pyautogui.moveTo(830, 750, 2)
    pyautogui.sleep(0.5)
    #press mouse
    pyautogui.leftClick()
    
    pyautogui.sleep(2)


def handle_match():
    pyautogui.sleep(2)
    #screenshot and check if match happened
    #if no: return
    #if yes: press x button to close match

pyautogui.sleep(2)
run()
