""" Data Visualization
authors @ coreyacl, allisonbusa, junwonlee5

Holds the user interface code for the program currently run off of Pygame.

"""

import pygame as py



""" initiate pygame """
py.init()
clock = py.time.Clock()
running = True

""" some important variables """
display_width = 1600

display_height = 1200
gameDisplay = py.display.set_mode((display_width,display_height))
py.display.set_caption("Occupation Viz")
black = (0,0,0)
white = (255,255,255)



class Screen():
    black = (0,0,0)
    white = (255,255,255)
    bx = 700
    by = 100
    font = py.font.SysFont("couriernew",32)

    def __init__(self,gD):
        """
        gD: gameDisplay for pygame
        figres: list of figures (pygame img)
        locs: list of location (tuple)
        clickbox: list of clickbox blits (pygame rectangle)


        """
        self.gD = gD
        self.figures = []
        self.locs = []
        self.clickbox = []


        button = py.image.load('initialgraphs/income.png')
        self.figures.append(button)
        self.locs.append((500,700))
        self.clickbox.append(gameDisplay.blit(button,(500,700)))

    def addFigure(self,fig,xl,yl,scale):
        """Creates a figure and places it at xl,yl
        fig: String of filename
        xl: x coordinate of figure (remember, top left is 0,0)
        yl: y coordinate of figure
        scale: scaling factor of figure
        """
        img = py.image.load(fig)
        w,h = img.get_size()
        img = py.transform.scale(img,(int(w*scale),int(h*scale)))
        self.figures.append(img)
        self.locs.append((xl,yl))
        self.clickbox.append(self.gD.blit(img,(xl,yl)))

    def update(self):
        """ Updates the screen with all necesarry details
        Does it IN ORDER so be careful


        """
        self.gD.fill(self.white)
        box = py.surface.Surface((self.bx, self.by))
        box.fill(self.white)
        txt_surf = self.font.render("Data Viz!", False, self.black)  # bottom line
        txt_rect = txt_surf.get_rect(center=(105, 40))
        box.blit(txt_surf, txt_rect)
        self.gD.blit(box,(30,0))
        for x in range(1,len(self.locs)):
            self.gD.blit(self.figures[x],self.locs[x])
            # self.gD.blit(self.clickbox[x])

""" Create the GUIs """
mainScreen = Screen(gameDisplay)
mainScreen.addFigure('mainFigures/farmer.jpeg',70,70,.6)
mainScreen.addFigure('mainFigures/phys.jpeg',820,70,.4)

phys = Screen(gameDisplay)
phys.addFigure('initialgraphs/physicist.png',40,50,.4)

farmer = Screen(gameDisplay)
farmer.addFigure('initialgraphs/farmerstate.png',80,90,.4)

# ADD IN ORDER!!
screens = [mainScreen,farmer,phys]

# b = gameDisplay.blit(mainScreen.figures[0],mainScreen.locs[0])

screenIndex = 0
while running:
    currentInterface = screens[screenIndex]

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYUP:
            if event.key == py.K_q:
                running = False
        if event.type == py.MOUSEBUTTONDOWN:
            #print event.button
            pos = py.mouse.get_pos()
            for x in range(len(currentInterface.locs)):
                if currentInterface.clickbox[x].collidepoint(pos):
                    if screenIndex == 0:
                        screenIndex = x
                    elif screenIndex > 0 and x == 0:
                        screenIndex = 0


            # print(xm,ym)
    gameDisplay.fill(white)


    currentInterface.update()
    py.display.update()
    clock.tick(60)
    # do stuff...


py.quit()
quit()
