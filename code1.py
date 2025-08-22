import pyautogui
import time
from PIL import Image, ImageOps, ImageGrab
from numpy import *
from quickGrab import screenGrab
from cord import Cord

x_pad = 77
y_pad = 163


    

def mousePos(cord):
    """Move the cursor to a position relative to the play area."""
    x, y = cord
    pyautogui.moveTo(x_pad + x, y_pad + y)

def startGame():
    """Automates clicking through the game start menus."""
    
    # Location of "Play" button (double click)
    pyautogui.click(600, 537, clicks=2, interval=1)
    time.sleep(5)

    # Location of first menu
    pyautogui.click(600,398)
    time.sleep(0.1)
    
    # Location of second menu
    pyautogui.click(584, 623)
    time.sleep(0.1)

    # Location of third menu
    pyautogui.click(895, 678)
    time.sleep(0.1)

    # Location of fourth menu
    pyautogui.click(595, 595)
    time.sleep(0.1)
    

def clearTables():
    pyautogui.click(339,403)
    pyautogui.click(457,403)
    pyautogui.click(571,403)
    pyautogui.click(685,403)
    pyautogui.click(802,403)
    pyautogui.click(922,403)
    time.sleep(1)
    
    
def makeFood(food):
    if food == "caliroll":
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 1  
        pyautogui.click(Cord.f_rice)  # 1 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        pyautogui.click(Cord.f_roe)  # 1 roe
        foldMat()
        time.sleep(1.5)
    
    elif food == "onigiri":
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1 
        pyautogui.click(Cord.f_rice, clicks=2, interval=0.1) # 2 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        foldMat()
        time.sleep(1.5)
        
    elif food == "gunkan":
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2
        pyautogui.click(Cord.f_rice)  # 1 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        pyautogui.click(Cord.f_roe, clicks=2, interval=0.1)  # 2 roe
        foldMat()
        time.sleep(1.5)
    
    
def foldMat():
    pyautogui.click(464, 604) # fold mat

    

def grab():
    box = (x_pad+1, y_pad+1, x_pad+1047, y_pad+556)
    im = ImageOps.grayscale(ImageGrab.grab(box)) # Converts the image to grayscale
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a
        
        
def buyFood(food):
    if food == "rice":
        pyautogui.click(Cord.phone)
        time.sleep(0.1)
        pyautogui.click(Cord.menu_rice)
        time.sleep(0.1)
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (224, 216, 206, 255): 
            print("Rice is NOT available")
            pyautogui.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)
        else:
            print("Rice is available")
            pyautogui.click(Cord.buy_rice)
            time.sleep(0.1)
            pyautogui.click(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(2.5)

            
    if food == "nori":
        pyautogui.click(Cord.phone)
        time.sleep(0.1)
        pyautogui.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        print("Test")
        time.sleep(0.1)
        if s.getpixel(Cord.t_nori) != (0, 0, 0, 255):
            print("Nori is NOT available")
            pyautogui.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)
        else:
            print("Nori is available")
            pyautogui.click(Cord.t_nori)
            time.sleep(0.1)
            pyautogui.click(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(2.5)
        
        
    if food == "roe":
        pyautogui.click(Cord.phone)
        time.sleep(0.1)
        pyautogui.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        if s.getpixel(Cord.t_roe) != (103, 78, 46, 255):
            print("Roe is NOT available")
            pyautogui.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)
        else:
            print("Roe is available")
            pyautogui.click(Cord.t_roe)
            time.sleep(0.1)
            pyautogui.click(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(2.5)
                


foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}


def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print ('%s is low and needs to be replenished' % i)
                buyFood(i)













if __name__ == "__main__":
    print("Switch to the game window. Starting in 2 seconds...")
    time.sleep(2)  # Wait 2 seconds to give time to switch
    # makeFood("onigiri")
    # makeFood("caliroll")
    # makeFood("gunkan")
    # buyFood("roe")
    # clearTables()
    grab()