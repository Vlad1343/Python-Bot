# """ 
# All coordinates assume a screen resolution of 3456x2234, and Chrome 
# maximized with the Bookmarks Toolbar enabled. 
# Down key has been hit 4 times to center play area in browser. 
# You can find your own coordinates using the code in soft.py.

# x_pad = 156 
# y_pad = 345 
# Play area = x_pad+1, y_pad+1, 796, 825 
# Sushi Go Round: https://www.crazygames.com/game/sushi-go-round
# """

# from PIL import ImageGrab
# import os
# import time


# x_pad = 77
# y_pad = 163


# def screenGrab():
#     time.sleep(5)  # Wait 5 seconds before taking the screenshot
    
#     im = ImageGrab.grab()
#     box = (x_pad+1, y_pad+1, x_pad+1047, y_pad+556)  # Define the bounding box (left, upper, right, lower)
#     im = ImageGrab.grab(box)
#     # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
#     im.save(os.path.join(os.getcwd(), 'screenshot.png'), 'PNG')


# def main():
#     # screenGrab()
#     pass


# if __name__ == '__main__':
#     main()
