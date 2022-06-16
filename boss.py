from pickle import NONE
from pickletools import pyunicode
from threading import local
from time import sleep, time
from operator import truediv
from turtle import position
import pyautogui, os, time



caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
os.chdir(caminho)
monster_position = 0

def select_target():      
    while True:
        if verify("monster2.png")==1:
            pyautogui.moveTo(local)
            pyautogui.mouseDown()
            pyautogui.move(0,270)
            pyautogui.mouseUp()  
            global monster_position 
            monster_position = pyautogui.position()
            print("Monster Found (Select Target)")
            return 1
        else:
            print("Monster Not Found (Select Target)")   
            return 0
        


def skill4():
    #verify skill 4
    global local
    while True:
        local = pyautogui.locateCenterOnScreen("skill4.png")
        if local != None:
            print("skill 4 Up")
            if verify("monster3.png")==1:
                pyautogui.moveTo(local)
                pyautogui.move(0,200)
                global monster_position
                monster_position = pyautogui.position()
            else:
                pyautogui.moveTo(monster_position)
            
            pyautogui.press("4")
            pyautogui.mouseDown()
            pyautogui.move(100,0)
            pyautogui.mouseUp()
            time.sleep(1)
        else:
            print("skill 4 Off")
            break
     
def verify(name):
    arquivo = name
    global local
    local = pyautogui.locateCenterOnScreen(arquivo, confidence=0.9)
    if local != None:
        return 1
    else:
        return 0

def verify_Empty_Energy():
    arquivo = 'empty_energy.PNG'
    global local
    local = pyautogui.locateCenterOnScreen(arquivo)
    if local != None:
        return 1
    else:
        return 0


def Full_Energy_Battle():
    print("Full Energy Up")
    while True:
        if verify("target.png") == 1 and verify_Empty_Energy() == 0:
            pyautogui.press("3",presses= 20,interval=0.1)
        else:
            print("Full Energy Off")
            break

def Empty_Energy_Battle():
    print("Empty Energy Up")
    while True:
        if verify("target.png") == 1 and verify("full_energy.png") == 0:
            skill4()
            pyautogui.click(monster_position,clicks=3)
        else:
            print("Empty Energy Off")
            break
def verify_ok():
    if verify("ok.png")==1:
        pyautogui.click(local)
        print("Ok found!") 
        select_target()
        skill4()
        return 1
    else:
        return 0



'''#battle tower 
while True:     
    if verify("target2.png") == 1:
        time.sleep(4)
        while True:
            if select_target() == 1:
                pyautogui.click()
                break

        while True:
            pyautogui.press("1",presses=100,interval=0.1)
            if verify("ok.png") == 1 or verify("target2.png") == 0 :
                pyautogui.click(local)
                break
    else:
        break'''






'''''
while True:
    select_target()
    if verify("ok.png")!= 1:
        if verify("target.png") == 1:
            while True:
                if verify("target.png") == 1 and verify_Empty_Energy() == 0:
                    skill4()
                    pyautogui.press("3",presses= 50)
                else:
                    if verify("target.png") == 1:
                        while True:
                            if verify("target.png") == 1 and verify("full_energy.png") == 0:
                                skill4()
                                pyautogui.click(monster_position)
                                pyautogui.click(monster_position)
                            else:
                                break
                    else:
                        break
    else:
        pyautogui.moveTo(local)
        pyautogui.click()
        select_target()
'''
        




    





   
    
        