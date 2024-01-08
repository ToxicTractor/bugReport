## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_sc_edit_screenshot:
    modal True
    zorder 200
    
    default currentTool = 0
    default currentColor = 0

    key "game_menu" action [Hide(CurrentScreenName())]

    add "br_i_modalOverlay":
        xysize(1.0, 1.0)

    default painter = ScreenshotPainter(br_screenshot_path)

    frame:
        padding(100, 100)
        background None

        add painter

    hbox:
        ysize 50
        align(0.5, 0.98)
        spacing 20

        hbox:
            spacing 20
            for i in range(len(br_EDIT_SCREENSHOT_COLORS)):
                fixed:
                    xysize(50, 1.0)
                    use br_usc_button(
                        buttonIcon=br_t_frame(br_EDIT_SCREENSHOT_COLORS[i]), 
                        actions=SetScreenVariable("currentColor", i),
                        sensitiveIf=(currentColor != i)
                        )

        null width 100
        
        hbox:
            spacing 20

            fixed:
                xysize(50, 1.0)
                use br_usc_button(
                    buttonIcon="bugReport/images/pencil_icon.webp", 
                    actions=SetScreenVariable("currentTool", 0),
                    sensitiveIf=(currentTool == 1),
                    baseTooltip="Draw"
                    )

            fixed:
                xysize(50, 1.0)
                use br_usc_button(
                    buttonIcon="bugReport/images/eraser_icon.webp", 
                    actions=SetScreenVariable("currentTool", 1),
                    sensitiveIf=(currentTool == 0),
                    baseTooltip="Erase"
                    )
    
    ## exit button in the top right corner
    $ scaleFactor = config.screen_width / config.screen_height
    use br_usc_button_exit(Function(br_Close), (0.99, 0.01 * scaleFactor))

    ## get the current tooltip
    $ tooltip = GetTooltip()

    ## if the current tooltip is set and showTooltip is True, we show the tooltip
    if tooltip:

        nearrect:
            ypos -5
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                xmaximum 0.4
                padding(10, 5)
                
                style_prefix "br_st_tooltip"

                text tooltip