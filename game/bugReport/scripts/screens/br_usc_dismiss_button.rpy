## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## custom dismiss button
screen br_usc_dismiss_button(actions):
    fixed:
        ## make sure the entire screen is covered no matter where the element is placed
        pos(-2.0, -2.0)
        xysize(4.0, 4.0)

        button:
            xysize(1.0, 1.0)
            action actions
