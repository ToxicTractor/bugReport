## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the main bug report screen.
screen br_sc_main():
    zorder 197
    modal True

    ## close actions
    $ closeActions = Function(br_main.Close) if not br_main.description else Show("br_sc_confirmation_modal", None, "Are you sure you want to close the window. Your description will be lost!", Function(br_main.Close))
    
    ## make sure that the "game_menu" key doesn't open the menu and instead does the closeActions
    key "game_menu" action closeActions

    ## the main frame
    frame:
        style_prefix "br_st"
        xysize(1.0, 1.0)
        xpadding 50

        ## set the background of the box to the modal overlay
        background "br_i_modalOverlay"

        ## display a mobile friendly version of the screen if we are on android or ios
        if renpy.android or renpy.ios:
            side "c r":
                area(0, 0, config.screen_width, int(config.screen_height / 2))

                viewport id "android_view":
                    child_size(config.screen_width - 150, config.screen_height)
                    draggable True

                    use br_usc_main_content

                vbar value YScrollValue("android_view") style "br_st_vbar"

        else:
            
            use br_usc_main_content
    
    ## edit screenshot button at the top right
    fixed:
        xysize(100, 100)
        yalign 0.2
        xanchor 1.0
        xpos config.screen_width - 50
        use br_usc_button(buttonIcon="bugReport/images/edit_screenshot.webp", actions=Show("br_sc_edit_screenshot"), baseTooltip="Edit the screenshot of the report.")

    ## exit button in the top right corner
    $ scaleFactor = config.screen_width / config.screen_height
    use br_usc_button_exit(closeActions, (0.99, 0.01 * scaleFactor))

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
    