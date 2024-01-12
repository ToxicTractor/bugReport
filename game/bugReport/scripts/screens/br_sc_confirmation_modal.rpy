## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## confirmation modal screen
screen br_sc_confirmation_modal(modalText, actions=NullAction(), confirmText="Confirm", cancelText="Cancel"):
    zorder 205

    ## actions to take when each button is pressed
    $ cancelAction = Hide(CurrentScreenName())
    $ confirmActions = (actions if isinstance(actions, list) else [actions]) + [Hide(CurrentScreenName())]

    ## make sure the "game_menu" key does not open the menu and instead does the cancel action
    key "game_menu" action cancelAction

    ## add a slightly transparent black background
    add "br_i_modalOverlay"

    ## modal box
    frame:
        padding(25, 25)
        style_prefix "br_st_modal"
        
        align(0.5, 0.5)
        xmaximum 0.4

        vbox:
            spacing 50

            ## display the text of the modal window
            text modalText:
                textalign 0.5
            
            hbox:
                xalign(0.5)
                spacing 200

                ## the cancel button
                fixed:
                    xysize(150, 80)
                    use br_usc_button(
                        buttonText="Cancel", 
                        actions=cancelAction
                        )

                ## the confirm button
                fixed:
                    xysize(150, 80)
                    use br_usc_button(
                        buttonText="Confirm", 
                        actions=confirmActions
                        )
                        