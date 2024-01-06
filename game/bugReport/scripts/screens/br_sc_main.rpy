## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## creates the main bug report screen.
screen br_sc_main():

    zorder 197

    modal True

    key "game_menu" action NullAction()

    frame:
        xysize(1.0, 1.0)
        xpadding 50

        style_prefix "br_st"

        background "br_i_modalOverlay"

        if renpy.android or renpy.ios:
            side "c r":
                area(0, 0, config.screen_width, int(config.screen_height / 2))

                viewport id "andorid_view":
                    child_size(config.screen_width - 150, config.screen_height)
                    draggable True

                    use br_usc_main_content

                vbar value YScrollValue("andorid_view") style "br_st_vbar"

        else:
            use br_usc_main_content
        
    ## exit button in the top right corner
    $ scaleFactor = config.screen_width / config.screen_height
    use br_usc_button_exit(Function(br_Close), (0.99, 0.01 * scaleFactor))
    