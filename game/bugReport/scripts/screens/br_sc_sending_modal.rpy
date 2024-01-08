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

            if br_sent_successfully:
                use br_usc_button_exit(Function(br_Close))
            elif not br_sent_successfully:
                use br_usc_button_exit(Function(br_CloseSendingModal))

            vbox:
            
                if br_sent_successfully is None:
                
                    text "Sending bug report. Please wait..."               
    
                elif br_sent_successfully:
                
                    text "Bug report sent. Thank you!"

                    fixed:
                        xalign 0.5
                        xysize(150, 80)
                        use br_usc_button("Close", actions=Function(br_Close))

                else:
                    fixed:
                        xysize(1.0, 0.3)

                        text "[br_error_message]":
                            yalign 0.0
                    
                        text "[br_error_info]":
                            yalign 1.0
                            size 20
                            color "#800"

                    fixed:
                        xalign 0.5
                        xysize(150, 80)
                        use br_usc_button("Back", actions=Function(br_CloseSendingModal))
