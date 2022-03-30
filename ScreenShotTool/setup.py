import sys
import cx_Freeze
base= None
if sys.platform == "win32":
    base="win32GUI"

executables=[cx_Freeze.Executable("Home.py", base=base, icon='main_icon.ico')]
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "ScreenshotTK",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Home.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\{}'.format("ScreenShotTK"),
'data': msi_data
    }
cx_Freeze.setup(
    name="ScreenShotTK",
    options={'bdist_msi': bdist_msi_options, "build_exe": {"packages":["tkinter","webbrowser","shutil","docx","win32clipboard","io","glob","os","time","PIL","pyautogui", "threading", "win32gui"],"include_files":["documents-folder.png","folder.png","home-page.png", "Launch-Icon.png", "pictures-folder.png","screenshot.png", "startup.png","start.png","save.png","pause.png", "main_icon.ico","clipboard.png","readme.txt","about.html"]}},
    version="2.1",
    executables=executables
)


