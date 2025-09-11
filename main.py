import pyautogui
import time
from PIL import ImageGrab, ImageOps
from quickGrab import screenGrab
from cords import Cord

pyautogui.FAILSAFE = True

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


# Each tuple is the rectangular area where the customer bubble appears.
seat_areas = [
    (264, 231, 335, 253),
    (378, 233, 450, 254),
    (494, 231, 565, 251),
    (609, 231, 680, 253),
    (725, 231, 797, 252),
    (839, 233, 913, 253),
]


# Mapping of grayscale sums to sushi types
sushiTypes = {
    317063: "onigiri",
    372787: "caliroll",
    332489: "gunkan",
}


def get_image_sum(box):
    """Take a screenshot of the given box, convert to grayscale, and return the sum of all pixel values."""
    img = ImageGrab.grab(box)
    gray = ImageOps.grayscale(img)
    return sum(gray.getdata())


def check_seats():
    """Check each seat area, detect which sushi is requested, and return a list of (seat_index, sushiType)."""
    results = []
    for i, box in enumerate(seat_areas, start=1):
        img_sum = get_image_sum(box)

        if img_sum in sushiTypes:
            results.append((i, sushiTypes[img_sum]))  # (seat_number, sushi_name)
        else:
            results.append((i, None))  # None means seat is empty or unknown
    return results


def process_seats():
    """Loop through all seats, print results, and call makeFood() if needed."""
    detections = check_seats()

    for seat_index, sushi in detections:
        if sushi:
            print(f"Seat {seat_index} needs {sushi}")
            makeFood(sushi)  # <-- This function must exist in your code
        else:
            print(f"Seat {seat_index} is empty or unknown sushi")


def check_bubs():
    """Check all 6 seat bubbles, identify requested sushi, and make it if needed."""
    checkFood()  # Make sure we have enough ingredients before starting
    detections = check_seats()  # Returns a list of (seat_index, sushi_name or None)

    for seat_index, sushi in detections:
        if sushi:
            print(f"Table {seat_index} is occupied and needs {sushi}")
            makeFood(sushi)
        else:
            print(f"Table {seat_index} is unoccupied or unknown sushi")

        checkFood()  # Check after each table to keep ingredients topped up

    clearTables()  # Clear plates at the end of the cycle

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    import pyautogui
    pyautogui.FAILSAFE = True  # move cursor to top-left to stop script

    print("Switch to the game window. Starting in 3 seconds...")
    time.sleep(3)
    startGame()

    try:
        while True:
            detections = check_seats()  # returns list of (seat_index, sushi_name)
            
            for seat_index, sushi in detections:
                if sushi:
                    print(f"Table {seat_index} needs {sushi}")
                    makeFood(sushi)
                else:
                    print(f"Table {seat_index} is empty or unknown")
                
                checkFood()  # restock if needed
            
            clearTables()  # clear plates
            time.sleep(1.5)

    except pyautogui.FailSafeException:
        print("Stopped by moving mouse to top-left corner.")