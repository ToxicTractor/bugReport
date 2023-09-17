## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## this creates the button that you click on to open the bug report overlay
screen bugReport_buttonScreen():

    zorder 196

    ## local variables used to keep track of the hovered state
    default showTooltip = False
    default isHovered = False

    imagebutton auto "images/bugReport/bugReport_button_%s.webp":
        align(1.0, 1.0)

        hovered SetLocalVariable('isHovered', True)
        unhovered [SetLocalVariable('isHovered', False), SetLocalVariable('showTooltip', False)]

        action Function(OpenBugReportScreen)

        tooltip "Report a bug."
    
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
                
                style_prefix "bugReport_tooltip"

                text tooltip

## python functions used in the screens
init python:

    def OpenBugReportScreen():
        
        ## disable rollback while the bug report screen is open
        store.bugReport_originalRollbackSetting = config.rollback_enabled
        config.rollback_enabled = False

        ## Take a screen shot
        TakeBugReportScreenshot()

        ## show the bug report screen
        renpy.show_screen("bugReport_mainScreen")

    def TakeBugReportScreenshot():

        ## store the original screenshot callback
        oldScreenshotCallback = config.screenshot_callback
        
        ## set the screenshot callback to our callback method
        config.screenshot_callback = OnScreenshotTaken

        ## take a screenshot
        Screenshot()()

        ## restore the screenshot callback back to the original
        config.screenshot_callback = oldScreenshotCallback

    def OnScreenshotTaken(path):

        store.bugReport_screenshotPath = path
