## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the overlay that pops up when the bug report is being sent. Also prevents the user from spamming the send button.
screen br_sc_sending_modal():
    zorder 199
    modal True

    ## make sure the "game_menu" key doesn't work on this screen
    key "game_menu" action NullAction()

    ## fills the screen with a frame and add the modal background to it
    frame:
        xysize(1.0, 1.0)
        background "br_i_modalOverlay"

        ## the main box of the sending modal
        frame:
            style_prefix "br_st_modal"
            xysize(0.4, 0.4)
            padding(10, 10)

            ## if the bug report was send successfully, the close button closes the entire overlay, including the main screen
            if br_main.sentSuccessfully:
                use br_usc_button_exit(Function(br_main.Close))
            ## otherwise it just closes the sending modal
            else:
                use br_usc_button_exit(Function(br_main.CloseSendingModal))

            ## vbox containing the various bits of information on the sending modal
            vbox:

                ## if sentSuccessfully is None the bugreport is in the progress of being sent
                if br_main.sentSuccessfully is None:
                
                    text "Sending bug report. Please wait..."               

                ## if the report was send successfully
                elif br_main.sentSuccessfully:
                
                    text "Bug report sent. Thank you!"

                    fixed:
                        xalign 0.5
                        xysize(150, 80)
                        use br_usc_button("Close", actions=Function(br_main.Close))

                ## if the report was not sent
                else:
                    fixed:
                        xysize(1.0, 0.3)

                        ## display an error message
                        text "[br_main.errorMessage]":
                            yalign 0.0

                        ## display some error details
                        text "[br_main.errorInfo]":
                            yalign 1.0
                            size 20
                            color "#800"

                    ## close button
                    fixed:
                        xalign 0.5
                        xysize(150, 80)
                        use br_usc_button("Back", actions=Function(br_main.CloseSendingModal))
