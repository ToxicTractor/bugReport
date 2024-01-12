## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## reuseable button screen 
screen br_usc_button(buttonText=None, buttonIcon=None, actions=NullAction(), sensitiveIf=True, baseTooltip=None, notSensitiveTooltip=None):
    style_prefix "br_st_button"
    
    fixed:
        xysize(1.0, 1.0)
        
        button:
            padding(0, 0)

            action actions

            sensitive sensitiveIf

            ## if a base tooltip was given, display that
            if (bool(baseTooltip)):
                tooltip baseTooltip

            frame:
                padding(10, 10)
                xysize(1.0, 1.0)

                ## if an icon was given, show that
                if (bool(buttonIcon)):
                    add buttonIcon:
                        align(0.5, 0.5)
                        xysize(1.0, 1.0)

                ## if a text was given, show that
                if (bool(buttonText)):
                    text buttonText:
                        align(0.5, 0.5)

        ## if the button is not sensitive
        if (not sensitiveIf):

            ## we ma a new button with the same dimensions as the first, but with no visuals
            button:
                padding(0, 0)
                xysize(1.0, 1.0)

                ## null action to make sure we still react to hover events
                action NullAction()

                ## if the notSensitiveTooltip was given, show that
                if (bool(notSensitiveTooltip)):
                    tooltip notSensitiveTooltip
                ## otherwise if the base tooltip was given, show that
                elif (bool(baseTooltip)):
                    tooltip baseTooltip

## reuseable close button screen
screen br_usc_button_exit(actions, align=(1.0, 0.0)):

    ## more or less a standard image button with a fixed image
    imagebutton:
        align align

        ## using transforms to desaturate the image when it is not hovered
        idle br_t_exit_button(0.5)
        hover br_t_exit_button(1.0)

        action actions