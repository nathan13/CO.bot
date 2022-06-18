from email.mime import image
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
        if verify(name) == 1:
            pyautogui.click(local)
           

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


#OK
def click_verify(a:str,b:int,c:str,d:int):
    '''Click and verify next step
       -params: a = Where to click
                b = 1 -- Search a Image
                    0 -- Click directly
                c = Next Step
                d = 1 -- If image found
                    0 -- If image not found
    '''
    while True:
        print(a)            
        if b == 1:
         Find_Click(a)
        elif b == 0:
            pyautogui.click(a)
        print(a)

        if d == 1:
            for vv in range(10):
                time.sleep(0.01)
                if verify(c) == 1:
                    return 
        elif d == 0:
            for vv in range(10):
                time.sleep(0.01)
                if verify(c) == 0:
                    return


time.sleep(2)
ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Tower Of Mystery"
os.chdir(ImagePath)



click_verify("towerofmystery10.png",1,"towerofmystery10.png",0)

'''pyautogui.move(0,-200)
NPC_position = pyautogui.position()'''
