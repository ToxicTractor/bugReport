## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

##---------------------------------------------------------------------
## tooltip styles
##---------------------------------------------------------------------
style br_st_tooltip_text:
    size 18
    color br_PRIMARY_TEXT_COLOR

style br_st_tooltip_frame:
    background br_t_frame(br_SECONDAY_PANEL_COLOR)


##---------------------------------------------------------------------
## dropdown styles
##---------------------------------------------------------------------
style br_st_dropdown_text:
    yalign 0.5
    color br_PRIMARY_TEXT_COLOR
    hover_color br_PRIMARY_TEXT_HOVER_COLOR
    size 24

style br_st_dropdown_frame:
    padding(0, 0)
    background br_t_frame(br_BUTTON_IDLE_COLOR)
    hover_background br_t_frame(br_BUTTON_HOVER_COLOR)


##---------------------------------------------------------------------
## dropdown options styles
##---------------------------------------------------------------------
style br_st_dropdown_option_text:
    yalign 0.5
    color br_SECONDARY_TEXT_COLOR
    hover_color br_PRIMARY_TEXT_HOVER_COLOR
    size 24

style br_st_dropdown_option_frame:
    padding(0, 0)
    background Solid("#0000")
    hover_background Solid(br_BUTTON_HOVER_COLOR)


##---------------------------------------------------------------------
## modal styles
##---------------------------------------------------------------------
style br_st_modal_text:
    align(0.5, 0.5)
    color br_PRIMARY_TEXT_COLOR

style br_st_modal_frame:
    align(0.5, 0.5)
    background br_t_frame(br_PRIMARY_PANEL_COLOR)

style br_st_modal_vbox:
    align(0.5, 0.5)
    spacing 100


##---------------------------------------------------------------------
## button styles
##---------------------------------------------------------------------
style br_st_button_text:
    color br_PRIMARY_TEXT_COLOR
    hover_color br_PRIMARY_TEXT_HOVER_COLOR
    insensitive_background br_SECONDARY_TEXT_COLOR

style br_st_button_frame:
    background None
    idle_background br_t_frame(br_BUTTON_IDLE_COLOR)
    hover_background br_t_frame(br_BUTTON_HOVER_COLOR)
    insensitive_background br_t_frame(br_BUTTON_INSENSITIVE_COLOR)


##---------------------------------------------------------------------
## common styles
##---------------------------------------------------------------------
style br_st_text:
    yalign 0.5
    color "#fff"
    size 24

style br_st_input:
    color "#000"
    size 24

style br_st_vbar:
    bar_invert True
    top_gutter 16
    bottom_gutter 16
    thumb_offset 16
    
    base_bar Frame("br_i_[prefix_]vbar_base", 16, 16)
    thumb Frame("br_i_[prefix_]vbar", 16, 16)