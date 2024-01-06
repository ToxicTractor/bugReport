## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the main bug report screen.
screen bugReport_mainScreen():

    zorder 197

    modal True

    key "game_menu" action NullAction()

    frame:
        xysize(1.0, 1.0)
        xpadding 50

        style_prefix "bugReport"

        background "i_bugReport_modalOverlay"

        if renpy.android or renpy.ios:
            side "c r":
                area(0, 0, config.screen_width, int(config.screen_height / 2))

                viewport id "andorid_view":
                    child_size(config.screen_width - 150, config.screen_height)
                    draggable True

                    use bugReport_mainScreenContent

                vbar value YScrollValue("andorid_view") style "bugReport_vbar"

        else:
            use bugReport_mainScreenContent
        
    ## exit button in the top right corner
    frame:
        background None
        align(1.0, 0.0)
        padding(10, 10)

        imagebutton:

            idle t_bugReport_exit_button(0.5)
            hover t_bugReport_exit_button(1.0)

            action [Hide("bugReport_mainScreen"), SetVariable("config.rollback_enabled", bugReport_originalRollbackSetting), Function(ResetVariables, False)]

screen bugReport_mainScreenContent():
    
    fixed:
        xysize(1.0, 1.0)

        vbox:
            xfill True
            order_reverse True

            text "Report a bug":
                xalign 0.5
                size 64

            null height 50

            text "Here you can report an issue directly to the developer. You must have an active internet connection to send the bug report."
            text "A bug report contains a screenshot, some system information and whatever you enter on this page."
            
            null height 40

            hbox:
                text "Please select a category: "

                $ dropdownSize = (500, 40)
                fixed:
                    xysize dropdownSize

                    use bugReport_dropdownScreen(bugReport_categories, xysize=dropdownSize, outputVariableName="bugReport_category")

            null height 20

            text "Please describe the issue below."
            text "If you will allow the developer to contact you for further information please include some contact information."

            null height 10

            frame:
                style_prefix "bugReport"

                xysize (1.0, 0.6)
                background t_bugReport_frame(BUGREPORT_PRIMARY_PANEL_COLOR)

                side "c r":

                    viewport id "desc_input":
                        mousewheel True
                        
                        input id "input_description":
                            xsize 1.0
                            multiline True
                            changed OnDescriptionChanged

                    vbar value YScrollValue("desc_input") unscrollable "hide" style "bugReport_vbar"

            null height 50

            frame:
                background None
                xfill True

                use bugReport_onScreenButton("Close", align=(0.0, 0.0), actions=[Hide("bugReport_mainScreen"), SetVariable("config.rollback_enabled", bugReport_originalRollbackSetting), Function(ResetVariables, False)])
                use bugReport_onScreenButton("Send", align=(1.0, 0.0), actions=[Show("bugReport_sendingModalScreen"), Function(ConstructAndSendEmail)])
        
init python:

    def OnDescriptionChanged(input):

        store.bugReport_description = input
