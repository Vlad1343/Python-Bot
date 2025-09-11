

from PIL import ImageGrab
import os
import time
from cords import Cord

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

