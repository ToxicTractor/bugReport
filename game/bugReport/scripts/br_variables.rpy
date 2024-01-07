## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

##---------------------------------------------------------------------
## resetting variables
##---------------------------------------------------------------------
default br_description = None
default br_sent_successfully = None
default br_error_message = None
default br_screenshot_path = None
default br_original_rollback_setting = None
default br_original_input_next_line = None
default br_original_input_enter = None


##---------------------------------------------------------------------
## non-resetting variables
##---------------------------------------------------------------------
default br_contactInfo = None
default br_category_index = 0
default br_contact_info_index = 0


##---------------------------------------------------------------------
## dropdown options
##---------------------------------------------------------------------
define br_CATEGORIES = ["Spelling/Grammar/Text", "Critical/Progress Blocking", "Gameplay/Logic", "Visual/Graphical", "Other"]
define br_CONTACT_INFO_TYPES = ["Email", "Discord", "Other"]


##---------------------------------------------------------------------
## other settings
##---------------------------------------------------------------------
define br_allow_empty_description = True ## set this to 'False' if you want to force the player to put in a description


##---------------------------------------------------------------------
## ui colors
##---------------------------------------------------------------------
define br_PRIMARY_PANEL_COLOR = "#aaa"
define br_SECONDAY_PANEL_COLOR = "#ccc"

define br_BUTTON_IDLE_COLOR = "#888"
define br_BUTTON_HOVER_COLOR = "#ccc"
define br_BUTTON_INSENSITIVE_COLOR = "#555"

define br_PRIMARY_TEXT_COLOR = "#000"
define br_SECONDARY_TEXT_COLOR = "#444"
define br_PRIMARY_TEXT_HOVER_COLOR = "#222"

define br_PRIMARY_BAR_IDLE_COLOR = "#888"
define br_SECONDARY_BAR_IDLE_COLOR = "#444"
define br_PRIMARY_BAR_HOVER_COLOR = "#ccc"
define br_SECONDARY_BAR_HOVER_COLOR = "#555"
