
import pyautogui
try:
    while True:
        x, y = pyautogui.position()
        try:
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        except OSError:
            positionStr = f'X: {x} Y: {y} RGB: (---, ---, ---)'

        print(positionStr, end='\r', flush=True)

except KeyboardInterrupt:
    print('\nDone.')