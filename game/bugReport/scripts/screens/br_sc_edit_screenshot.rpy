## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_sc_edit_screenshot:
    modal True
    zorder 200
    
    ## the screenshot painter displayable
    default painter = br_ScreenshotPainter(br_main.screenshotPath)
    
    ## actions for cancel and confirm
    $ cancelActions = Show("br_sc_confirmation_modal", None, "Are you sure you want to cancel? Your changes will not be saved.", Hide(CurrentScreenName()))
    $ confirmActions = [Function(painter.ConfirmEdits), Hide(CurrentScreenName())]

    ## make sure the "game_menu" key does not open the menu and instead does the cancel action
    key "game_menu" action cancelActions

    ## adds a slightly transparent black background
    add "br_i_modalOverlay"

    ## creates a frame for the screenshot painter, makes sure the width and height is in the same aspect ratio as the screen
    frame:
        padding(int(100 * (config.screen_width / config.screen_height)), 100)
        background None
        
        ## adds the screenshot painter to the frame
        add painter

    ## hbox for the buttons at the bottom of the screen
    hbox:
        ysize 50
        xalign 0.5
        ypos config.screen_height - 50
        yanchor 0.5
        spacing 20

        ## hbox for color buttons
        hbox:
            spacing 20

            ## creates a button for each color in the COLORS list of the screenshot painter class
            for i in range(len(br_ScreenshotPainter.COLORS)):
                fixed:
                    xysize(50, 1.0)
                    use br_usc_button(
                        buttonIcon=br_t_frame(br_ScreenshotPainter.COLORS[i]), 
                        actions=Function(painter.SetColor, i),
                        sensitiveIf=(painter.colorIndex != i)
                        )

        ## adds some whitespace
        null width 100
        
        ## hbox for tools, currently we only have clear so hbox is not strictly necessary
        hbox:
            spacing 20
            
            fixed:
                xysize(50, 1.0)
                use br_usc_button(
                    buttonIcon="bugReport/images/clear_icon.webp", 
                    actions=Function(painter.ClearEdits),
                    baseTooltip="Clear"
                    )
        
        ## adds some whitespace
        null width 200

        ## hbox for the cancel and confirm buttons
        hbox:
            spacing 50

            ## cancel button
            fixed:
                xysize(150, 1.0) 
                use br_usc_button(
                    buttonText="Cancel", 
                    actions=cancelActions
                    )
                    
            ## confirm button
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