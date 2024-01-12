## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

init python:

    class br_ScreenshotPainter(renpy.Displayable):
        DEBUG = True
        COLORS = ["#f00", "#0f0", "#00f"]

        def __init__(self, screenshotPath):
            super(br_ScreenshotPainter, self).__init__(self)

            self.editedScreenshot = None

            ## color index and brush size
            self._colorIndex = 0
            self._brushSize = 5

            ## the path to the screenshot we use as background
            self._path = screenshotPath
            
            ## control variables
            self._initialised = False
            self._drawing = False
            self._captureLine = False

            ## data stores
            self._lines = []
            self._surfaces = []

            ## creates a displayable based on the data we read from the image file
            self.bgDisplayable = im.Data(self.ReadScreenshot(screenshotPath), screenshotPath)


        @property
        def colorIndex(self):
            return self._colorIndex


        def visit(self):
            return [ self.bgDisplayable ]


        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            # ## create render object for the screenshot
            bg = renpy.render(self.bgDisplayable, width, height, st, at)           
            
            # ## if the scale factor was not yet calculated
            if (not self._initialised):
                
                ## mark this instance as initialise
                self._initialised = True

                ## get the size of the screenshot file so we can calculate the zoom factor
                imageSize = bg.get_size()
                zoomFactorX = width / imageSize[0]
                zoomFactorY = height / imageSize[1]

                ## zoom the background to the correct size
                ## we only want to do this once, otherwise the background will grow or shrink every render
                bg.zoom(zoomFactorX, zoomFactorY)

                if (br_ScreenshotPainter.DEBUG):
                    print("Initialised.")

            ## draw the background
            r.blit(bg, (0, 0))
            
            ## loop through all the lines and draw them
            lineCount = len(self._lines)

            if (self._lines and lineCount > 0):
                
                for i in range(lineCount):

                    ## cache a reference to the canvas
                    canvas = r.canvas()

                    ## if there are more that 1 point in the line, draw a line
                    if (len(self._lines[i][1]) > 1):
                        canvas.lines(self._lines[i][0], False, self._lines[i][1], self._brushSize)
                    ## if there are only one point in the line, draw a circle instead
                    ## we divide the brush size by 2 because it represents a width and we need a radius
                    else:
                        canvas.circle(self._lines[i][0], self._lines[i][1][0], self._brushSize / 2)
                    
                    ## if we are at the last line in the list and the signal to capture the line was sent
                    if (i == lineCount - 1 and self._captureLine):

                        ## we make sure to reset the signal back to false
                        self._captureLine = False

                        ## we then add the surface that we drew the line on to the surfaces list
                        self._surfaces.append(canvas.get_surface())
                        
                        if (br_ScreenshotPainter.DEBUG):
                            print(f"Surface captured! Surface count: {len(self._surfaces)}")

            return r           


        def event(self, ev, x, y, st):
            
            ## if the event was a mouse move event
            if (ev.type == 1024):
                
                ## if we are drawing
                if (self._drawing):

                    ## only draw if we have moved the mouse more than 10 pixels
                    ## we calculate the in distance squared to avoid sqrt operations
                    if (br_ScreenshotPainter.SqrDistance((x, y), self._lines[-1][1][-1]) > 10*10):

                        self._lines[-1][1].append((x, y))

                        renpy.redraw(self, 0)

                return

            ## if the left mouse button was clicked
            if (renpy.map_event(ev, 'mousedown_1')):
                self._drawing = True
                
                self._lines.append((br_ScreenshotPainter.COLORS[self._colorIndex], [(x, y)]))
                
                if (br_ScreenshotPainter.DEBUG):
                    print("Mouse 1 down event registered!")

                return
            
            ## if the right mouse button was clicked
            if (renpy.map_event(ev, 'mouseup_1')):
                self._drawing = False
                self._captureLine = True

                renpy.redraw(self, 0)

                if (br_ScreenshotPainter.DEBUG):
                    print("Mouse 1 up event registered!")

                return


        ## sets the current color, method is used by a screen action
        def SetColor(self, index):
            self._colorIndex = index

            if (br_ScreenshotPainter.DEBUG):
                print(f"Color was set to '{self._colorIndex}'.")


        ## clears all the edits made to the image
        def ClearEdits(self):
            
            ## clears the to data lists
            self._lines.clear()
            self._surfaces.clear()
            
            ## redraws the screen to make any lines disappear
            renpy.redraw(self, 0)

            if (br_ScreenshotPainter.DEBUG):
                print("Edits were cleared!")


        ## reads the the image file as a byte string 
        def ReadScreenshot(self, path):
            with open(path, "rb") as image:
                return image.read()


        def ConfirmEdits(self):
            import pygame

            ## if no edits were made, we just return
            if (len(self._surfaces) == 0):
                
                if (br_ScreenshotPainter.DEBUG):
                    print("No edits detected.")

                    return

            noExtension = self._path.rsplit(".")[0]
            savePath = f"{noExtension}_new.png"
            
            ## load the screenshot as a pygame surface
            background = pygame.image.load(self._path)

            ## loop through our saved surfaces
            for i in range(len(self._surfaces)):
                surface = self._surfaces[i]
                
                ## scale the surface up to fit the screenshots size
                surface = pygame.transform.scale(surface, (background.get_size()))

                ## draw the surface onto the screenshot
                background.blit(surface, surface.get_rect())
            
            pygame.image.save(background, savePath)
            
            with open(savePath, "rb") as file:
                self.editedScreenshot = file.read()

                br_main.editedScreenshotData = self.editedScreenshot

            if (br_ScreenshotPainter.DEBUG):
                print(f"Edits confirmed. Edits was saved to: {savePath}")


        @staticmethod
        def SqrDistance(point1, point2):
            return (point2[0] - point1[0])*(point2[0] - point1[0]) + (point2[1] - point1[1])*(point2[1] - point1[1])
