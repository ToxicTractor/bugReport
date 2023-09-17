## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## button screen for the main screen
screen bugReport_onScreenButton(buttonText, pos=None, anchor=None, align=None, actions=NullAction()):

    button:
        style_prefix "bugReport_button"

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