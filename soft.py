# """ Utility to get mouse position and RGB color of pixel under mouse. """

# import pyautogui
# import time

# def main():
#     try:
#         while True:
#             x, y = pyautogui.position()
#             try:
#                 pixelColor = pyautogui.screenshot().getpixel((x, y))
#                 positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#                 positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
#                 positionStr += ', ' + str(pixelColor[1]).rjust(3)
#                 positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
#             except OSError:
#                 positionStr = f'X: {x} Y: {y} RGB: (---, ---, ---)'

#             print(positionStr, end='\r', flush=True)
#             time.sleep(0.5)
            

#     except KeyboardInterrupt:
#         print('\nDone.')

# if __name__ == '__main__':
#     main()




# """Utility to get a specific rectangle on screen. """

# import pyautogui

# def main():
#     print("Move your mouse to TOP-LEFT corner and press Enter in console...")
#     input()
#     x1, y1 = pyautogui.position()
#     print(f"Top-left: ({x1}, {y1})")

#     print("Move your mouse to BOTTOM-RIGHT corner and press Enter...")
#     input()
#     x2, y2 = pyautogui.position()
#     print(f"Bottom-right: ({x2}, {y2})")
#     print(f"Rectangle: ({x1}, {y1}, {x2}, {y2})")

# if __name__ == "__main__":
#     main()






""" Quick test to grab and analyze one seat bubble for sushi type. """

from PIL import ImageGrab, ImageOps
import time
def main():
    
# 👇 Replace with your actual coordinates for ONE seat bubble
    box = (725, 231, 797, 252)
    img = ImageGrab.grab(box)
    gray = ImageOps.grayscale(img)

    img_sum = sum(gray.getdata())
    print(f"Pixel sum for this sushi: {img_sum}")

if __name__ == "__main__":
    time.sleep(2)
    main()

