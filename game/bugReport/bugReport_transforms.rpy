## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

transform t_bugReport_tint(color):
    matrixcolor TintMatrix(color)

transform t_bugReport_exit_button(saturation):
    "bugReport/images/bugReport_exit.webp"
    matrixcolor SaturationMatrix(saturation)

transform t_bugReport_frame(color):
    Frame("bugReport/images/bugReport_frame.webp", 11, 11)
    matrixcolor TintMatrix(color)