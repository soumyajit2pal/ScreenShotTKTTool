import pyautogui
import win32gui
from datetime import datetime
import time
from image_processing import image_resize
def screenshot(window_title=None):
    global message
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # pyautogui.getWindowsWithTitle(window_title)[0].minimize()
            pyautogui.getWindowsWithTitle(window_title)[0].maximize()
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(1)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            message="Not able take screenshot\nwindow not active"
    else:
        im = pyautogui.screenshot()
        return im

    # if window_title:
    #     print(window_title)
    #     active_window=win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #     print(active_window)
    #     if active_window == window_title:
    #         im=pyautogui.screenshot()
    #         return  im
    #     else:
    #         pyautogui.getWindowsWithTitle(window_title)[0].minimize()
    #         pyautogui.getWindowsWithTitle(window_title)[0].maximize()
    #         time.sleep(0.5)
    #         im = pyautogui.screenshot()
    #         return im
    # else:
    #     im = pyautogui.screenshot()
    #     return im



def trigger(title, working_dir):
    global message
    try:
        im = screenshot(title)
        if im:
            take_time=datetime.now().strftime('%H_%M_%S')
            message="screenshot{}.jpeg saved".format(take_time)
            im.save('{}\image\screenshot{}.jpeg'.format(working_dir,take_time))
            # image_resize(working_dir, "screenshot{}.jpeg".format(take_time))

    except Exception as e:
        print(e)
        message="Not able take screenshot\nwindow not active"
    return message
