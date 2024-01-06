## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## button screen for the main screen
screen br_usc_button(buttonText, pos=None, anchor=None, align=None, actions=NullAction()):

    button:
        style_prefix "br_st_button"

        if align is not None:
            align align
        else:
            if pos is not None:
                pos pos
            if anchor is not None:
                anchor anchor

        padding(0, 0)

        action actions
        
        frame:
            padding(25, 15)
            
            text buttonText


screen br_usc_button_exit(actions, align=(1.0, 0.0)):

    imagebutton:
        align align

        idle br_t_exit_button(0.5)
        hover br_t_exit_button(1.0)

        action actions