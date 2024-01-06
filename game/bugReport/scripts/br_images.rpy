## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

image br_i_modalOverlay:
    Solid("#000000cc")


image br_i_idle_vbar_base:
    "bugReport/images/bugReport_vbar_base.webp"
    matrixcolor TintMatrix(br_SECONDARY_BAR_IDLE_COLOR)


image br_i_hover_vbar_base:
    "bugReport/images/bugReport_vbar_base.webp"
    matrixcolor TintMatrix(br_SECONDARY_BAR_HOVER_COLOR)


image br_i_idle_vbar:
    "bugReport/images/bugReport_vbar.webp"
    matrixcolor TintMatrix(br_PRIMARY_BAR_IDLE_COLOR)


image br_i_hover_vbar:
    "bugReport/images/bugReport_vbar.webp"
    matrixcolor TintMatrix(br_PRIMARY_BAR_HOVER_COLOR)