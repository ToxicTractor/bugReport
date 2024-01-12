## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## replacement for the default notify that appears when a screenshot is taken. 
## zorder has been increased to make sure it is shown on top of the rest of the screens in the tool.
screen br_sc_notify(message):
    zorder 1000
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('br_sc_notify')