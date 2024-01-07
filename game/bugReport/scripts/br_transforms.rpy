## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

transform br_t_tint(color):
    matrixcolor TintMatrix(color)

transform br_t_exit_button(saturation):
    "bugReport/images/exit.webp"
    matrixcolor SaturationMatrix(saturation)

transform br_t_frame(color):
    Frame("bugReport/images/frame.webp", 11, 11)
    matrixcolor TintMatrix(color)