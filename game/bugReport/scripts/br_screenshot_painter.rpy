## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init python:

    class ScreenshotPainter(renpy.Displayable):

        def __init__(self, screenshotPath):
            renpy.Displayable.__init__(self)

            self.BRUSH_SIZE = 4
            self.BRUSH_COLOR = "#f00"

            self.oldTime = None
            
            self.screenshotData = self.ReadScreenshot(screenshotPath)
            ## creates a displayable based on the data we read from the image file
            self.screenshotDisplayable = im.Data(self.screenshotData, screenshotPath)

        ## reads the the image file as a byte string 
        def ReadScreenshot(self, path):
            with open(path, "rb") as image:
                return image.read()

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            if (self.oldTime is None):
                self.oldTime = st

            ## calculate delta time (time since last frame)
            deltaTime = st - self.oldTime
            self.oldTime = st

            ## create render object for the screenshot
            bg = renpy.render(self.screenshotDisplayable, width, height, st, at)           
            
            ## get the size of the screenshot file so we can calculate the zoom factor
            bg_x, bg_y = bg.get_size()
            xScaleFactor = width / bg_x
            yScaleFactor = height / bg_y

            ## zoom the image and then draw it using blit
            r.zoom(xScaleFactor, yScaleFactor)
            r.blit(bg, (0, 0))
            
            renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            import pygame

            if (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1):
                
                print("pressing mouse button 1")

                renpy.restart_interaction()