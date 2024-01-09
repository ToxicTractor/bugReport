## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_sc_confirmation_modal(modalText, actions=NullAction(), confirmText="Confirm", cancelText="Cancel"):
    zorder 205

    $ cancelAction = Hide(CurrentScreenName())
    $ confirmActions = (actions if isinstance(actions, list) else [actions]) + [Hide(CurrentScreenName())]

    key "game_menu" action cancelAction

    add "br_i_modalOverlay"

    frame:
        padding(25, 25)
        style_prefix "br_st_modal"
        
        align(0.5, 0.5)
        xmaximum 0.4

        vbox:
            spacing 50

            text modalText:
                textalign 0.5
            
            hbox:
                xalign(0.5)
                spacing 200

                fixed:
                    xysize(150, 80)
                    use br_usc_button(
                        buttonText="Cancel", 
                        actions=cancelAction
                        )

                fixed:
                    xysize(150, 80)
                    use br_usc_button(
                        buttonText="Confirm", 
                        actions=confirmActions
                        )
                        