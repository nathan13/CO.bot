from pickle import NONE
from time import sleep, time
from operator import truediv
import pyautogui, os, time

caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
os.chdir(caminho)

def verify(name):
    arquivo = name
    global local
    local = pyautogui.locateOnScreen(arquivo, confidence=0.9)
    if local != None:
        return 1
    else:
        return 0

def Find_Click(name):
    while True:
        if verify(name) == 1:
            pyautogui.click(local)
            break

def Find_Move(name):
    while True:
        if verify(name) == 1:
            pyautogui.moveTo(local)
            break

def roll():                                
    while True:
        if verify("roll2.png") == 1:
            pyautogui.moveTo(local)
            pyautogui.mouseDown()
            pyautogui.move(0,-100,duration=0.2)
            pyautogui.mouseUp()  
            return 0

caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img "
os.chdir(caminho)

'''#press 1 many times
while True:
    pyautogui.press("1",presses=100,interval=0.1)'''

'''#up with double XP
while True:
    if verify("ok.png") == 1:
        Find_Click("ok.png")

    time.sleep(2)

    while True:
        pyautogui.press("b")
        time.sleep(1)
        if verify("UP1.png") == 1:
            break
    
    while True:
        Find_Click("UP1.png")
        time.sleep(1)
        if verify("UP2.png") == 1:
            break

    while True:
        Find_Click("UP2.png")
        time.sleep(1)
        if verify("UP2.png") == 0:
            break
    
    while True:
        Find_Click("UP3.png")
        time.sleep(1)
        if verify("UP3.png") == 0:
            break
    print("ok")
    time.sleep(3600)'''

