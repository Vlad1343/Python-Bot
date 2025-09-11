# Sushi Go Round Automation Bot

This repository is dedicated to automating the browser game **Sushi Go Round** using Python.
It serves as a hands-on project to explore GUI automation, image processing, and game logic simulation.

---

## Project Focus

### Advanced Python Features

- GUI automation using `pyautogui` to control mouse clicks and positions  
- Screenshot capture and image analysis using `Pillow` (PIL)  
- Grayscale image processing to detect sushi orders  
- Modular design with helper scripts (`cords.py` and `quickGrab.py`)  
- Recursion for repeated ingredient purchase attempts  
- Time delays and program flow control with `time.sleep()`  

### Game Logic & Automation

- Detect customer orders across six seat areas  
- Map pixel-based image sums to specific sushi types  
- Automatic sushi preparation based on inventory and recipes  
- Dynamic inventory management for key ingredients (`rice`, `nori`, `roe`)  
- Table clearing automation to maintain workflow efficiency  

---

## Key Features

- Automates gameplay for a complete sushi restaurant simulation  
- Detects and prepares sushi in real time based on customer orders  
- Keeps track of inventory and restocks ingredients as needed  
- Flexible configuration for different screen resolutions using relative coordinates  
- Includes a failsafe mechanism to stop the program by moving the cursor to the top-left corner  

---

## Quick Start

All coordinates assume a screen resolution of 3456x2234, and Safari
maximized with the Bookmarks Toolbar enabled.  
You can find your own coordinates using the code in `soft.py`.  
Or you can readjust the code and use image recognition to find buttons.

**Game URL:** [Sushi Go Round](https://www.crazygames.com/game/sushi-go-round)
