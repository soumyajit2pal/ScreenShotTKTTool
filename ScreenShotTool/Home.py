import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
from Screenshotwindow import mainfunction
from floating_button import floating_window
import webbrowser
from tkinter import ttk

colour={"black" : "#0080c0"}
font={"font":"Arial"}
root = Tk()
root.iconbitmap(r'main_icon.ico')
root.minsize(750, 600)
root.maxsize(750, 600)
root.config(bg=colour["black"])
root.title("ScreenShotTK")


def quit_window():
    root.destroy()

def open_aboutus():
    html='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "icon" href =  "main_icon.ico" sizes="70x70"  type = "image/x-icon">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <title>About ScreenshotTK</title>
</head>

<style>
    body{
        background: -webkit-linear-gradient(left, rgb(95, 64, 104) , rgb(235, 92, 152));
                background: -o-linear-gradient(right rgb(95, 64, 104) ,rgb(235, 92, 152)); 
                background: -moz-linear-gradient(right, rgb(95, 64, 104) ,rgb(235, 92, 152));
                background: linear-gradient(to right, rgb(95, 64, 104) , rgb(235, 92, 152));
      }
.main-title{
  color: white;
  /* text-align: center; */
  text-transform: capitalize;
  padding: 0.7em 0;
}
.grid_container{
    align-content: center;  
}
.content{
    background-color:rgba(14, 9, 9, 0.3);
    border: 10px 10px 10px 10x;
}
.details{
  background-color:white;
  border: 10px 10px 10px 10x;
  padding: 10px;
  font-weight: 100;
  font-family:Arial, Helvetica, sans-serif;
  font-size: 15px;
}
</style>

<body>
  
    <div class="grid-container">
    <div class="grid-item">
      <div class="container">
        <div class="content">
          <center><span>
              <h2 class="main-title"><p><img src="main_icon.ico" height="50", width="50"/></p>ScreenshotTK<p>v2.1</p></h2></span></center>
              <div class ="details">
              <p>ScreenshotTK is a screenshot capture open source tool, Schedule screen capture sessions when screenshots should be taken</p>
              <p>Tool have multiple features -</p>
              <ul>
                <li>On demand
                  <ul>
                    <li>Tool has a floating button which can take screenshots of active window as and when required</li>
                  </ul>
                </li>
                <li>Scheduled
                  <ul>
                    <li>Screenshots can be taken by giving time interval in the form HH, MIN, SEC, MS</li>
                  </ul>
                </li>
              </ul>
              <ul>
                <li>Tool creates a document with given name with all the screenshots taken</li>
                </ul>
              
                <ul>
                  <li>Tool have clipboard functionality</li>
                </ul>

                <span><p>Any suggestion or issue feel free to reach
                  <a href="mailto:soumyajp@amdocs.com">Soumyajit Pal</a> &
                  <a href="mailto:Kuldeep.Rathod@amdocs.com">Kuldeep Rathod</a>
                </p></span>
            </div>
        </div>
      </div>
    </div>
  </div>
</body>

</html>   
    '''
    with open('about.html', "w+") as f:
        f.write(html)
    webbrowser.open(os.getcwd()+"/"+'about.html')


my_menu=Menu(root)
root.config(menu=my_menu)

options_menu=Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Clipboard", command=lambda: open_window(os.getcwd(), root))
options_menu.add_command(label="Quit", command=quit_window)

About_menu=Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="About", menu=About_menu)
About_menu.add_command(label="About ScreenshotTK", command=open_aboutus)


upload_label=Label(root, text="SELECT OUTPUT DIRECTORY *",fg='White',bd=8, font=(font['font'], 10, "bold"), bg=colour["black"])
upload_label.grid(sticky=W, padx=10, pady=10, row=0, column=0)


dir_value = StringVar()
upload_entry = ttk.Entry(root, text=dir_value,font=(font['font'], 10, "bold"), width=55)
upload_entry.grid(row=1, column=0, sticky=W, padx=10)
def open_dir():
    path = filedialog.askdirectory()
    dir_value.set(path)

## OPEN DIR
image_folder = Image.open("folder.png")
image_folder=image_folder.resize((35, 35), Image.ANTIALIAS)
flder_icon = ImageTk.PhotoImage(image_folder)
Button(root,  image=flder_icon,  command=open_dir, bd=0.1).grid(row=1, column=1)


docx_label=Label(root, text="ENTER DOCUMENT NAME *",fg='White',bd=8, font=(font['font'], 10, "bold"), bg=colour["black"]).grid(row=2,sticky=W)
docx_name=StringVar()
docx_info=Label(root, text="(Total length of document name and output directory path should be less than 260 characters) *",fg='black',bd=8, font=(font['font'],8, "bold"), bg=colour["black"]).grid(row=3,sticky=W, columnspan=4)
ttk.Entry(root, text=docx_name, font=(font['font'], 10, "bold"), width=55).grid(row=4, column=0, sticky=W, padx=10)

## LAUNCH NEXT WINDOW AND INPUT VALIDATION
def check_empty():
    if len(docx_name.get()+dir_value.get())<245:
        if docx_name.get() and dir_value.get():
            root.withdraw()
            create_directory()
        else:
            tmsg.showerror("Waring", "Please enter all the fields", parent=root)
    else :
        tmsg.showerror("Permission Error", "PermissionError: [Errno 13] Permission denied\nTotal length of document "
                                           "name and output directory path should be less than 260 characters",
                       parent=root)

###### META DATA ###################################

def create_metadata():
    with open("metadata.txt", "w+") as f:
        f.write(text.get("1.0", 'end-1c'))

def leftclick(event):
    text.delete("1.0",END)

metadata_label=Label(root, text="ENTER META DATA FOR DOCUMENT (Optional)",fg='White', font=(font['font'], 10, "bold"), bg=colour["black"]).grid(row=5,sticky=W, padx=10, pady=10)
text=Text(root, width=55, height=10, font=(font['font'],10, "bold"))
text.insert("1.0","Enter metadata which you want to add on document,like BAN,testcase details etc.\n\nRight click to "
                  "erase content")
text.grid(row=6, column=0, padx=10)
text.bind("<Button-3>", leftclick)


image = Image.open("Launch-Icon.png")
image=image.resize((30, 30), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
Button(root, text="LAUNCH",image = photo,font=(font['font'], 12, "bold"), command=check_empty, compound="right", bg="#0F0501",fg="white", width=150).grid(row=7, column=0, pady=10, columnspan=6)

def open_window(path, root):
    root.withdraw()
    floating_window(root, path, "home")

version_label=Label(root, text="V2.1",fg='#ffffff', font=(font['font'], 10, "bold"), bg=colour["black"]).grid(row=7,column=2,sticky=W)

def create_directory():
    parent_directory=dir_value.get()
    new_directory=docx_name.get()
    path=parent_directory+"\\{}".format(new_directory)
    try:
        os.mkdir(path)
        working_directory=os.path.abspath(parent_directory)
        image_dir=path+"\\image"
        os.mkdir(image_dir)
        docx_dir = path+"\\document"
        os.mkdir(docx_dir)
        create_metadata()
        mainfunction(root,working_directory, docx_name.get())
    except:
        create_metadata()
        value = tmsg.askquestion("Warning", "Directory allready Exist, continue ?", parent=root)
        if value == "yes":
            working_directory = os.path.abspath(parent_directory)
            mainfunction(root, working_directory, docx_name.get())
        else:
            root.deiconify()

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()