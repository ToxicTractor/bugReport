## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

define BUGREPORT_PRIMARY_PANEL_COLOR = "#aaa"
define BUGREPORT_SECONDAY_PANEL_COLOR = "#fff"
define BUGREPORT_BUTTON_IDLE_COLOR = "#888"
define BUGREPORT_BUTTON_HOVER_COLOR = "#ccc"
define BUGREPORT_PRIMARY_HOVER_COLOR = "#fff"
define BUGREPORT_PRIMARY_TEXT_COLOR = "#000"
define BUGREPORT_SECONDARY_TEXT_COLOR = "#444"
define BUGREPORT_PRIMARY_BAR_IDLE_COLOR = "#888"
define BUGREPORT_SECONDARY_BAR_IDLE_COLOR = "#444"
define BUGREPORT_PRIMARY_BAR_HOVER_COLOR = "#ccc"
define BUGREPORT_SECONDARY_BAR_HOVER_COLOR = "#555"

## tooltip styles
style bugReport_tooltip_text:
    size 18
    color BUGREPORT_PRIMARY_TEXT_COLOR

style bugReport_tooltip_frame:
    background t_bugReport_frame(BUGREPORT_SECONDAY_PANEL_COLOR)

## dropdown styles
style bugReport_dropdown_text:
    yalign 0.5
    color BUGREPORT_PRIMARY_TEXT_COLOR
    hover_color gui.hover_color
    size gui.text_size

style bugReport_dropdown_frame:
    background t_bugReport_frame(BUGREPORT_BUTTON_IDLE_COLOR)
    hover_background t_bugReport_frame(BUGREPORT_BUTTON_HOVER_COLOR)

## dropdown options styles
style bugReport_dropdownOptions_text:
    yalign 0.5
    color BUGREPORT_SECONDARY_TEXT_COLOR
    hover_color gui.hover_color
    size gui.text_size

style bugReport_dropdownOptions_frame:
    padding(0, 0)
    background Solid("#0000")
    hover_background Solid(gui.hover_muted_color)

## modal styles
style bugReport_modal_text:
    align(0.5, 0.5)
    color BUGREPORT_PRIMARY_TEXT_COLOR

style bugReport_modal_frame:
    align(0.5, 0.5)
    background t_bugReport_frame(BUGREPORT_PRIMARY_PANEL_COLOR)

style bugReport_modal_vbox:
    align(0.5, 0.5)
    spacing 100

## composite button styles
style bugReport_button_text:
    color BUGREPORT_PRIMARY_TEXT_COLOR
    hover_color gui.hover_color

style bugReport_button_frame:
    background None
    idle_background t_bugReport_frame(BUGREPORT_BUTTON_IDLE_COLOR)
    hover_background t_bugReport_frame(BUGREPORT_BUTTON_HOVER_COLOR)

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
    
    base_bar Frame("i_bugReport_[prefix_]vbar_base", 16, 16)
    thumb Frame("i_bugReport_[prefix_]vbar", 16, 16)