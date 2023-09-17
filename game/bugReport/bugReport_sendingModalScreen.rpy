## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the overlay that pops up when the bug report is being sent. Also prevents the user from spamming the send button.
screen bugReport_sendingModalScreen():
    
    zorder 199

    modal True

    frame:
        xysize(1.0, 1.0)
        background "bugReport modalOverlay"

        frame:
            xysize(0.4, 0.4)
            padding(10, 10)

            style_prefix "bugReport_modal"

            if bugReport_sentSuccessfully:
                use bugReport_sendingModalExitButtonScreen([Hide("bugReport_sendingModalScreen"), Hide("bugReport_mainScreen"), SetVariable("config.rollback_enabled", True), Function(ResetVariables, False)])
            elif not bugReport_sentSuccessfully:
                use bugReport_sendingModalExitButtonScreen([Hide("bugReport_sendingModalScreen"), Function(ResetVariables, True)])
            
            vbox:
            
                if bugReport_sentSuccessfully is None:
                
                    text "Sending bug report. Please wait..."               
    
                elif bugReport_sentSuccessfully:
                
                    text "Bug report sent. Thank you!"
    
                    use bugReport_onScreenButton("Close", align=(0.5, 0.5), actions=[Hide("bugReport_sendingModalScreen"), Hide("bugReport_mainScreen"), SetVariable("config.rollback_enabled", True), Function(ResetVariables, False)])
    
                else:
                    text "[bugReport_errorMessage]"
                    
                    use bugReport_onScreenButton("Back", align=(0.5, 0.5), actions=[Hide("bugReport_sendingModalScreen"), Function(ResetVariables, True)])

screen bugReport_sendingModalExitButtonScreen(actions):

    imagebutton auto "images/bugReport/bugReport_exit_%s.webp":
        align(1.0, 0.0)
        action actions