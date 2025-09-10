import pyautogui
import time

x_pad = 77
y_pad = 163


class Cord:
    f_shrimp = (273, 547)
    f_rice = (343, 543)
    f_nori = (277, 607)
    f_roe = (339, 603)
    f_salmon = (277, 671)
    f_unagi = (340, 670)
    
    phone = (911, 567)
    
    menu_toppings = (863, 474)
    
    t_shrimp = (798, 418)
    t_nori = (890, 418)
    t_roe = (798, 480)
    t_salmon = (890, 480)
    t_unagi = (798, 545)
    t_exit = (914, 542)
    
    menu_rice = (861, 502)
    buy_rice = (856, 485)
    
    delivery_norm = (799, 499)
    

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
        pyautogui.click(Cord.f_rice)  # 1 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        pyautogui.click(Cord.f_roe)  # 1 roe
        foldMat()
        time.sleep(1.5)
    
    elif food == "onigiri":
        pyautogui.click(Cord.f_rice, clicks=2, interval=0.1) # 2 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        foldMat()
        time.sleep(1.5)
        
    elif food == "gunkan":
        pyautogui.click(Cord.f_rice)  # 1 rice
        pyautogui.click(Cord.f_nori)  # 1 nori
        pyautogui.click(Cord.f_roe, clicks=2, interval=0.1)  # 2 roe
        foldMat()
        time.sleep(1.5)
    
    
def foldMat():
    pyautogui.click(464, 604) # fold mat
        
        





if __name__ == "__main__":
    print("Switch to the game window. Starting in 2 seconds...")
    time.sleep(2)  # Wait 2 seconds to give time to switch
    # makeFood("onigiri")
    # makeFood("caliroll")
    # makeFood("gunkan")
    clearTables()