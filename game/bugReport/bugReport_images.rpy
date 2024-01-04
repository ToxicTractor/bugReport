## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

image bugReport_modalOverlay:
    Solid("#000000cc")

image i_bugReport_idle_vbar_base:
    "bugreport_vbar_base"
    matrixcolor TintMatrix(BUGREPORT_SECONDARY_BAR_IDLE_COLOR)

image i_bugReport_hover_vbar_base:
    "bugreport_vbar_base"
    matrixcolor TintMatrix(BUGREPORT_SECONDARY_BAR_HOVER_COLOR)

image i_bugReport_idle_vbar:
    "bugreport_vbar"
    matrixcolor TintMatrix(BUGREPORT_PRIMARY_BAR_IDLE_COLOR)

image i_bugReport_hover_vbar:
    "bugreport_vbar"
    matrixcolor TintMatrix(BUGREPORT_PRIMARY_BAR_HOVER_COLOR)