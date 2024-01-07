## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## python functions used in the screens
init python:
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
        global br_original_rollback_setting
        global br_original_input_enter
        global br_original_input_next_line

        ## disable rollback while the bug report screen is open
        br_original_rollback_setting = config.rollback_enabled
        config.rollback_enabled = False
        
        ## disable the normal behaviour for pressing enter
        br_original_input_enter = config.keymap["input_enter"]
        config.keymap["input_enter"] = None
        
        ## set new line key and remember the original setting
        br_original_input_next_line = config.keymap["input_next_line"]
        config.keymap["input_next_line"] = ["K_RETURN", "K_KP_ENTER"]        

        ## Take a screen shot
        br_Screenshot()

        ## show the bug report screen
        renpy.show_screen("br_sc_main")


    ## closes the main and modal screen and resets variables
    def br_Close():
        global br_description
        global br_screenshot_path

        ## start by closing the sending modal in case it is open
        br_CloseSendingModal()

        ## hide all the bugreport screens
        renpy.hide_screen("br_sc_main")

        ## reset variables
        br_description = None
        br_screenshot_path = None

        ## set config settings back to their original values
        config.keymap['input_next_line'] = br_original_input_next_line
        config.keymap['input_enter'] = br_original_input_enter
        config.rollback_enabled = br_original_rollback_setting
        

    ## resets the store variables
    def br_CloseSendingModal():
        global br_error_message
        global br_sent_successfully
        
        ## hides the sending modal
        renpy.hide_screen("br_sc_sending_modal")

        ## reset modal variables
        br_error_message = None
        br_sent_successfully = None


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
        global br_screenshot_path

        ## show a screenshot notification
        renpy.show_screen("br_sc_notify", f"Screenshot taken: {path}")

        ## cache the path
        br_screenshot_path = path


    ## creates the email object and attempt to send it
    def br_TrySend():
        import bugreport_smtp

        ## show the sending modal
        renpy.show_screen("br_sc_sending_modal")

        ## create local variables for the report
        category = br_CATEGORIES[br_category_index]
        gameName = config.name
        gameVersion = config.version
        platformName = platform.platform()
        fileName, line = renpy.get_filename_line()
        description = "NO DESCRIPTION" if br_description is None or br_description == "" else br_description
        contactInfoType = br_CONTACT_INFO_TYPES[br_contact_info_index]
        contactInfo = None if br_contactInfo is None or br_contactInfo == "" else br_contactInfo

        ## create the mail object
        mail = MIMEMultipart()
        mail['Subject'] = f"Bug report: {category}"
        
        ## construct body of the mail
        body = f"""
            <html>
                <head></head>
                <body>
                    <b>General info</b><br>
                    Game: {gameName}<br>
                    Version: {gameVersion}<br>
                    Platform: {platformName}<br><br>

                    <b>Other info</b><br>
                    Category: {category}<br>
                    File: {fileName}<br>
                    Line: {line}<br><br>
    
                    <b>Description</b><br>
                    {description}"""

        if (contactInfo is not None):
            body += f"""
                    <br><br>
                    <b>Contact info</b><br>
                    Type: {contactInfoType}<br>
                    Info: {contactInfo}<br>"""

        body += """
                </body>
            </html>
        """

        mail.attach(MIMEText(body, 'html'))
        
        ## attach the screenshot if it exists
        if os.path.exists(br_screenshot_path):

            with open(br_screenshot_path, 'rb') as file:
                imageData = file.read()

            image = MIMEImage(imageData, name=os.path.basename(br_screenshot_path))

            mail.attach(image)

        ## attempt to send the mail and provide a callback function for when the result of the attempt is ready
        bugreport_smtp.AttemptSend(mail, br_TrySendCallback)


    ## callback function for when an attempt to send a mail is done
    def br_TrySendCallback(success, errorMessage):
        global br_error_message
        global br_sent_successfully
        
        if not success:
            br_error_message = errorMessage

        br_sent_successfully = success

        renpy.restart_interaction()
