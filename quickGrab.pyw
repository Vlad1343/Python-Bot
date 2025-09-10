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
from code1 import Cord

x_pad = 77
y_pad = 163


def screenGrab():
    time.sleep(3)  # Wait 3 seconds before taking the screenshot
    
    b1 = (x_pad+1, y_pad+1, x_pad+1047, y_pad+556)  # Define the bounding box (left, upper, right, lower)
    im = ImageGrab.grab(b1)

    # im.save(os.path.join(os.getcwd(), 'screenshot.png'), 'PNG')
    return im


def test():
    img = screenGrab()
    pixel = img.getpixel(Cord.buy_rice)
    print(f"Pixel color at shrimp button: {pixel}")


def main():
    im = screenGrab()
    # pass



if __name__ == '__main__':
    time.sleep(2)
    main()

"""
(0, 0, 0, 255) - nori
(103, 78, 46, 255) - roe
(0, 0, 0, 255) - salmon
(102, 158, 217, 255) - shrimp
(241, 193, 128, 255) - unagi
(224, 216, 206, 255) - buy rice
"""