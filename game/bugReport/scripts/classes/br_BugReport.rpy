## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init python:
## main class for the plugin
    class br_BugReport():
        CATEGORIES = ["Spelling/Grammar/Text", "Critical/Progress Blocking", "Gameplay/Logic", "Visual/Graphical", "Other"]
        CONTACT_INFO_TYPES = ["Email", "Discord", "Other"]

        def __init__(self):
            
            ## these variables reset when the main screen closes
            self.description = None
            self.categoryIndex = 0
            self.editedScreenshotData = None
            self.screenshotPath = None

            ## these variables are overwritten when the main screen is opened
            self.oldRollbackEnabled = None
            self.oldInputNextLine = None
            self.oldInputEnter = None
            self.oldQuickMenu = None
            
            ## these variables are reset when the sending modal screen is closed
            self.errorMessage = None
            self.errorInfo = None
            self.sentSuccessfully = None

            ## these variables does not reset
            self.contactInfo = None
            self.contactInfoTypeIndex = 0
        

        ## function for showing the bug report button
        def Enable(self):

            ## if we are running in a web-build, do nothing as the tool does not work in web-builds
            if (renpy.emscripten):
                return

            ## show the bug report button
            renpy.show_screen("br_sc_report_bug")


        ## function for hiding the bug report button
        def Disable(self):

            ## if we are running in a web-build, do nothing
            if (renpy.emscripten):
                return

            ## hide the report bug screen
            renpy.hide_screen("br_sc_report_bug")


        ## opens the main bug report screen
        def Open(self):
            global quick_menu

            ## store the original values of various settings
            self.oldRollbackEnabled = config.rollback_enabled
            self.oldInputEnter = config.keymap["input_enter"]
            self.oldInputNextLine = config.keymap["input_next_line"]
            self.oldQuickMenu = quick_menu
            
            ## hide the report bug screen
            self.Disable()
            
            ## disable rollback 
            config.rollback_enabled = False
            ## disable the normal behavior for pressing enter
            config.keymap["input_enter"] = None
            ## set new line key
            config.keymap["input_next_line"] = ["K_RETURN", "K_KP_ENTER"]        
            
            ## Take a screen shot
            self.TakeScreenshot()
            
            ## set hide the quick menu after the screenshot was taken
            quick_menu = False

            ## show the bug report screen
            renpy.show_screen("br_sc_main")


        ## closes the main and modal screen and resets variables
        def Close(self):
            ## start by closing the sending modal in case it is open
            self.CloseSendingModal()

            ## hide all the bugreport screens
            renpy.hide_screen("br_sc_main")

            ## show the bug report button again
            self.Enable()

            ## reset variables
            self.description = None
            self.screenshotPath = None
            self.editedScreenshotData = None

            ## set config settings back to their original values
            config.rollback_enabled = self.oldRollbackEnabled
            config.keymap['input_next_line'] = self.oldInputNextLine
            config.keymap['input_enter'] = self.oldInputEnter

            ## restore the value of quick_menu
            quick_menu = self.oldQuickMenu
        

        ## closes the screen and resets the variables
        def CloseSendingModal(self):
            
            ## hides the sending modal
            renpy.hide_screen("br_sc_sending_modal")

            ## reset modal variables
            self.errorMessage = None
            self.errorInfo = None
            self.sentSuccessfully = None


        ## callback function for when the contact info changes
        def OnContactInfoChanged(self, newValue):
            self.contactInfo = newValue


        ## callback function for when the description changes
        def OnDescriptionChanged(self, newValue):
            self.description = newValue


        ## takes a screenshot for the bug report
        def TakeScreenshot(self):
            ## cache the original screenshot callback and screenshot pattern
            oldCallback = config.screenshot_callback
            oldPattern = config.screenshot_pattern

            ## set the screenshot callback to our callback method
            config.screenshot_callback = self.TakeScreenshotCallback

            ## if we are in developer mode, save the screenshot to the dev folder instead of the default path
            if (config.developer):
                config.screenshot_pattern = os.path.join(br_BUGREPORT_PACKAGE_DIR, br_DEV_FOLDER, "screenshot%04d.png")

            ## take a screenshot
            Screenshot()()

            ## restore the screenshot callback and screenshot pattern back to the original values
            config.screenshot_callback = oldCallback
            config.screenshot_pattern = oldPattern


        ## callback function for when a screenshot was taken
        def TakeScreenshotCallback(self, path):
            self.screenshotPath = path

            ## show a screenshot notification
            renpy.show_screen("br_sc_notify", f"Screenshot taken: {path}")


        ## creates the email object and attempt to send it
        def TrySend(self):
            import platform, bugreport_smtp
            from email.mime.text import MIMEText
            from email.mime.image import MIMEImage
            from email.mime.multipart import MIMEMultipart

            ## show the sending modal
            renpy.show_screen("br_sc_sending_modal")

            ## create local variables for the report
            category = br_BugReport.CATEGORIES[self.categoryIndex]
            gameName = config.name
            gameVersion = config.version
            platformName = platform.platform()
            fileName, line = renpy.get_filename_line()
            description = self.description if bool(self.description) else "NO DESCRIPTION"
            contactInfoType = br_BugReport.CONTACT_INFO_TYPES[self.contactInfoTypeIndex]
            contactInfo = self.contactInfo if bool(self.contactInfo) else None

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

            ## attack edited screenshot if it exists
            if bool(self.editedScreenshotData):

                image = MIMEImage(self.editedScreenshotData, name="screenshot_edited.png")

                mail.attach(image)

            ## attach the screenshot if it exists
            if os.path.exists(self.screenshotPath):

                with open(self.screenshotPath, 'rb') as file:
                    imageData = file.read()

                image = MIMEImage(imageData, name="screenshot.png")

                mail.attach(image)

            ## attempt to send the mail and provide a callback function for when the result of the attempt is ready
            bugreport_smtp.AttemptSend(mail, self.TrySendCallback)


        ## callback function for when a send attempt is done
        def TrySendCallback(self, success, errorMessage, errorInfo):

            if (not success):
                self.errorMessage = errorMessage
                self.errorInfo = errorInfo

            self.sentSuccessfully = success

            renpy.restart_interaction()
