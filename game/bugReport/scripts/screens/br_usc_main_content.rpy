## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

screen br_usc_main_content():
    
    ## close actions
    $ closeActions = Function(br_main.Close) if not br_main.description else Show("br_sc_confirmation_modal", None, "Are you sure you want to close the window. Your description will be lost!", Function(br_main.Close))
    
    ## fixed area that fills the available space
    fixed:
        xysize(1.0, 1.0)
        
        ## vbox for all the bits of the main screen
        vbox:
            xfill True

            text "Report a bug":
                xalign 0.5
                size 64

            null height 40

            text "Here you can report an issue directly to the developer. You must have an active internet connection to send the bug report."
            
            null height 40

            ## contact info
            hbox:
                ysize 40
                text "Contact information (optional)":
                    yalign 0.5
                
                ## small questing mark button for displaying a tooltip about contact info
                button:
                    xysize(24, 24)
                    
                    idle_background "br_i_info_idle"
                    hover_background "br_i_info_hover"
                    action NullAction()

                    tooltip "Providing contact information allows the developer to contact you in case they need more information about the issue.\n\nNOTE: If you wish to use an email and you are unable to enter the '@' symbol, please replace it with something like ' at '."
                
                text ":":
                    yalign 0.5

                null width 20

                ## frame for the text box
                frame:
                    style_prefix "br_st"
                    xysize(500, 40)
                    padding(0, 0)
                    background None

                    ## button for selecting the text field
                    button:
                        xysize(1.0, 1.0)

                        idle_background br_t_frame(br_PRIMARY_PANEL_COLOR)
                        hover_background br_t_frame(br_SECONDARY_PANEL_COLOR)

                        action [
                            CaptureFocus("input_contact_info"),
                            Show(
                                "br_sc_text_popup",
                                variable=br_main.contactInfo,
                                onChanged=br_main.OnContactInfoChanged,
                                focus="input_contact_info"
                            )
                        ]

                    ## otherwise if the contact info is not empty display it in a text instead
                    if (br_main.contactInfo):
                        
                        frame:
                            background None

                            text "[br_main.contactInfo]":
                                xsize 1.0
                                color br_PRIMARY_TEXT_COLOR
                
                ## if any contact info was given, display a dropdown where you can select the type of contact info you entered
                if (br_main.contactInfo):
                    
                    null width 20

                    text "Type:":
                        yalign 0.5
                    
                    fixed:
                        xysize (200, 40)
                        use br_usc_dropdown("contact_info_type_dropdown", br_main.CONTACT_INFO_TYPES, "br_main.contactInfoTypeIndex", pixelHeight=40)

            null height 40

            ## category dropdown
            hbox:
                ysize 40

                text "Please select a category: ":
                    yalign 0.5
                
                fixed:
                    xysize (400, 40)
                    use br_usc_dropdown("category_dropdown", br_main.CATEGORIES, "br_main.categoryIndex", pixelHeight=40)

            null height 40

            text "Please describe the issue below."
            
            null height 10

            ## description text box, functions similarly to the contact info box
            frame:
                style_prefix "br_st"
                xysize (1.0, 0.6)
                padding(0, 0)
                background None

                button:
                    xysize(1.0, 1.0)

                    idle_background br_t_frame(br_PRIMARY_PANEL_COLOR)
                    hover_background br_t_frame(br_SECONDARY_PANEL_COLOR)

                    action [
                        CaptureFocus("input_description"), 
                        Show(
                            "br_sc_text_popup", 
                            variable=br_main.description, 
                            onChanged=br_main.OnDescriptionChanged, 
                            focus="input_description", 
                            multiline=True
                        )
                    ]
                
                if (br_main.description):

                    frame:
                        background None
                        side "c r":

                            viewport id "viewport_description":
                                mousewheel True

                                text "[br_main.description]":
                                    xsize 1.0
                                    color br_PRIMARY_TEXT_COLOR

                            vbar value YScrollValue("viewport_description") unscrollable "hide" style "br_st_vbar"

            null height 40
            
            ## close and send buttons
            fixed:
                xysize(1.0, 80)

                fixed:
                    xalign 0.0
                    xsize 200
                    use br_usc_button("Close", actions=closeActions)

                fixed:
                    xalign 1.0
                    xsize 200
                    use br_usc_button("Send", actions=Function(br_main.TrySend), sensitiveIf=(br_allow_empty_description or br_main.description), notSensitiveTooltip="You must provide a description!")
            
            null height 40

            ## disclaimer at the bottom
            text "A bug report contains a screenshot, some system information and whatever you enter on this page.":
                xalign 0.5
    