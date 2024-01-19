## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## text popup screen used for the text fields on mobile devices
screen br_sc_text_popup(variable, onChanged, focus, multiline=False):
    zorder 200
    modal True

    key "game_menu" action NullAction()

    $ rect = GetFocusRect(focus)

    ## frame that fills the screen
    frame:
        xysize(1.0, 1.0)
        padding(0, 0)

        ## adds the modal background to the frame
        background "br_i_modalOverlay"

        ## add our custom dismiss button and makes it hide the screen
        use br_usc_dismiss_button(Hide(CurrentScreenName()))

        ## use the whole screen if not on android or ios otherwise make the top half of the screen available
        ## this is to make room for the on screen keyboard on mobile devices
        fixed:
            if (not renpy.android and not renpy.ios):
                xysize(1.0, 1.0)
            else:
                xysize(1.0, 0.5)

            ## the visual frame of the textbox
            frame:
                style_prefix "br_st"
                background br_t_frame(br_PRIMARY_PANEL_COLOR)
                
                if (not renpy.android and not renpy.ios):
                    pos(int(rect[0]), int(rect[1]))
                else:
                    align(0.5, 0.5)
                
                ## the size of the text box is defined by the dimensions of the rect
                xysize (int(rect[2]), int(rect[3]))

                ## an empty button to capture clicks on the text boxes
                button:
                    action NullAction()

                ## if multiline make the input field inside a viewport
                if (multiline):

                    side "c r":

                        viewport id "viewport_description":
                            mousewheel True

                            input:
                                if (variable):
                                    default variable
                                xsize 1.0
                                multiline True
                                changed onChanged

                        vbar value YScrollValue("viewport_description") unscrollable "hide" style "br_st_vbar"

                ## otherwise just show the input field
                else:

                    input:
                        xysize(1.0, 1.0)

                        if (variable):
                            default variable

                        changed onChanged

                        multiline False
        
