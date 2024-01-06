## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the overlay that pops up when the bug report is being sent. Also prevents the user from spamming the send button.
screen br_sc_sending_modal():
    
    zorder 199

    modal True

    key "game_menu" action NullAction()

    frame:
        xysize(1.0, 1.0)
        background "br_i_modalOverlay"

        frame:
            xysize(0.4, 0.4)
            padding(10, 10)

            style_prefix "br_st_modal"

            if br_sentSuccessfully:
                use br_usc_button_exit(Function(br_Close))
            elif not br_sentSuccessfully:
                use br_usc_button_exit(Function(br_CloseSendingModal))
            
            vbox:
            
                if br_sentSuccessfully is None:
                
                    text "Sending bug report. Please wait..."               
    
                elif br_sentSuccessfully:
                
                    text "Bug report sent. Thank you!"
    
                    use br_usc_button("Close", align=(0.5, 0.5), actions=Function(br_Close))

                else:
                    text "[br_errorMessage]"
                    
                    use br_usc_button("Back", align=(0.5, 0.5), actions=Function(br_CloseSendingModal))
