## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init -2 python:
    ## get the directory of the python folder for the current Ren'Py installation. This is not in your project folder but in the 
    ## installation directory for Ren'Py itself. The path might be different on other machines but it should look something like:
    ## "renpy install path"/lib/"python version"
    ## it compiles to this folder as this was the only way I could get RenPy to import the compiled '.pyc' files on android devices.
    br_RENPY_PYTHON_DIR = os.path.join(sys.base_prefix, sys.platlibdir, f"python{sys.version_info.major}.{sys.version_info.minor}")
    
    ## path to the 'bugReport' folder
    br_BUGREPORT_PACKAGE_DIR = os.path.join(config.gamedir, "bugReport")
    
    ## path to the py files
    br_SMTPLIB_PY = os.path.join(br_BUGREPORT_PACKAGE_DIR, "scripts", "python", "smtplib.py")
    br_BUGREPORTSMTP_PY = os.path.join(br_BUGREPORT_PACKAGE_DIR, "scripts", "python", "bugreport_smtp.py")

    ## define the name of the dev folder
    br_DEV_FOLDER = "_dev"

    ## ----------------------------------------------------------------
    ## exclude the '.py' files from builds of the game
    build.classify("**bugreport_smtp.py", None)
    build.classify("**smtplib.py", None)

    ## exclude contents of the '_dev' folder. This is where screenshots are saved when 'config.developer == True'
    build.classify(f"**/bugReport/{br_DEV_FOLDER}/**", None)
    ## ----------------------------------------------------------------


##---------------------------------------------------------------------
## main
##---------------------------------------------------------------------
default br_main = br_BugReport()


##---------------------------------------------------------------------
## settings
##---------------------------------------------------------------------
define br_allow_empty_description = True ## set this to 'False' if you want to force the player to put in a description


##---------------------------------------------------------------------
## ui colors
##---------------------------------------------------------------------
define br_PRIMARY_PANEL_COLOR = "#aaa"
define br_SECONDARY_PANEL_COLOR = "#ccc"

define br_BUTTON_IDLE_COLOR = "#888"
define br_BUTTON_HOVER_COLOR = "#ccc"
define br_BUTTON_INSENSITIVE_COLOR = "#555"

define br_PRIMARY_TEXT_COLOR = "#000"
define br_SECONDARY_TEXT_COLOR = "#444"
define br_PRIMARY_TEXT_HOVER_COLOR = "#222"

define br_PRIMARY_BAR_IDLE_COLOR = "#888"
define br_SECONDARY_BAR_IDLE_COLOR = "#444"
define br_PRIMARY_BAR_HOVER_COLOR = "#ccc"
define br_SECONDARY_BAR_HOVER_COLOR = "#555"
