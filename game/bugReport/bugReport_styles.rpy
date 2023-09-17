## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## tooltip styles
style bugReport_tooltip_text:
    size 18
    color "#000"

style bugReport_tooltip_frame:
    background Frame("bugReport frame white", 11, 11)

## dropdown styles
style bugReport_dropdown_text:
    yalign 0.5
    color "#000"
    hover_color gui.hover_color
    size gui.text_size

style bugReport_dropdown_frame:
    background Frame("bugReport frame grey", 11, 11)
    hover_background Frame("bugReport frame white", 11, 11)

## dropdown options styles
style bugReport_dropdownOptions_text:
    yalign 0.5
    color "#444444"
    hover_color gui.hover_color
    size gui.text_size

style bugReport_dropdownOptions_frame:
    padding(0, 0)
    background Solid("#0000")
    hover_background Solid(gui.hover_muted_color)

## modal styles
style bugReport_modal_text:
    align(0.5, 0.5)
    color "#000"

style bugReport_modal_frame:
    align(0.5, 0.5)
    background Frame("bugReport frame grey", 11, 11)

style bugReport_modal_vbox:
    align(0.5, 0.5)
    spacing 100

## composite button styles
style bugReport_button_text:
    color "#000"
    hover_color gui.hover_color

style bugReport_button_frame:
    background Frame("bugReport frame grey", 11, 11)
    hover_background Frame("bugReport frame white", 11, 11)

## common styles
style bugReport_text:
    color "#fff"
    size 24

style bugReport_input:
    color "#000"
    size 24

style bugReport_vbar:
    bar_invert True
    top_gutter 16
    bottom_gutter 16
    thumb_offset 16
    base_bar Frame("bugReport vbar base", 16, 16)
    thumb Frame("bugReport vbar grey", 16, 16)
    hover_thumb Frame("bugReport vbar white", 16, 16)