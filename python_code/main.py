import d3dshot #Screen shot module for windows
import cv2 # image recognition
import numpy as np
import pyautogui # mouse click

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def click_dice():
    print("Click called")
    pyautogui.click() #click(x,y)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    template = cv2.imread('dice_six.png', 0)
    template_w, template_h = template.shape[::-1]

    screen_image_left_px = 0
    screen_image_top_px = 0
    screen_image_right_px = 200
    screen_image_bottom_px = 200

    d = d3dshot.create(capture_output="numpy")
    #d.displays
    #d.display = d.displays[1] #sets display you want to capture from

    #Begin image capture
    d.capture(region=(screen_image_left_px, screen_image_top_px, screen_image_right_px, screen_image_bottom_px))


    dice_not_six = True

    while dice_not_six:
        print("Not Six")

        latest_screen_image = d.get_latest_frame()

        res = cv2.matchTemplate(latest_screen_image, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        if res >= threshold:

            dice_not_six = False


    d.stop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
