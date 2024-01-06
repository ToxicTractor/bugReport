## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## python functions used in the screens
init python:
    import bugreport_smtp
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    ## function for showing the bug report button. 
    def br_Enable():

        ## if we are running in a web-build, do nothing as the tool does not work in web-builds
        if (renpy.emscripten):
            return

        ## show the bug report button
        renpy.show_screen("br_sc_report_bug")
    

    ## function for hiding the bug report button
    def br_Disable():

        ## if we are running in a web-build, do nothing
        if (renpy.emscripten):
            return

        ## hide the report bug screen
        renpy.hide_screen("br_sc_report_bug")


    ## opens the main bug report screen
    def br_Open():
        global br_originalRollbackSetting
        global br_originalInputEnter
        global br_originalInputNextLine

        ## disable rollback while the bug report screen is open
        br_originalRollbackSetting = config.rollback_enabled
        config.rollback_enabled = False
        
        ## disable the normal behaviour for pressing enter
        br_originalInputEnter = config.keymap["input_enter"]
        config.keymap["input_enter"] = None
        
        ## set new line key and remember the original setting
        br_originalInputNextLine = config.keymap["input_next_line"]
        config.keymap["input_next_line"] = ["K_RETURN", "K_KP_ENTER"]        

        ## Take a screen shot
        br_Screenshot()

        ## show the bug report screen
        renpy.show_screen("br_sc_main")


    ## closes the main and modal screen and resets variables
    def br_Close():
        global br_category
        global br_description
        global br_screenshotPath

        ## hide all the bugreport screens
        renpy.hide_screen("br_sc_main")
        renpy.hide_screen("br_sc_sending_modal")

        ## reset variables
        br_category = None
        br_description = None
        br_screenshotPath = None

        ## set config settings back to their original values
        config.keymap['input_next_line'] = br_originalInputNextLine
        config.keymap['input_enter'] = br_originalInputEnter
        config.rollback_enabled = br_originalRollbackSetting
        

    ## resets the store variables
    def br_CloseSendingModal():
        global br_errorMessage
        global br_sentSuccessfully
        
        ## hides the sending modal
        renpy.hide_screen("br_sc_sending_modal")

        ## reset modal variables
        br_errorMessage = None
        br_sentSuccessfully = None


    ## callback function for when the description of the report changes
    def br_OnDescriptionChanged(input):
        global br_description

        br_description = input


    ## callback function for when the contact info of the report changes
    def br_OnContactInfoChanged(input):
        global br_contactInfo

        br_contactInfo = input


    ## takes a screenshot for the bug report
    def br_Screenshot():

        ## store the original screenshot callback and screenshot pattern
        oldCallback = config.screenshot_callback
        oldPattern = config.screenshot_pattern

        ## set the screenshot callback to our callback method
        config.screenshot_callback = br_ScreenshotCallback

        ## if we are in developer mode, save the screenshot to the dev folder instead of the default path
        if (config.developer):
            config.screenshot_pattern = os.path.join(br_BUGREPORT_PACKAGE_DIR, br_DEV_FOLDER, "screenshot%04d.png")

        ## take a screenshot
        Screenshot()()

        ## restore the screenshot callback and screenshot pattern back to the original values
        config.screenshot_callback = oldCallback
        config.screenshot_pattern = oldPattern


    ## callback function for when a screenshot was taken
    def br_ScreenshotCallback(path):
        global br_screenshotPath

        ## show a screenshot notification
        renpy.show_screen("br_sc_notify", f"Screenshot taken: {path}")

        ## cache the path
        br_screenshotPath = path


    ## creates the email object and attempt to send it
    def br_TrySend():

        #show the sending modal
        renpy.show_screen("br_sc_sending_modal")

        ## create the mail object
        mail = MIMEMultipart()
        mail['Subject'] = f"BugReport: {br_category if br_category is not None else br_CATEGORIES[0]}"
        
        ## construct body of the mail
        body = f"Game: {config.name} - {config.version}\n"

        body += f"{platform.platform}\n"
        
        fileAndLine = renpy.get_filename_line()

        body += f"File: '{fileAndLine[0]}' - Line: {fileAndLine[1]}\n"

        if (br_contactInfo is None or br_contactInfo == ""):
            body += "NO CONTACT INFO\n"
        else:
            body += br_contactInfo

        description = None
        if br_description is None or br_description == "":
            description = "NO DESCRIPTION GIVEN"
        else:
            description = br_description

        body += f"{description}\n\n"

        mail.attach(MIMEText(body))
        
        ## attach the screenshot if it exists
        if os.path.exists(br_screenshotPath):

            with open(br_screenshotPath, 'rb') as file:
                imageData = file.read()

            image = MIMEImage(imageData, name=os.path.basename(br_screenshotPath))

            mail.attach(image)

        ## attempt to send the mail and provide a callback function for when the result of the attempt is ready
        bugreport_smtp.AttemptSend(mail, br_TrySendCallback)
    

    ## callback function for when an attempt to send a mail is done
    def br_TrySendCallback(success, errorMessage):
        global br_errorMessage
        global br_sentSuccessfully
        
        if not success:
            br_errorMessage = errorMessage

        br_sentSuccessfully = success

        renpy.restart_interaction()
