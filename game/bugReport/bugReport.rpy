default bugReport_description = None
default bugReport_category = None
default bugReport_originalRollbackSetting = None
default bugReport_sentSuccessfully = None
default bugReport_errorMessage = None

define bugReport_categories = ["Spelling/Grammar/Text", "Critical/Progress Blocking", "Gameplay/Logic", "Visual/Graphical", "Other"]
define bugReport_screenshotPath = config.gamedir + "\\bugReport\\screenshot1.png"

## this creates the button that you click on to open the bug report overlay
screen bugReport_button:

    textbutton "REPORT BUG":
        align(1.0, 1.0)
        action [SetVariable("bugReport_originalRollbackSetting", config.rollback_enabled), Function(TakeBugReportScreenshot), Function(ToggleRollback, False), Show("bugReport_screen")]

## creates a dropdown menu
screen bugReport_dropdown_menu(width, maxHeight, valueIndex, values, result):

    zorder 2
    default isOpen = False
    default currentValueIndex = valueIndex

    vbox:

        button:
            padding(0, 0)
            frame:
                xysize (width, 50)
                xfill True yfill True
                text values[currentValueIndex]

            action SetLocalVariable("isOpen", True)
        
        if isOpen:
            dismiss action SetLocalVariable("isOpen", False)
    
            $ height = min(50 * len(values) + 5, maxHeight)
            frame:
                xsize width

                side "c r":
                    xfill True

                    viewport id "options":
                        ysize height
                        mousewheel True

                        has vbox

                        for i in range(len(values)):
                        
                            textbutton values[i]:
                                action [SetVariable(result, values[i]), SetLocalVariable("currentValueIndex", i), SetLocalVariable("isOpen", False)]
                    
                    vbar value YScrollValue("options") unscrollable "hide":
                        ysize height

## creates the overlay that pops up when the bug report is being sent. Also prevents the user from spamming the send button.
screen bugReport_sending_screen:
    zorder 5
    modal True
    frame:
        xysize(1.0, 1.0)
        background Solid("#000000cc")

        frame:
            xysize(0.4, 0.4)
            align(0.5, 0.5)

            has vbox
            align(0.5, 0.5)
            spacing 100

            if bugReport_sentSuccessfully is None:
                text "Sending bug report. Please wait..."

            elif bugReport_sentSuccessfully:

                text "Bug report sent. Thank you!":
                    yalign 0.5

                button:
                    xalign 0.5
                    frame:
                        padding(10,10)
                        text "Close"
                    action [Hide("bugReport_sending_screen"), Hide("bugReport_screen"), Function(ToggleRollback, True), Function(ResetVariables, False)]
            else:
                text "[bugReport_errorMessage]":
                    text_align 0.5

                button:
                    xalign 0.5
                    frame:
                        padding(10,10)
                        text "Back"
                    action [Hide("bugReport_sending_screen"), Function(ResetVariables, True)]

## creates the main bug report screen.
screen bugReport_screen:

    modal True
    zorder 3

    frame:
        xysize(1.0, 1.0)
        xpadding 50

        background Solid("#000000cc")

        text "Report an issue":
            xalign 0.5
            size 64

        text "Please describe the issue:":
            ypos 0.35
        
        frame:
            ypos 0.4
            xysize (1.0, 0.3)
            side "c r":

                viewport id "desc_input":
                    mousewheel True
                    input:
                        xsize 1.0
                        multiline True
                        changed OnDescriptionChanged

                vbar value YScrollValue("desc_input") unscrollable "hide"

        hbox:
            align(0.5, 0.8)
            spacing 100

            button:
                frame:
                    padding (10, 10)
                    text "Close"

                action [Hide("bugReport_screen"), Function(ToggleRollback, True), Function(ResetVariables, False)]
                
            button:
                frame:
                    padding (10, 10)
                    text "Send"
                    
                action [Show("bugReport_sending_screen"), Function(ConstructAndSendEmail)]
        
        ## draw the drop down last to make it draw on top
        text "To report an issue you must select a category below and describe the issuse.\nWhen sending your report, a screenshot, some diagnostics data and whatever you enter here will be sent. This requires a connection to the internet.":
            ypos 0.1

        hbox:
            ypos 0.25
            text "Please select a category: "
            use bugReport_dropdown_menu(500, 300, 0, bugReport_categories, "bugReport_category")

init python:
    import os, sys
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    ## Compiles the 'bugReportSMTP.py' script so we can use the compiled script in our game. You can comment out these 2 lines when
    ## you have a compiled file. These lines should always be commented out in a released game as the 'bugReportSMTP.py' file should
    ## only exist during development.
    import py_compile
    py_compile.compile(os.path.join(config.gamedir, "bugReport", "bugReportSMTP.py"))
    
    ## add the path of this plugin to the sys path to allow us to import the compiled bugReportSMTP script
    sys.path.append(os.path.join(config.gamedir, "bugReport"))

    from bugReportSMTP import AttemptSend

    def ToggleRollback(value):

        ## toggle the rollback feature on or off
        config.rollback_enabled = value

    def OnDescriptionChanged(input):

        ## update the value of the store variable
        store.bugReport_description = input

    def ResetVariables(partialReset):
        
        store.bugReport_errorMessage = None
        store.bugReport_sentSuccessfully = None
        
        ## return if this was only a partial reset
        if partialReset:
            return
        
        store.bugReport_originalRollbackSetting = None
        store.bugReport_category = None
        store.bugReport_description = None

        if os.path.exists(bugReport_screenshotPath):
            os.remove(bugReport_screenshotPath)
    
    def TakeBugReportScreenshot():

        ## saves the original screenshot pattern so we can reset the patter when we are done with it
        oldPattern = config.screenshot_pattern

        config.screenshot_pattern = os.path.join(config.gamedir, "bugreport", "screenshot%s.png")
        
        screenshotPath = config.screenshot_pattern % 1

        ## removes any old bug related screenshots before taking a new one
        if os.path.exists(screenshotPath):
            os.remove(screenshotPath)

        ## takes a screenshot
        Screenshot()()

        ## reset to the old pattern
        config.screenshot_pattern = oldPattern
    
    def ConstructAndSendEmail():

        ## create the mail object
        mail = MIMEMultipart()
        mail['Subject'] = f"BugReport: {store.bugReport_category if store.bugReport_category is not None else bugReport_categories[0]}"
        
        ## construct body of the mail
        body = f"Game: {config.name} - {config.version}\n"

        if renpy.windows:
            body += "Platform: Windows\n\n"
        elif renpy.macintosh:
            body += "Platform: macOS\n\n"
        elif renpy.android:
            body += "Platform: Android\n\n"
        
        description = None
        if store.bugReport_description is None or store.bugReport_description == "":
            description = "NO DESCRIPTION GIVEN"
        else:
            description = store.bugReport_description

        body += f"{description}\n\n"

        fileAndLine = renpy.get_filename_line()

        body += f"File: {fileAndLine[0]} | Line: {fileAndLine[1]}"

        mail.attach(MIMEText(body))
        
        ## attach the screenshot if it exists
        if os.path.exists(bugReport_screenshotPath):

            with open(bugReport_screenshotPath, 'rb') as file:
                imageData = file.read()

            image = MIMEImage(imageData, name=os.path.basename(bugReport_screenshotPath))

            mail.attach(image)

        ## attempt to send the mail and provide a callback function for when the result of the attempt is ready
        AttemptSend(mail, OnAttemptCompleted)
    
    ## callback function for when an attempt to send a mail is done
    def OnAttemptCompleted(success, errorMessage):
        if success:
            store.bugReport_errorMessage = errorMessage

        store.bugReport_sentSuccessfully = success

        renpy.restart_interaction()