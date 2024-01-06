## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_usc_dropdown(values, align=(0.0, 0.5), xysize=None, text_size=24, startIndex=0, outputVariableName=None):

    zorder 198

    default currentValueIndex = startIndex
    default isHovered = False

    style_prefix "br_st_dropdown"
    
    frame:
        if xysize is not None:
            xsize xysize[0]
        xfill True
        padding(0, 0)

        background None

        has vbox

        button:

            padding(0, 0)
            
            hovered SetLocalVariable("isHovered", True)
            unhovered SetLocalVariable("isHovered", False)

            frame:
                xfill True

                text values[currentValueIndex]:
                    size text_size
                
                fixed:
                    align (1.0, 0.5)
                    xysize (text_size, text_size)

                    if isHovered:
                        add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_HOVER_COLOR):
                            xysize(1.0, 1.0)
                    else:
                        add "bugReport/images/dropdown.webp" at br_t_tint(br_BUTTON_IDLE_COLOR):
                            xysize(1.0, 1.0)

            action CaptureFocus("options_dd")

        if GetFocusRect("options_dd"):
            dismiss action ClearFocus("options_dd")

            frame:
                if xysize is not None:
                    xsize xysize[0]
                    ysize xysize[1] * len(values) + 20

                side "c r":

                    viewport id "options":

                        mousewheel True
                        has vbox
                        for i in range(len(values)):
                            use br_usc_dropDownOption(values[i], i, currentValueIndex, text_size, [SetVariable(outputVariableName, values[i]), SetLocalVariable("currentValueIndex", i), ClearFocus("options_dd")])
                    
                    vbar value YScrollValue("options") unscrollable "hide" style "br_st_vbar"


screen br_usc_dropDownOption(name, i, selected, text_size, actions):
    style_prefix "br_st_dropdownOption"

    button:

        action actions

        frame:
            xfill True
                
            text name:
                size text_size

                if selected == i:
                    color "#000"
