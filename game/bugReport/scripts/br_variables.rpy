## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

##---------------------------------------------------------------------
## report data
##---------------------------------------------------------------------
default br_category = None
default br_description = None
default br_contactInfo = None
default br_sentSuccessfully = None
default br_errorMessage = None
default br_screenshotPath = None
default br_originalRollbackSetting = None
default br_originalInputNextLine = None
default br_originalInputEnter = None


##---------------------------------------------------------------------
## other
##---------------------------------------------------------------------
define br_CATEGORIES = ["Spelling/Grammar/Text", "Critical/Progress Blocking", "Gameplay/Logic", "Visual/Graphical", "Other"]


##---------------------------------------------------------------------
## ui colors
##---------------------------------------------------------------------
define br_PRIMARY_PANEL_COLOR = "#aaa"
define br_SECONDAY_PANEL_COLOR = "#ccc"

define br_BUTTON_IDLE_COLOR = "#888"
define br_BUTTON_HOVER_COLOR = "#ccc"

define br_PRIMARY_TEXT_COLOR = "#000"
define br_SECONDARY_TEXT_COLOR = "#444"

define br_PRIMARY_BAR_IDLE_COLOR = "#888"
define br_SECONDARY_BAR_IDLE_COLOR = "#444"
define br_PRIMARY_BAR_HOVER_COLOR = "#ccc"
define br_SECONDARY_BAR_HOVER_COLOR = "#555"
