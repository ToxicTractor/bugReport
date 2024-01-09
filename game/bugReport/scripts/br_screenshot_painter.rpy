## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init python:
    import pygame

    class ScreenshotPainter(renpy.Displayable):
        

        def __init__(self, screenshotPath, colors):
            renpy.Displayable.__init__(self)

            self.tool = 0
            self.color = 0

            self.COLORS = colors

            self.oldTime = None
            
            self.screenshotPath = screenshotPath
            self.screenshotData = self.ReadScreenshot(screenshotPath)
            ## creates a displayable based on the data we read from the image file
            self.screenshotDisplayable = im.Data(self.screenshotData, screenshotPath)

            self.imageSize = None
            self.scaleFactorX = None
            self.scaleFactorY = None
            self.zoomFactorX = None
            self.zoomFactorY = None

            self.scaledMousePos = (0, 0)
            self.canvas = None
            self.edits = []
            self.lines = []
            self._currentLineIndex = None


        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            

            if (self.oldTime is None):
                self.oldTime = st

            ## calculate delta time (time since last frame)
            deltaTime = st - self.oldTime
            self.oldTime = st

            ## create render object for the screenshot
            bg = renpy.render(self.screenshotDisplayable, width, height, st, at)           
            

            ## if the scale factor was not yet calculated
            if (self.imageSize is None):
                
                ## get the size of the screenshot file so we can calculate the zoom factor
                self.imageSize = bg.get_size()

                self.zoomFactorX = width / self.imageSize[0]
                self.zoomFactorY = height / self.imageSize[1]
                self.scaleFactorX = self.imageSize[0] / width
                self.scaleFactorY = self.imageSize[1] / height


            ## zoom the image and then draw it using blit
            r.zoom(self.zoomFactorX, self.zoomFactorY)
            r.blit(bg, (0, 0))
            
            
            self.canvas = r.canvas()
            self.DrawEdits()

            mousePressed = pygame.mouse.get_pressed()[0]

            if (self.scaledMousePos[0] > 0 & self.scaledMousePos[0] < self.imageSize[0] and
                self.scaledMousePos[1] > 0 & self.scaledMousePos[1] < self.imageSize[1]):
                
                if (mousePressed):
                    
                    if self._currentLineIndex is not None:
                        self.lines[self._currentLineIndex][2].append(self.scaledMousePos)
                    else:
                        self.edits.append(self.CurrentColor(), self.scaledMousePos, 4)

                    self.canvas.circle(self.CurrentColor(), self.scaledMousePos, 4)

            renpy.redraw(self, 0)

            return r           


        def event(self, ev, x, y, st):

            xScaled = int(x * self.scaleFactorX)
            yScaled = int(y * self.scaleFactorY)

            self.scaledMousePos = (xScaled, yScaled)

            if (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1):
                
                if (self._currentLineIndex is None):
                    self._currentLineIndex = 0
                
                self.lines.append((self.CurrentColor(), False, [self.scaledMousePos], 4))

                renpy.restart_interaction()

            if (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1):

                if (len(self.lines[self._currentLineIndex][2]) > 1):
                    self._currentLineIndex += 1
                else:
                    self.lines.pop()

                renpy.restart_interaction()


        def CreatePixelArray(self, width, height):
            print((width, height))
            self.pixels = []
            
            for y in range(int(height)):
                for x in range(int(width)):
                    self.pixels.append((0, 0, 0, 0))


        def DrawEdits(self):

            for i in range(len(self.lines)):
                
                if len(self.lines[i][2]) > 1:
                    self.canvas.lines(*self.lines[i])

            for i in range(len(self.edits)):
                self.canvas.circle(*self.edits[i])


        ## sets the current color
        def SetColor(self, index):
            self.color = index


        ## sets the current tool
        def SetTool(self, index):
            self.tool = index


        def CurrentColor(self):
            return self.COLORS[self.color]


        ## clears all the edits made to the image
        def ClearEdits(self):
            self.edits = []
            self.lines = []
            self._currentLineIndex = None


        ## reads the the image file as a byte string 
        def ReadScreenshot(self, path):
            with open(path, "rb") as image:
                return image.read()


        def ConfirmEdits(self):

            return



            
            

            
