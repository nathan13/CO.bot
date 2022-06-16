from gettext import find
from pickle import NONE
from platform import python_branch
from ssl import VerifyFlags
from threading import local
from time import sleep, time
from operator import truediv
from cv2 import dnn_DetectionModel
import pyautogui, os, time,pygetwindow




caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
os.chdir(caminho)

def verify(name:str) -> int:
    '''Verify image on screen
        -> params: name = Image Name
        -> Returns: 1  = Image Found
                    0  = Image not found
    ''' 
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
            if verify(name) == 0:
                break

def Find_Move(name):
    while True:
        if verify(name) == 1:
            pyautogui.moveTo(local)
            break

def roll():     
    RollPath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"                           
    os.chdir(RollPath)
    while True:
        if verify("roll.png") == 1:
            pyautogui.moveTo(local)
            pyautogui.mouseDown()
            pyautogui.move(0,-100,duration=0.2)
            pyautogui.mouseUp()  
            os.chdir(ImagePath)
            return 0
            
def Combat_Tower():
    while True:
        Find_Click("auto.png")
        autobutton = local
        if verify("ok.png") == 0:
            #pyautogui.press("3",presses = 3)
            #pyautogui.click() 
            print("a")  
                        
        else:
            pyautogui.click(autobutton)
            Find_Click("ok.png")
            Find_Click("towerofmystery17.png")
            Find_Click("towerofmystery12.png")
            Find_Click("towerofmystery13.png")
            Find_Click("towerofmystery14.png")
            Find_Click("towerofmystery15.png")
            return

#Go To LDPlayer Window
while True:
        title = "LDPlayer"
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.activate()
        if verify("LDPlayer_Window.png") == 1:
            break

#beginnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

def Verify_Click(name):
        '''Verify image on screen
            -> params: name = Image Name
            -> Returns: 1  = Image Found
                        0  = Image not found
        ''' 
        image = name
        global local
        local = pyautogui.locateOnScreen(image, confidence=0.9)
        if local != None:
            while True:
                pyautogui.click(local)
                time.sleep(0.2)
                local = pyautogui.locateOnScreen(image, confidence=0.9)
                if local == None:
                    return 1
        else:
            return 0


def BackToDaily():
    #set image path
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
    os.chdir(ImagePath)

    #set DA_Position = Daily Arrow Position
    verify("daily_arrow.png")
    global DA_position
    DA_position = local

    #start
    while True:
        Verify_Click("daily_arrow.png")
        Verify_Click("daily_button.png")
        if Verify_Click("daily_ok.png") == 1:
            pyautogui.click(DA_position)
            #Verify If its over
            for a in range(6):
                time.sleep(1)
                if verify("daily_quest.png") == 1:
                    return 


def Bright_Fortune():
            global caminho
            caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Bright Fortune"
            os.chdir(caminho)
            Find_Click("Bright_Fortune.png")
            time.sleep(2)
            pyautogui.click(DA_position)
            Find_Click("bright_fortune_npc.png")
            Find_Click("bright_fortune_1.png")
            Find_Click("bright_fortune_2.png")
            Find_Click("ok.png")
            while True:
                Find_Click("bright_fortune_3.png")             
                time.sleep(3)
                if verify("bright_fortune_4.png") == 1:
                    if verify("ok.png") == 1:
                        pyautogui.click(local)                
                else:
                    if verify("ok.png") == 1:
                        pyautogui.click(local)
                        break
                
            Find_Click("bright_fortune_npc2.png")
            time.sleep(1)
            Find_Click("bright_fortune_end.png")
            return 0

def Open_Treasure():
    #set Image Path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Open Treasure"
    os.chdir(ImagePath)
    #start
    Find_Click("open_treasure.png")
    Find_Click("open_treasure_1.png")
    Find_Click("open_treasure_2.png")
    Find_Click("open_treasure_3.png") 
    Find_Click("ok.png")
    Find_Click("open_treasure_npc.png")     
    Find_Click("open_treasure_4.png") 
    return 0

def Fellow_Fighters():
    global caminho
    caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Fellow Fighters"
    os.chdir(caminho)
    while True:
        if verify("fellow_fighters.png") == 1:
            pyautogui.click(local)
            Find_Click("open_treasure_1.png")
            time.sleep(2)
            pyautogui.click(DA_position)
            Find_Click("fellow_fighters_npc.png")
            Find_Click("fellow_fighters_1.png")  
            Find_Click("fellow_fighters_2.png") 
            Find_Click("ok.png") 
            while True:
                Find_Click("fellow_fighters_3.png")
                time.sleep(1) 
                Find_Click("fellow_fighters_4.png") 
                Find_Click("ok.png")

        else:        
            roll()

def Magnolias_All_Around():
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Magnolias All Around"
    os.chdir(ImagePath)
    while True:
        if verify("magnolias_all_around.png") == 1:
            pyautogui.click(local)
            Find_Click("magnolias_all_around2.png")   
            Find_Click("magnolias_all_around3.png") 
            Find_Click("magnolias_all_around4.png") 
            Find_Click("magnolias_all_around5.png")
            Find_Click("ok.png")      
            pyautogui.press("b")  
            Find_Click("magnolias_all_around7.png")
            Find_Click("magnolias_all_around8.png")
            Find_Click("ok.png")
            Find_Click("magnolias_all_around11.png")
            Find_Click("magnolias_all_around9.png")
            Find_Click("magnolias_all_around10.png")
            return 0                          
        else:
            roll()

def Spirit_Beads():
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Spirit Beads"
    os.chdir(ImagePath)
    while True:
        if verify("spirit_beads.png") == 1:
            pyautogui.click(local)
            Find_Click("spirit_beads2.png")
            Find_Click("ok.png")
            return 0
        else:
            roll()

def Heaven_Treasury():
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Heaven Treasury"
    os.chdir(ImagePath)
    while True:
        if verify("heaven_treasury.png") == 1:
            pyautogui.click(local)
            Find_Click("heaven_treasury2.png")
            Find_Click("ok.png")
            while True:
                if verify("heaven_treasury3.png") == 1:
                    pyautogui.click(local)
                    break
                elif verify("heaven_treasury4.png") == 1: 
                    pyautogui.click(local)
                    break
                elif verify("heaven_treasury5.png") == 1:
                    pyautogui.click(local)
                    break
                elif verify("heaven_treasury6.png") == 1: 
                    pyautogui.click(local) 
                    break
            Find_Click("heaven_treasury7.png")
            Find_Click("ok.png")  
            Find_Click("heaven_treasury8.png")
            Find_Click("heaven_treasury9.png")   
            return 0
        else:
            roll()

def EverythingHasAPrice():

    while True:
        global ImagePath
        ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Everything Has a Price"
        os.chdir(ImagePath)
        if verify("EverythingHasAPrice.png") == 1 or verify("EverythingHasAPrice2.png") == 1:
            while True: 
                if verify("EverythingHasAPrice.png") == 1:
                    pyautogui.click(local)
                    break
                else:
                    if verify("EverythingHasAPrice2.png") == 1:
                        pyautogui.click(local)
                        break
            while True:
                if verify("EverythingHasAPrice_2.png") == 1:
                    pyautogui.click(local)
                    break
                else:
                    if verify("EverythingHasAPrice_3.png") == 1:
                        pyautogui.click(local)
                        break
            time.sleep(1)
            if verify("EverythingHasAPrice_10.png")== 1:
                pyautogui.click(local)
                Find_Click("EverythingHasAPrice_12.png")
                return 0 
            Find_Click("EverythingHasAPrice_4.png") 
            pyautogui.press("b")  
            Find_Click("EverythingHasAPrice_5.png")
            Find_Click("EverythingHasAPrice_6.png")
            Find_Click("EverythingHasAPrice_7.png")
            time.sleep(2)
            Find_Click("EverythingHasAPrice_8.png")
            Find_Click("EverythingHasAPrice_9.png")
            time.sleep(300)
            pyautogui.click(local)
            Find_Click("EverythingHasAPrice_12.png")
            Find_Click("EverythingHasAPrice_13.png")
            BackToDaily()
        else:
            roll()

def TowerOfMystery():
    global caminho
    caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Tower Of Mystery"
    os.chdir(caminho)
    while True:
        if verify("towerofmystery.png") == 1:
            pyautogui.click(local)
            Find_Click("towerofmystery2.png")
            Find_Click("towerofmystery3.png")
            time.sleep(2)
            pyautogui.click(DA_position)
            Find_Click("towerofmystery4.png")
            if verify("towerofmystery5.png")==1:
                pyautogui.click(local)
            Find_Click("towerofmystery6.png")
            Find_Click("towerofmystery7.png")
            Find_Click("towerofmystery8.png")
            while True:
                '''time.sleep(2)
                Find_Move("towerofmystery16.png")
                pyautogui.move(-450,-100)
                pyautogui.click()
                time.sleep(1)
                verify("towerofmystery16.png")
                MO_Postion = local'''
                while True:
                    if verify("towerofmystery9.png") == 1:
                        pyautogui.click(local)
                        break
                    if verify("towerofmystery18.png") == 1:
                        pyautogui.click(local)
                        break
                    if verify("towerofmystery19.png") == 1:
                        pyautogui.click(local)    
                        break
                while True:
                    if verify("towerofmystery10.png") == 1:
                        pyautogui.click(local)
                        if verify("towerofmystery20.png") == 0:
                            break
                    else:  
                        while True:
                            if verify("roll2.png") == 1:
                                pyautogui.moveTo(local)
                                pyautogui.mouseDown()
                                pyautogui.move(0,-100,duration=0.2)
                                pyautogui.mouseUp()  
                                break
                if verify("towerofmystery21.png") == 0:
                   # pyautogui.click(MO_Postion)
                    #pyautogui.mouseDown()
                    #pyautogui.move(0,-150)
                   # pyautogui.mouseUp()
                   # pyautogui.click(MO_Postion)
                    Combat_Tower()
                else:
                    Find_Click("towerofmystery21.png")
                    Find_Click("towerofmystery22.png")
                    Find_Click("towerofmystery23.png")
                    return
                     
        else:
            roll()

def Free_Pack():
    global caminho
    caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Free Pack"
    Find_Click("FreePack.png")
    pyautogui.click(DA_position)
    Find_Click("FreePack1.png")
    Find_Click("FreePack2.png")

def Labyrinth():
    global caminho
    caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Labyrinth"
    os.chdir(caminho)
    Find_Click("Labyrinth4.png")
    pyautogui.click(DA_position)
    Find_Click("Labyrinth.png")
    Find_Click("Labyrinth1.png")
    time.sleep(2)
    pyautogui.press("b")
    while True:
        Find_Click("Labyrinth2.png")
        if verify("Labyrinth3.png") == 1:
            Find_Click("Labyrinth3.png")
            break
    Find_Click("Labyrinth5.png")
    time.sleep(2)
    Find_Click("Labyrinth6.png")

def Devil_Challenge():
    global caminho
    caminho = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Fellow Fighters"
    Find_Click("EndlessTower.png")
    Find_Click("EndlessTower1.png")
    Find_Click("EndlessTower2.png")
    Find_Click("EndlessTower3.png")
    
    Find_Click("DevilChallenge.png")
    Find_Click("DevilChallenge1.png")
    Find_Click("DevilChallenge2.png")
    Find_Click("DevilChallenge.png")
    Find_Click("DevilChallenge3.png")
    Find_Click("DevilChallenge4.png")
    Find_Click("DevilChallenge2.png")
    Find_Click("DevilChallenge5.png")
    Find_Click("DevilChallenge6.png")


    



BackToDaily()
EverythingHasAPrice()

#Magnolias_All_Around()







