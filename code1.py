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
    mousePos((600, 537))
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(3)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(7)

    # Location of first menu
    mousePos((595, 398))
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    # Location of second menu
    mousePos((603, 621))
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    # Location of third menu
    mousePos((894, 673))
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    # Location of fourth menu
    mousePos((598, 590))
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

if __name__ == "__main__":
    startGame()