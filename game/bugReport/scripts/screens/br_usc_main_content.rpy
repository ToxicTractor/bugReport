## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_usc_main_content():
    
    default textAreaSelected = False
    default hoveringTextArea = False

    dismiss action [SetLocalVariable("textAreaSelected", False), SetLocalVariable("hoveringTextArea", False)]

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

                    use br_usc_dropdown(br_CATEGORIES, xysize=dropdownSize, outputVariableName="br_category")

            null height 20

            text "Please describe the issue below."
            text "If you will allow the developer to contact you for further information please include some contact information."

            null height 10

            frame:
                style_prefix "br_st"

                xysize (1.0, 0.6)

                if (hoveringTextArea):
                    background br_t_frame(br_SECONDAY_PANEL_COLOR)
                else:
                    background br_t_frame(br_PRIMARY_PANEL_COLOR)

                button:
                    xysize(1.0, 1.0)

                    hovered SetLocalVariable("hoveringTextArea", True)
                    unhovered SetLocalVariable("hoveringTextArea", False)

                    action [SetLocalVariable("textAreaSelected", True), SetLocalVariable("hoveringTextArea", True)]

                    sensitive (not textAreaSelected)

                side "c r":

                    viewport id "desc_input":
                        mousewheel True
                        
                        if (textAreaSelected):

                            input id "input_description":
                                if (br_description is not None):
                                    default br_description
                                xsize 1.0
                                multiline True
                                changed br_OnDescriptionChanged

                        elif (br_description is not None):

                            text "[br_description]":
                                xsize 1.0
                                color br_PRIMARY_TEXT_COLOR
                        
                    vbar value YScrollValue("desc_input") unscrollable "hide" style "br_st_vbar"

            null height 50

            frame:
                background None
                xfill True

                use br_usc_button("Close", align=(0.0, 0.0), actions=Function(br_Close))
                use br_usc_button("Send", align=(1.0, 0.0), actions=Function(br_TrySend))