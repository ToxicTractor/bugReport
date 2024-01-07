## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_usc_main_content():
    
    default selectedTextArea = 0
    default hoveringTextArea = 0

    $ CATEGORY_DD_SIZE = (400, 40)
    $ CATEGORY_DD_ID = "category_dropdown"
    $ CONTACT_INFO_DD_SIZE = (200, 40)
    $ CONTACT_INFO_DD_ID = "contact_info_type_dropdown"

    fixed:
        xysize(1.0, 1.0)
        
        vbox:
            xfill True

            text "Report a bug":
                xalign 0.5
                size 64

            null height 40

            text "Here you can report an issue directly to the developer. You must have an active internet connection to send the bug report."
            
            null height 40

            hbox:
                ysize 40
                text "Contact information (optional)":
                    yalign 0.5
                
                button:
                    xysize(24, 24)
                    
                    idle_background "br_i_info_idle"
                    hover_background "br_i_info_hover"
                    action NullAction()

                    tooltip "Providing contact information allows the developer to contact you in case they need more information about the issue.\n\nNOTE: If you wish to use an email and you are unable to enter the '@' symbol, please replace it with something like ' at '."
                
                text ":":
                    yalign 0.5

                null width 20

                frame:
                    style_prefix "br_st"
                    xysize(500, 40)

                    if (hoveringTextArea == 1 or selectedTextArea == 1):
                        background br_t_frame(br_SECONDAY_PANEL_COLOR)
                    else:
                        background br_t_frame(br_PRIMARY_PANEL_COLOR)

                    button:
                        xysize(1.0, 1.0)

                        hovered SetLocalVariable("hoveringTextArea", 1)
                        unhovered SetLocalVariable("hoveringTextArea", 0)

                        action [SetLocalVariable("selectedTextArea", 1), SetLocalVariable("hoveringTextArea", 0)]

                    if (selectedTextArea == 1):

                        input:
                            if (br_contactInfo is not None):
                                default br_contactInfo
                            xysize(1.0, 1.0)
                            changed br_OnContactInfoChanged

                    elif (br_contactInfo is not None):

                        text "[br_contactInfo]":
                            xsize 1.0
                            color br_PRIMARY_TEXT_COLOR
                
                if (br_contactInfo):
                    
                    null width 20

                    text "Type:":
                        yalign 0.5
                    
                    fixed:
                        xysize CONTACT_INFO_DD_SIZE
                        use br_usc_dropdown(CONTACT_INFO_DD_ID, br_CONTACT_INFO_TYPES, "br_contact_info_index", pixelHeight=CONTACT_INFO_DD_SIZE[1])

            null height 40

            hbox:
                ysize CATEGORY_DD_SIZE[1]

                text "Please select a category: ":
                    yalign 0.5
                
                fixed:
                    xysize CATEGORY_DD_SIZE
                    use br_usc_dropdown(CATEGORY_DD_ID, br_CATEGORIES, "br_category_index", pixelHeight=CATEGORY_DD_SIZE[1])

            null height 40

            text "Please describe the issue below."
            
            null height 10

            frame:
                style_prefix "br_st"
                xysize (1.0, 0.6)

                if (hoveringTextArea == 2 or selectedTextArea == 2):
                    background br_t_frame(br_SECONDAY_PANEL_COLOR)
                else:
                    background br_t_frame(br_PRIMARY_PANEL_COLOR)

                button:
                    xysize(1.0, 1.0)

                    hovered SetLocalVariable("hoveringTextArea", 2)
                    unhovered SetLocalVariable("hoveringTextArea", 0)

                    action [SetLocalVariable("selectedTextArea", 2), SetLocalVariable("hoveringTextArea", 0)]

                side "c r":

                    viewport id "viewport_description":
                        mousewheel True
                        
                        if (selectedTextArea == 2):

                            input:
                                if (br_description is not None):
                                    default br_description
                                xsize 1.0
                                multiline True
                                changed br_OnDescriptionChanged

                        elif (br_description is not None):

                            text "[br_description]":
                                xsize 1.0
                                color br_PRIMARY_TEXT_COLOR
                        
                    vbar value YScrollValue("viewport_description") unscrollable "hide" style "br_st_vbar"

            null height 40

            fixed:
                xysize(1.0, 80)

                fixed:
                    xalign 0.0
                    xsize 200
                    use br_usc_button("Close", Function(br_Close))

                fixed:
                    xalign 1.0
                    xsize 200
                    use br_usc_button("Send", Function(br_TrySend), (br_allow_empty_description or bool(br_description)), "You must provide a description!")
            
            null height 40

            text "A bug report contains a screenshot, some system information and whatever you enter on this page.":
                xalign 0.5
    
    if (selectedTextArea != 0):
        use br_usc_dismiss_button(SetLocalVariable("selectedTextArea", 0))
    