## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

default bugReport_category = None
default bugReport_description = None
default bugReport_originalRollbackSetting = None
default bugReport_sentSuccessfully = None
default bugReport_errorMessage = None
default bugReport_screenshotPath = None

## these are the categories displayed in the dropdown menu
define bugReport_categories = ["Spelling/Grammar/Text", "Critical/Progress Blocking", "Gameplay/Logic", "Visual/Graphical", "Other"]

init python:
    import os, platform, bugreport_smtp
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    ## exclude the '.py' files from builds of the game
    build.classify("**bugreport_smtp.py", None)
    build.classify("**smtplib.py", None)

    ## resets the store variables
    def ResetVariables(partialReset):
        
        store.bugReport_errorMessage = None
        store.bugReport_sentSuccessfully = None
        
        ## return if this was only a partial reset
        if partialReset:
            return
        
        store.bugReport_originalRollbackSetting = None
        store.bugReport_category = None
        store.bugReport_description = None
        store.bugReport_screenshotPath = None
    
    ## creates the email object and attempt to send it
    def ConstructAndSendEmail():

        ## create the mail object
        mail = MIMEMultipart()
        mail['Subject'] = f"BugReport: {store.bugReport_category if store.bugReport_category is not None else bugReport_categories[0]}"
        
        ## construct body of the mail
        body = f"Game: {config.name} - {config.version}\n"

        body += f"{platform.platform}\n"
        
        fileAndLine = renpy.get_filename_line()

        body += f"File: '{fileAndLine[0]}' - Line: {fileAndLine[1]}"

        description = None
        if store.bugReport_description is None or store.bugReport_description == "":
            description = "NO DESCRIPTION GIVEN"
        else:
            description = store.bugReport_description

        body += f"{description}\n\n"

        mail.attach(MIMEText(body))
        
        ## attach the screenshot if it exists
        if os.path.exists(bugReport_screenshotPath):

            with open(bugReport_screenshotPath, 'rb') as file:
                imageData = file.read()

            image = MIMEImage(imageData, name=os.path.basename(bugReport_screenshotPath))

            mail.attach(image)

        ## attempt to send the mail and provide a callback function for when the result of the attempt is ready
        bugreport_smtp.AttemptSend(mail, OnAttemptCompleted)
    
    ## callback function for when an attempt to send a mail is done
    def OnAttemptCompleted(success, errorMessage):
        if not success:
            store.bugReport_errorMessage = errorMessage

        store.bugReport_sentSuccessfully = success

        renpy.restart_interaction()