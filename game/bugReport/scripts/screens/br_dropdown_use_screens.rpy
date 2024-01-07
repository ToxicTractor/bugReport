## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_usc_dropdown(id, values, outputVariable, arrowSize=24, pixelHeight=40):
    style_prefix "br_st_dropdown"
    zorder 198

    default isIdle = True

    button:
        padding(0, 0)
        xysize (1.0, 1.0)
        
        hovered SetLocalVariable("isIdle", False)
        unhovered SetLocalVariable("isIdle", True)

        action [CaptureFocus(id), Show("br_sc_dropdown_options", None, id, values, outputVariable, pixelHeight)]
        
        frame:
            xsize 1.0
            padding(10, 0)

            text values[globals()[outputVariable]]:
                yalign 0.5

            fixed:
                xysize(arrowSize, arrowSize)
                align(1.0, 0.5)

                if isIdle:
                    add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_IDLE_COLOR):
                        xysize(1.0, 1.0)
                else:
                    add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_HOVER_COLOR):
                        xysize(1.0, 1.0)


screen br_sc_dropdown_options(id, values, outputVariable, pixelHeight, maxPixelHeight=500):
    style_prefix "br_st_dropdown"
    zorder 200
    modal True

    key "game_menu" action Hide(CurrentScreenName())

    use br_usc_dismiss_button(Hide(CurrentScreenName()))

    $ rect = GetFocusRect(id)

    if (rect):
        
        $ valueCount = len(values)
        $ boxHeight = int(min(pixelHeight * valueCount, maxPixelHeight))

        nearrect:
            focus id

            frame:
                xysize(int(rect[2]), boxHeight)

                side "c r":
                    viewport id "[id]_viewport":
                        mousewheel True
                        
                        has vbox

                        for i in range(valueCount):
                            button:
                                style_prefix "br_st_dropdown_option"
                                ysize pixelHeight
                                action [SetVariable(outputVariable, i), Hide(CurrentScreenName())]

                                frame:
                                    xysize(1.0, 1.0)
                                    text values[i]:
                                        if (globals()[outputVariable] == i):
                                            color br_PRIMARY_TEXT_COLOR
                
                    vbar value YScrollValue("[id]_viewport") unscrollable "hide" style "br_st_vbar"
