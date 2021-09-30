#import pyautogui
#pyautogui.click(1742, 1087, duration = 1) # x+=140 y+=120

import os

while True:
    if not os.path.exists("/home/citi/Downloads/foo.txt"):
        continue

    line = ""
    with open('/home/citi/Downloads/foo.txt') as f:
        line = f.readline()

    if line == "":
        continue

    print(line)

    os.remove("/home/citi/Downloads/foo.txt")