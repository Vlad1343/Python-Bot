from PIL import ImageGrab
import os
import time

def screenGrab():
    time.sleep(5)  # Wait 5 seconds before taking the screenshot
    
    im = ImageGrab.grab()
    box = (152, 324, 2248, 1422)  # Define the bounding box (left, upper, right, lower)
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    im.save(os.path.join(os.getcwd(), 'screenshot.png'), 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
