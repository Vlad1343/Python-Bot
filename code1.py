import pyautogui
import time

x_pad = 77
y_pad = 163

def mousePos(cord):
    """Move the cursor to a position relative to the play area."""
    x, y = cord
    pyautogui.moveTo(x_pad + x, y_pad + y)

def startGame():
    """Automates clicking through the game start menus."""

    print("Switch to the game window. Starting in 5 seconds...")
    time.sleep(5)  # Wait 5 seconds to give time to switch

    # Location of "Play" button (double click)
    pyautogui.click(600, 537, clicks=2, interval=1)
    time.sleep(5)

    # Location of first menu
    pyautogui.click(600,398)
    time.sleep(0.5)
    
    # Location of second menu
    pyautogui.click(584, 623)
    time.sleep(0.5)

    # Location of third menu
    pyautogui.click(895, 678)
    time.sleep(0.5)

    # Location of fourth menu
    pyautogui.click(595, 595)
    time.sleep(0.5)



if __name__ == "__main__":
    startGame()