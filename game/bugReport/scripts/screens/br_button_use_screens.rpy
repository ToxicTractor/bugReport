## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## button screen for the main screen
screen br_usc_button(buttonText=None, buttonIcon=None, actions=NullAction(), sensitiveIf=True, baseTooltip=None, notSensitiveTooltip=None):
    style_prefix "br_st_button"
    
    fixed:
        xysize(1.0, 1.0)
        
        button:
            padding(0, 0)

            action actions

            sensitive sensitiveIf

            if (bool(baseTooltip)):
                tooltip baseTooltip

            frame:
                padding(10, 10)
                xysize(1.0, 1.0)

                if (bool(buttonIcon)):
                    add buttonIcon:
                        align(0.5, 0.5)
                        xysize(1.0, 1.0)

                if (bool(buttonText)):
                    text buttonText:
                        align(0.5, 0.5)

        if (not sensitiveIf):
            button:
                padding(0, 0)
                xysize(1.0, 1.0)

                action NullAction()

                if (bool(notSensitiveTooltip)):
                    tooltip notSensitiveTooltip
                elif (bool(baseTooltip)):
                    tooltip baseTooltip

screen br_usc_button_exit(actions, align=(1.0, 0.0)):

    imagebutton:
        align align

        idle br_t_exit_button(0.5)
        hover br_t_exit_button(1.0)

        action actions