## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init -1 python:
    ## define the name of the dev folder
    br_DEV_FOLDER = "_dev"

    ## exclude the '.py' files from builds of the game
    build.classify("**bugreport_smtp.py", None)
    build.classify("**smtplib.py", None)

    ## exclude contents of the '_dev' folder. This is where screenshots are saved when 'config.developer == True'
    build.classify(f"**/bugReport/{br_DEV_FOLDER}/**", None)