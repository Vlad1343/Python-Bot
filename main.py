import pyautogui
import time
from PIL import ImageGrab, ImageOps
from quickGrab import screenGrab
from cords import Cord

# --- GLOBAL CONFIGURATION ---
x_pad = 77
y_pad = 163

# Initial food inventory
foodOnHand = {
    'shrimp': 5,
    'rice': 10,
    'nori': 10,
    'roe': 10,
    'salmon': 5,
    'unagi': 5
}

# --- HELPER FUNCTIONS ---

def mousePos(cord):
    """Move the cursor to a position relative to the play area."""
    x, y = cord
    pyautogui.moveTo(x_pad + x, y_pad + y)


def click(pos, clicks=1, interval=0.1):
    """Click a given position (Cord or tuple) with optional click count."""
    pyautogui.click(pos, clicks=clicks, interval=interval)
    time.sleep(0.1)

# --- GAME AUTOMATION FUNCTIONS ---

def startGame():
    """Automates clicking through the game start menus."""
    click((600, 537), clicks=2, interval=1)
    time.sleep(5)

    for coord in [(600, 398), (584, 623), (895, 678), (595, 595)]:
        click(coord)


def clearTables():
    """Clear all 6 tables by clicking their plates."""
    table_coords = [(339, 403), (457, 403), (571, 403),
                    (685, 403), (802, 403), (922, 403)]
    for coord in table_coords:
        click(coord)
    time.sleep(1)


def foldMat():
    """Click the mat to fold sushi."""
    click((464, 604))


def makeFood(food):
    """Prepare sushi based on the given recipe name."""
    recipes = {
        "caliroll": [("rice", 1, Cord.f_rice), ("nori", 1, Cord.f_nori), ("roe", 1, Cord.f_roe)],
        "onigiri": [("rice", 2, Cord.f_rice), ("nori", 1, Cord.f_nori)],
        "gunkan": [("rice", 1, Cord.f_rice), ("nori", 1, Cord.f_nori), ("roe", 2, Cord.f_roe)]
    }

    if food not in recipes:
        print(f"Unknown recipe: {food}")
        return

    for ingredient, count, cord in recipes[food]:
        foodOnHand[ingredient] -= count
        click(cord, clicks=count, interval=0.1)

    foldMat()
    time.sleep(1.5)


def grab():
    """Take a screenshot of the play area and return grayscale sum."""
    box = (x_pad+1, y_pad+1, x_pad+1047, y_pad+556)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = sum(im.getdata())
    print(f"Screen sum: {a}")
    return a


def buyFood(food):
    """Generalized function to order ingredients if available."""
    phone_menus = {
        "rice": Cord.menu_rice,
        "nori": Cord.menu_toppings,
        "roe": Cord.menu_toppings
    }
    buy_buttons = {
        "rice": Cord.buy_rice,
        "nori": Cord.t_nori,
        "roe": Cord.t_roe
    }
    unavailable_colors = {
        "rice": (224, 216, 206, 255),
        "nori": (0, 0, 0, 255),
        "roe": (103, 78, 46, 255)
    }

    if food not in phone_menus:
        print(f"Unknown food type: {food}")
        return

    click(Cord.phone)
    click(phone_menus[food])
    s = screenGrab()

    if s.getpixel(buy_buttons[food]) != unavailable_colors[food]:
        print(f"{food.capitalize()} is NOT available")
        click(Cord.t_exit)
        time.sleep(1)
        buyFood(food)  # Retry later
    else:
        print(f"{food.capitalize()} is available")
        click(buy_buttons[food])
        click(Cord.delivery_norm)
        foodOnHand[food] += 10
        time.sleep(2.5)


def checkFood():
    """Check if core ingredients are running low and restock them."""
    for item in ("rice", "nori", "roe"):
        if foodOnHand[item] <= 4:
            print(f"{item} is low and needs to be replenished")
            buyFood(item)




# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("Switch to the game window. Starting in 2 seconds...")
    time.sleep(2)
    startGame()
    # makeFood("onigiri")
    # clearTables()
    # checkFood()