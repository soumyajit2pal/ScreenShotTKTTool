from tkinter import  *
from byactivewindow import takeScreenshot
import time

def floating_window(window, path, from_="Normal"):
    floating_window=Toplevel(bg="grey", highlightbackground = "red", highlightcolor= "red")
    floating_window.geometry("100x73")
    floating_window.minsize(100, 73)
    floating_window.maxsize(100, 73)

    f1 = Frame(floating_window, relief=SUNKEN, bg="grey")
    f1.pack()

    def disable_event():
        window.deiconify()
        floating_window.destroy()
    def forget():
        message_label.config(text="")

    def message_show():
        floating_window.withdraw()
        takeScreenshot(path, from_)
        message_label.config(text="SAVED")
        floating_window.update()
        floating_window.deiconify()
        message_label.after(2000, forget)

    screen_shot = Button(f1, text='TAKE', font="Balthazar 10 bold",  bg="black", fg="#F8E72C",
                   command=message_show)
    screen_shot.pack(pady=5)
    floating_window.protocol("WM_DELETE_WINDOW", disable_event)
    floating_window.attributes("-toolwindow", True)
    floating_window.attributes("-topmost", True)
    message_label = Label(f1, text="", font="Balthazar 7", justify=LEFT, fg="red", bg="grey")
    message_label.pack(pady=5)
    floating_window.mainloop()





