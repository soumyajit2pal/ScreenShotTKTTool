import pyautogui
from datetime import datetime
from Clipboardaction import image_convert
import os
import shutil

def takeScreenshot (working_dir, From_="Normal"):
    myScreenshot = pyautogui.screenshot()
    time_=datetime.now().strftime("%H_%M_%S")
    if From_ == "Normal":
        myScreenshot.save('{}\image\screenshot{}.jpeg'.format(working_dir,time_),optimize=True)
        image_convert('{}\image\screenshot{}.jpeg'.format(working_dir,time_))
    elif From_ == "home":
        if os.path.exists("Temp"):
            myScreenshot.save('{}\Temp\screenshot{}.jpeg'.format(working_dir, time_), optimize=True)
            image_convert('{}\Temp\screenshot{}.jpeg'.format(working_dir, time_))
        else:
            os.mkdir(working_dir+"\Temp")
            myScreenshot.save('{}\Temp\screenshot{}.jpeg'.format(working_dir, time_), optimize=True)
            image_convert('{}\Temp\screenshot{}.jpeg'.format(working_dir, time_))
        try:
            shutil.rmtree(working_dir+"\Temp")
        except:
            pass
    return  "screenshot{}.jpeg saved".format(datetime.now().strftime('%H_%M_%S'))


