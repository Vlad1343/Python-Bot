""" 
All coordinates assume a screen resolution of 3456x2234, and Chrome 
maximized with the Bookmarks Toolbar enabled. 
Down key has been hit 4 times to center play area in browser. 
You can find your own coordinates using the code in soft.py.
Or you can readjust the code and use image recognition to find buttons

x_pad = 156 
y_pad = 345 
Play area = x_pad+1, y_pad+1, 796, 825 
Sushi Go Round: https://www.crazygames.com/game/sushi-go-round
"""

from PIL import ImageGrab
import os
import time
from cord import Cord

x_pad = 77
y_pad = 163



def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1047, y_pad+556)  # Define the bounding box (left, upper, right, lower)
    im = ImageGrab.grab(box)

    im.save(os.path.join(os.getcwd(), 'screenshot.png'), 'PNG')
    return im


def test():
    img = screenGrab()
    pixel = img.getpixel(Cord.buy_rice)
    print(f"Pixel color at shrimp button: {pixel}")




if __name__ == '__main__':
    time.sleep(2)
    screenGrab()

