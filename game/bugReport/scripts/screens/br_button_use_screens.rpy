## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## button screen for the main screen
screen br_usc_button(buttonText, actions=NullAction(), sensitiveIf=True, notSensitiveTooltip=None):
    
    fixed:
        
        button:
            style_prefix "br_st_button"
            padding(0, 0)
            xysize(1.0, 1.0)

            action actions

            sensitive sensitiveIf

            frame:
                padding(25, 15)
                xysize(1.0, 1.0)
                text buttonText:
                    align(0.5, 0.5)

        if (not sensitiveIf):
            button:
                padding(0, 0)
                xysize(1.0, 1.0)

                action NullAction()

                if (bool(notSensitiveTooltip)):
                    tooltip notSensitiveTooltip


screen br_usc_button_exit(actions, align=(1.0, 0.0)):

    imagebutton:
        align align

        idle br_t_exit_button(0.5)
        hover br_t_exit_button(1.0)

        action actions