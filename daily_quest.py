from multiprocessing.context import assert_spawning
from pickle import NONE
from re import A
from time import sleep, time
from cv2 import CALIB_CB_ACCURACY
import pyautogui, os, time,pygetwindow

global ImagePath
ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img" 
global RollPath
RollPath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"    

#OK
def verify(name:str) -> int:
    '''
        Verify image on screen
        - params: -> name = ImageName.png
        - Returns: -> 1  = Image Found | -> 0  = Image not found
    ''' 
    global local
    local = pyautogui.locateOnScreen(name, confidence=0.9)
    if local != None:
        return 1
    else:
        return 0

#OK
def Find_Click(name:str):
    '''
        Click on local image if found
        - params: name = ImageName.png
    '''
    if verify(name) == 1:
        pyautogui.click(local)

#OK
def Find_Move(name:str):
    '''
        Move to Local Image if found
        - params: name = ImageName.png
    '''
    while True:
        if verify(name) == 1:
            pyautogui.moveTo(local)
            return
           
#OK
def roll():
    '''
        Scroll mouse in a specific location
    '''    

    # Set image path                       
    os.chdir(RollPath)
    
    #Start
    while True:
        if verify("roll.png") == 1:
            pyautogui.moveTo(local)
            pyautogui.mouseDown()
            pyautogui.move(0,-100,duration=0.2)
            pyautogui.mouseUp()  
            os.chdir(ImagePath)
            return

#?
def roll2(a:str,b:int):
    '''
        Scroll mouse in a specific location
        - pararms: a = Image to find | b = 1 roll.png
                                           0 roll2.png
    '''    

    # Set image path                       
    

    if b == 1:
        c = "roll.png"
    elif b == 0:
        c = "roll2.png"

    #Start
    while True:
        os.chdir(ImagePath)
        if verify(a) == 1:
            click_verify(a,1,a,0)
            return
        else:
         os.chdir(RollPath)
         if verify(c) == 1:
            pyautogui.moveTo(local)
            pyautogui.mouseDown()
            pyautogui.move(0,-100,duration=0.2)
            pyautogui.mouseUp()  

#OK
def Find_Roll(name:str,name2:str):                       
    while True:
        if verify(name) == 1:
            kk = local
            click_verify(kk,0,name2,1)
            return
        else:
            os.chdir(RollPath)
            while True:
                if verify("roll.png") == 1:
                    pyautogui.moveTo(local)
                    pyautogui.mouseDown()
                    pyautogui.move(0,-100,duration=0.2)
                    pyautogui.mouseUp()
                    os.chdir(ImagePath)  
                    break


#?            
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

#OK               
def BackToDaily():
    '''
        Back to Daily Quest NPC
    '''
    #set image path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
    os.chdir(ImagePath)

    #start
    while True:
        click_verify(DA_position,0,"daily_button.png",1)
        click_verify("daily_button.png",1,"daily_ok.png",1)
        click_verify("daily_ok.png",1,"daily_ok.png",0)
        pyautogui.click(DA_position)

        #Verify If its over
        for a in range(60):
            time.sleep(0.1)
            if verify("daily_quest.png") == 1:
                return 

#OK
def Bright_Fortune():
        '''
            Complete the "Bright Fortune" quest from Daily Quest NPC
        '''

        #set image path
        global ImagePath
        ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Bright Fortune"
        os.chdir(ImagePath)

        #start
        click_verify("Bright_Fortune.png",1,"Bright_Fortune.png",0)
        time.sleep(2)
        click_verify("bright_fortune_npc.png",1,"bright_fortune_1.png",1)
        click_verify("bright_fortune_1.png",1,"bright_fortune_2.png",1)
        click_verify("bright_fortune_2.png",1,"ok.png",1)
        click_verify("ok.png",1,"ok.png",0)
        while True:
            Find_Move("bright_fortune_3.png")
            pyautogui.move(0,60,0.2)
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(1.2)
            if verify("bright_fortune_4.png") == 1:
                if verify("ok.png") == 1:
                    click_verify("ok.png",1,"ok.png",0)              
            else:
                if verify("ok.png") == 1:
                    click_verify("ok.png",1,"ok.png",0)   
                    break

        click_verify("bright_fortune_5.png",1,"bright_fortune_5.png",0)           
        click_verify("bright_fortune_npc2.png",1,"bright_fortune_end.png",1)
        click_verify("bright_fortune_end.png",1,"bright_fortune_end.png",0)
        BackToDaily()
        print("Bright Fortune Done")
        return

#OK
def Open_Treasure():
    '''
        Complete the "Open Treasure" quest from Daily Quest NPC
    '''

    #set Image Path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Open Treasure"
    os.chdir(ImagePath)

    #start
    click_verify("open_treasure.png",1,"open_treasure_1.png",1)
    click_verify("open_treasure_1.png",1,"open_treasure_2.png",1)
    click_verify("open_treasure_2.png",1,"open_treasure_3.png",1)
    click_verify("open_treasure_3.png",1,"ok.png",1)
    click_verify("ok.png",1,"open_treasure_npc.png",1)  
    click_verify("open_treasure_npc.png",1,"open_treasure_4.png",1)
    click_verify("open_treasure_4.png",1,"open_treasure_4.png",0)
    BackToDaily()
    print("Open Treasure Done")
    return 

#?
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

#OK
def Magnolias_All_Around():
    '''
        Complete the "Magnolias All Around" quest from Daily Quest NPC
    '''

    #Set Image Path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Magnolias All Around"
    os.chdir(ImagePath)

    #Start
    Find_Roll("magnolias_all_around.png","magnolias_all_around2.png")
    click_verify("magnolias_all_around2.png",1,"magnolias_all_around3.png",1)
    click_verify("magnolias_all_around3.png",1,"magnolias_all_around4.png",1) 
    click_verify("magnolias_all_around4.png",1,"magnolias_all_around5.png",1)
    click_verify("magnolias_all_around5.png",1,"ok.png",1)
    click_verify("ok.png",1,"ok.png",0)    
    Bag(1)
    click_verify("magnolias_all_around7.png",1,"magnolias_all_around8.png",1)
    click_verify("magnolias_all_around8.png",1,"ok.png",1)
    click_verify("ok.png",1,"ok.png",0)
    Bag(0)
    click_verify("magnolias_all_around9.png",1,"magnolias_all_around10.png",1)
    click_verify("magnolias_all_around10.png",1,"magnolias_all_around10.png",0)
    BackToDaily()
    print("Magnolias All Around Done")
    return                    

#OK
def Spirit_Beads():
    '''
        Complete the "Spirit Beads" quest from Daily Quest NPC
    '''

    #set image path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Spirit Beads"
    os.chdir(ImagePath)

    #Start
    Find_Roll("spirit_beads.png","spirit_beads2.png")
    click_verify("spirit_beads2.png",1,"ok.png",1)
    click_verify("ok.png",1,"ok.png",0)
    BackToDaily()
    print("Spirit Beads Done")
    return 


#OK
def Heaven_Treasury():
    '''
        Complete the "Heaven Treasury" quest from Daily Quest NPC
    '''

    #set image path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Heaven Treasury"
    os.chdir(ImagePath)

    #Start
    while True:
            Find_Roll("heaven_treasury.png","heaven_treasury2.png")
            click_verify("heaven_treasury2.png",1,"ok.png",1)
            click_verify("ok.png",1,"ok.png",0)
            
            while True:
                if verify("heaven_treasury3.png") == 1:
                    click_verify(local,0,"heaven_treasury3.png",0)
                    break
                elif verify("heaven_treasury4.png") == 1: 
                    click_verify(local,0,"heaven_treasury4.png",0)
                    break
                elif verify("heaven_treasury5.png") == 1:
                    click_verify(local,0,"heaven_treasury5.png",0)
                    break
                elif verify("heaven_treasury6.png") == 1: 
                    click_verify(local,0,"heaven_treasury6.png",0)
                    break
            
            click_verify("heaven_treasury7.png",1,"ok.png",1)
            click_verify("ok.png",1,"heaven_treasury8.png",1)
            click_verify("heaven_treasury8.png",1,"heaven_treasury9.png",1)
            Find_Click("heaven_treasury9.png")   
            click_verify("heaven_treasury9.png",1,"heaven_treasury9.png",0)
            BackToDaily()
            print("Heaven Treasury Done")
            return
        

#OK(ICE DOESNT WORK)
def EverythingHasAPrice():
    '''
        Complete the "Everything has a Price" quest from Daily Quest NPC
    '''

   

    #start
    while True:
        #set image path
        global ImagePath
        ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Everything Has a Price"
        os.chdir(ImagePath)
        if verify("EverythingHasAPrice.png") == 1 or verify("EverythingHasAPrice2.png") == 1:
            while True: 
                if verify("EverythingHasAPrice.png") == 1:
                    click_verify("EverythingHasAPrice.png",1,"EverythingHasAPrice.png",0)
                    break
                else:
                    if verify("EverythingHasAPrice2.png") == 1:
                        click_verify("EverythingHasAPrice2.png",1,"EverythingHasAPrice2.png",0)
                        break
            while True:
                if verify("EverythingHasAPrice_2.png") == 1:
                    click_verify("EverythingHasAPrice_2.png",1,"EverythingHasAPrice_2.png",0)
                    click_verify("EverythingHasAPrice_3.png",1,"EverythingHasAPrice_3.png",0)
                    break
                else:
                    if verify("EverythingHasAPrice_3.png") == 1:
                        click_verify("EverythingHasAPrice_3.png",1,"EverythingHasAPrice_3.png",0)
                        break   

            time.sleep(2)             
            if verify("EverythingHasAPrice_10.png") == 1:
                click_verify("EverythingHasAPrice_10.png",1,"EverythingHasAPrice_12.png",1)
                click_verify("EverythingHasAPrice_12.png",1,"EverythingHasAPrice_12.png",0)
                BackToDaily()
                print("Everything has a Price Done")
                return

            click_verify("EverythingHasAPrice_4.png",1,"EverythingHasAPrice_4.png",0)
            Bag(1) 
            click_verify("EverythingHasAPrice_5.png",1,"EverythingHasAPrice_6.png",1)
            click_verify("EverythingHasAPrice_6.png",1,"EverythingHasAPrice_7.png",1)
            click_verify("EverythingHasAPrice_7.png",1,"EverythingHasAPrice_7.png",0)
            time.sleep(2)
            Bag(0)
            click_verify("EverythingHasAPrice_9.png",1,"EverythingHasAPrice_9.png",0)
            time.sleep(300)
            click_verify(local,0,"EverythingHasAPrice_12.png",1)
            click_verify("EverythingHasAPrice_12.png",1,"EverythingHasAPrice_13.png",1)
            click_verify("EverythingHasAPrice_13.png",1,"EverythingHasAPrice_13.png",0)
            BackToDaily()
        else:
            roll()

#? TRAVOU PROCURANDO A IMAGEM 14 DEPOIS DO PRIMEIRO BOSS
def TowerOfMystery():
    '''
        Complete the "Spirit Beads" quest from Daily Quest NPC
    '''

    #set image path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Tower Of Mystery"
    os.chdir(ImagePath)

    #start
    while True:
            Find_Roll("towerofmystery.png","towerofmystery2.png")
            click_verify("towerofmystery2.png",1,"towerofmystery3.png",1)
            click_verify("towerofmystery3.png",1,"towerofmystery3.png",0)
            time.sleep(2)

            click_verify("towerofmystery4.png",1,"towerofmystery24.png",1)
            if verify("common.png")==1:
                click_verify("common.png",1,"common.png",0)  

            click_verify("towerofmystery6.png",1,"towerofmystery7.png",1)
            click_verify("towerofmystery7.png",1,"towerofmystery8.png",1)
            click_verify("towerofmystery8.png",1,"towerofmystery8.png",0)
            time.sleep(2)
            
            Find_Move("towerofmystery16.png")
            MO_postion = local
            pyautogui.move(0,-200)
            NPC_position = pyautogui.position()

            #repeat
            while True:
                click_verify(NPC_position,0,"towerofmystery20.png",1)

                #IF DONE-
                if verify("towerofmystery21.png") == 1:
                    click_verify("towerofmystery21.png",1,"towerofmystery21.png",0)
                    time.sleep(2)
                    click_verify("towerofmystery22.png",1,"towerofmystery23.png",1)
                    click_verify("towerofmystery23.png",1,"towerofmystery23.png",0)
                    time.sleep(2)
                    BackToDaily()
                    return

                roll2("towerofmystery10.png",0)
                click_verify("towerofmystery10.png",1,"towerofmystery10.png",0)

                #start battle
                pyautogui.moveTo(MO_postion)
                time.sleep(0.5)
                pyautogui.mouseDown()
                pyautogui.move(0,-200,duration= 0.3)
                pyautogui.mouseUp()
                time.sleep(0.5)
                pyautogui.click(MO_postion)
                while True:
                    for vv in range(3):
                        pyautogui.press("1",presses=10,interval= 0.2)

                    if verify("target2.png") == 0:
                        break

                click_verify("ok.png",1,"ok.png",0)
                time.sleep(3)
                click_verify("towerofmystery17.png",1,"towerofmystery12.png",1)
                click_verify("towerofmystery12.png",1,"towerofmystery13.png",1)
                click_verify("towerofmystery13.png",1,"towerofmystery13.png",0)
                time.sleep(1)
                click_verify("towerofmystery14.png",1,"towerofmystery15.png",1)
                click_verify("towerofmystery15.png",1,"towerofmystery15.png",0)
                time.sleep(3)

#OK
def Labyrinth():
    '''
        Complete the "Labyrinth" quest from Daily Quest NPC
    '''
    
    #set image path
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img\Labyrinth"
    os.chdir(ImagePath)

    #start
    click_verify("Labyrinth4.png",1,"Labyrinth4.png",0)
    click_verify("Labyrinth.png",1,"Labyrinth1.png",1)
    click_verify("Labyrinth1.png",1,"Labyrinth1.png",0)
    time.sleep(2)
    Bag(1)
    click_verify("Labyrinth2.png",1,"Labyrinth3.png",1)
    click_verify("Labyrinth3.png",1,"Labyrinth5.png",1)
    click_verify("Labyrinth5.png",1,"Labyrinth5.png",0)
    time.sleep(2)
    Bag(0)
    BackToDaily()
    print("Labyrinth Done")


#?
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

#OK
def Set_Button(a:str,b:str):
    '''
        Set Button position
        - params: a = Arrow name PNG | b = Next step name PNG
    '''
    os.chdir(ImagePath)
    c = None
    while True:
        if verify(a) == 1:
            if c != None:
                pyautogui.click(xxx)

            xxx = local
            pyautogui.click(xxx)
            for vv in range(30):
                time.sleep(0.1)
                if verify(b) == 1:
                    c = xxx
                    click_verify(c,0,b,0)
                    return c
                
#OK
def Bag(a:int):
    '''
        Open and close the bag
        - params: a = 1:Open Bag
                      0:Close Bag
    '''

    global BagPath
    BagPath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
    os.chdir(BagPath)

    if a == 1:
        click_verify(BA_position,0,"bag_button.png",1)
        click_verify("bag_button.png",1,"bag_open.png",1)
    elif a == 0:
        click_verify("UP3.png",1,"UP3.png",0)
        click_verify(BA_position,0,"bag_button.png",0)

    os.chdir(ImagePath)

#OK
def Switch_Window(a:str,b:str):
    '''
        Switch between windows
        - params: a = Windows Title | b = Windows Image Name PNG
    '''
    global ImagePath
    ImagePath = r"C:\Users\Nathan\Documents\Python\Automação\Conquer\img"
    os.chdir(ImagePath)

    while True:
        title = a
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.activate()
        if verify(b) == 1:
            break

#Go To LDPlayer Window (OK)
Switch_Window("LDPlayer","LDPlayer_Window.png")

#Set Daily Arrow Position
DA_position = Set_Button("daily_arrow.png","daily_button.png")

#Set Bag Arrow Position
BA_position = Set_Button("bag_arrow.png","bag_button.png")




#Start Program
BackToDaily()
#Labyrinth()
#Bright_Fortune()
#Open_Treasure()
#Magnolias_All_Around()
#Spirit_Beads()
#Heaven_Treasury()
#EverythingHasAPrice()
TowerOfMystery()











