from pickle import NONE
from time import sleep, time
from operator import truediv
import pyautogui, os, time

caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
os.chdir(caminho)

def verify(name):
    arquivo = name
    global local
    local = pyautogui.locateCenterOnScreen(arquivo, confidence=0.9)
    if local != None:
        return 1
    else:
        return 0

def Find_Click(name):
    while True:
        if verify(name) == 1:
            pyautogui.click(local)
            break

def Combat_Tower():
    while True:
        if verify("ok.png") == 0:
            pyautogui.press("3",presses = 3)
            pyautogui.click()               
        else:
            Find_Click("ok.png")
            Find_Click("towerofmystery17.png")
            Find_Click("towerofmystery12.png")
            Find_Click("towerofmystery13.png")
            Find_Click("towerofmystery14.png")
            Find_Click("towerofmystery15.png")
            return 0

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

time.sleep(2)
caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Bright Fortune"
os.chdir(caminho)
while True:
    Find_Click("bright_fortune_3.png")
    
    time.sleep(2)
    if verify("bright_fortune_4.png") == 1:
        if verify("ok.png") == 1:
            pyautogui.click(local)                
    else:
        if verify("ok.png") == 1:
            pyautogui.click(local)
            break