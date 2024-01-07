## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

image br_i_modalOverlay:
    Solid("#000000cc")

image br_i_idle_vbar_base:
    "bugReport/images/vbar_base.webp"
    matrixcolor TintMatrix(br_SECONDARY_BAR_IDLE_COLOR)

image br_i_hover_vbar_base:
    "bugReport/images/vbar_base.webp"
    matrixcolor TintMatrix(br_SECONDARY_BAR_HOVER_COLOR)

image br_i_idle_vbar:
    "bugReport/images/vbar.webp"
    matrixcolor TintMatrix(br_PRIMARY_BAR_IDLE_COLOR)

image br_i_hover_vbar:
    "bugReport/images/vbar.webp"
    matrixcolor TintMatrix(br_PRIMARY_BAR_HOVER_COLOR)

image br_i_info_idle:
    "bugReport/images/info.webp"
    matrixcolor TintMatrix(br_BUTTON_IDLE_COLOR)
    zoom 0.75

image br_i_info_hover:
    "bugReport/images/info.webp"
    matrixcolor TintMatrix(br_BUTTON_HOVER_COLOR)
    zoom 0.75