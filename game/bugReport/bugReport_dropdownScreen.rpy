## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen bugReport_dropdownScreen(values, align=(0.0, 0.5), xysize=None, text_size=24, startIndex=0, outputVariableName=None):

    zorder 198

    default currentValueIndex = startIndex
    default isHovered = False

    style_prefix "bugReport_dropdown"
    
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
                        add "bugreport_dropdown" at t_bugReport_tint(BUGREPORT_PRIMARY_HOVER_COLOR):
                            xysize(1.0, 1.0)
                    else:
                        add "bugreport_dropdown" at t_bugReport_tint(BUGREPORT_PRIMARY_PANEL_COLOR):
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
                            use bugReport_dropDownOptionScreen(values[i], i, currentValueIndex, text_size, [SetVariable(outputVariableName, values[i]), SetLocalVariable("currentValueIndex", i), ClearFocus("options_dd")])
                    vbar value YScrollValue("options") unscrollable "hide":
                        style "bugReport_vbar"

screen bugReport_dropDownOptionScreen(name, i, selected, text_size, actions):

    button:
        style_prefix "bugReport_dropdownOptions"

        action actions

        frame:
            xfill True
                
            text name:
                size text_size

                if selected == i:
                    color "#000"
