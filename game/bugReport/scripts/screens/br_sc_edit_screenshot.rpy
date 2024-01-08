## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_sc_edit_screenshot:
    modal True
    zorder 200
    
    default painter = br_ScreenshotPainter(br_screenshot_path)

    $ cancelActions = Show("br_sc_confirmation_modal", None, "Are you sure you want to cancel? Your changes will not be saved.", Hide(CurrentScreenName()))
    $ confirmActions = [Function(painter.ConfirmEdits), Hide(CurrentScreenName())]

    key "game_menu" action [Hide(CurrentScreenName())]

    add "br_i_modalOverlay":
        xysize(1.0, 1.0)

    frame:
        padding(int(100 * (config.screen_width / config.screen_height)), 100)
        background None

        add painter

    hbox:
        ysize 50
        xalign 0.5
        ypos config.screen_height - 50
        yanchor 0.5
        spacing 20

        hbox:
            spacing 20

            for i in range(len(br_ScreenshotPainter.COLORS)):
                fixed:
                    xysize(50, 1.0)
                    use br_usc_button(
                        buttonIcon=br_t_frame(br_ScreenshotPainter.COLORS[i]), 
                        actions=Function(painter.SetColor, i),
                        sensitiveIf=(painter.colorIndex != i)
                        )

        null width 100
        
        hbox:
            spacing 20
            
            fixed:
                xysize(50, 1.0)
                use br_usc_button(
                    buttonIcon="bugReport/images/clear_icon.webp", 
                    actions=Function(painter.ClearEdits),
                    baseTooltip="Clear"
                    )
        
        null width 200

        hbox:
            spacing 50

            fixed:
                xysize(150, 1.0) 
                use br_usc_button(
                    buttonText="Cancel", 
                    actions=cancelActions
                    )

            fixed:
                xysize(150, 1.0)
                use br_usc_button(
                    buttonText="Confirm", 
                    actions=confirmActions
                    )
    
    ## exit button in the top right corner
    $ scaleFactor = config.screen_width / config.screen_height
    use br_usc_button_exit(cancelActions, (0.99, 0.01 * scaleFactor))

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