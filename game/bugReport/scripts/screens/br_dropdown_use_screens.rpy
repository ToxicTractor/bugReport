## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## reuseable dropdown screen
screen br_usc_dropdown(id, values, outputVariable, arrowSize=24, pixelHeight=40):
    style_prefix "br_st_dropdown"
    zorder 198

    ## variable used to keep track of whether the dropdown is hovered or not
    default isIdle = True

    button:
        padding(0, 0)
        xysize (1.0, 1.0)
        
        hovered SetLocalVariable("isIdle", False)
        unhovered SetLocalVariable("isIdle", True)

        ## capture focus to allow us to place the dropdown at the correct position
        action [CaptureFocus(id), Show("br_sc_dropdown_options", None, id, values, outputVariable, pixelHeight)]
        
        ## visuals for the button
        frame:
            xsize 1.0
            padding(10, 0)

            ## if the output variable contains a '.' it means it is a class variable. we then have to access it differently that if it were just a global variable
            if ('.' in outputVariable):
                $ className, attributeName = outputVariable.split('.', 1)
                text values[getattr(globals()[className], attributeName)]:
                    yalign 0.5
            ## the output variable had no '.' so we treat it as a global variable
            else:
                text values[globals()[outputVariable]]:
                    yalign 0.5

            ## draw the arrow at the right side of the dropdown menu
            fixed:
                xysize(arrowSize, arrowSize)
                align(1.0, 0.5)

                ## change the image based on whether the dropdown was hovered or not
                if isIdle:
                    add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_IDLE_COLOR):
                        xysize(1.0, 1.0)
                else:
                    add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_HOVER_COLOR):
                        xysize(1.0, 1.0)


## dropdown options screen, opened when a dropdown is clicked
screen br_sc_dropdown_options(id, values, outputVariable, pixelHeight, maxPixelHeight=500):
    style_prefix "br_st_dropdown"
    zorder 200
    modal True

    ## if the player presses the game_menu key (right click/escape) close the dropdown instead of opening the menu
    key "game_menu" action Hide(CurrentScreenName())

    ## use a custom dismiss button to close the dropdown if the player clicks outside of the dropdown
    use br_usc_dismiss_button(Hide(CurrentScreenName()))

    ## capture the focus to allow us the place the dropdown correctly
    $ rect = GetFocusRect(id)

    if (rect):
        
        ## calculate a few values we will need later
        $ valueCount = len(values)
        $ boxHeight = int(min(pixelHeight * valueCount, maxPixelHeight))

        ## use the nearrect to place the dropdown at the correct position
        nearrect:
            focus id

            ## outer frame of the dropdown menu
            frame:
                xysize(int(rect[2]), boxHeight)

                ## create a side for the viewport and scrollbar
                side "c r":

                    ## viewport for our dropdown options
                    viewport id "[id]_viewport":
                        mousewheel True
                        
                        has vbox

                        ## loop through all values and create a button for each
                        for i in range(valueCount):

                            button:
                                style_prefix "br_st_dropdown_option"
                                ysize pixelHeight
                                
                                ## set the output variable equal to i and close the dropdown
                                action [SetVariable(outputVariable, i), Hide(CurrentScreenName())]

                                ## button visuals serve to highlight the hovered option
                                frame:
                                    xysize(1.0, 1.0)
                                    
                                    ## if the output variable contains a '.' it means it is a class variable. 
                                    ## we then have to access it differently that if it were just a global variable
                                    if ('.' in outputVariable):
                                        $ className, attributeName = outputVariable.split('.', 1)
                                        text values[i]:
                                            if (getattr(globals()[className], attributeName) == i):
                                                color br_PRIMARY_TEXT_COLOR
                                    ## the output variable had no '.' so we treat it as a global variable
                                    else:
                                        text values[i]:
                                            if (globals()[outputVariable]):
                                                color br_PRIMARY_TEXT_COLOR

                    ## scrollbar for large dropdowns
                    vbar value YScrollValue("[id]_viewport") unscrollable "hide" style "br_st_vbar"
