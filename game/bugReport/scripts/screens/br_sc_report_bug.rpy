## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## this creates the button that you click on to open the bug report overlay
screen br_sc_report_bug():

    zorder 196

    ## local variables used to keep track of the hovered state
    default showTooltip = False
    default isHovered = False

    imagebutton auto "bugReport/images/report_bug_%s.webp":

        align(1.0, 1.0)

        hovered SetLocalVariable('isHovered', True)
        unhovered [SetLocalVariable('isHovered', False), SetLocalVariable('showTooltip', False)]

        action Function(br_main.Open)

        tooltip "Report a bug"
    
    ## if the button is hovered, start the timer that will set 'showTooltip' to True
    if isHovered:

        timer 1.0 action SetLocalVariable('showTooltip', True)

    ## get the current tooltip
    $ tooltip = GetTooltip()

    ## if the current tooltip is set and showTooltip is True, we show the tooltip
    if tooltip and showTooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                
                style_prefix "br_st_tooltip"

                text tooltip
                