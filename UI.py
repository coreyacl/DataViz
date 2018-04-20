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



class Interface():
    black = (0,0,0)
    white = (255,255,255)
    bx = 700
    by = 100
    font = py.font.SysFont("couriernew",32)

    def __init__(self,gD):
        self.gD = gD
        self.figures = []
        self.locs = []

        button = py.image.load('initialgraphs/income.png')
        self.figures.append(button)
        self.locs.append((500,700))

    def addFigure(self,fig,xl,yl):
        """Creates a figure and places it at xl,yl
        fig: String of filename
        xl: x coordinate of figure (remember, top left is 0,0)
        yl: y coordinate of figure

        """
        img = py.image.load(fig)
        self.figures.append(img)
        self.locs.append((xl,yl))

    def update(self):
        self.gD.fill(self.white)
        box = py.surface.Surface((self.bx, self.by))
        box.fill(self.white)
        txt_surf = self.font.render("Data Viz!", False, self.black)  # bottom line
        txt_rect = txt_surf.get_rect(center=(105, 40))
        box.blit(txt_surf, txt_rect)
        self.gD.blit(box,(30,0))
        for x in range(len(self.locs)):
            self.gD.blit(self.figures[x],self.locs[x])

""" Create the GUIs """
mainScreen = Interface(gameDisplay)

mainScreen.addFigure('initialgraphs/times.png',70,70)

phys = Interface(gameDisplay)

phys.addFigure('initialgraphs/physicist.png',40,50)

screens = [mainScreen,phys]

b = gameDisplay.blit(mainScreen.figures[0],mainScreen.locs[0])

screenIndex = 0
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYUP:
            if event.key == py.K_q:
                running = False
        if event.type == py.MOUSEBUTTONDOWN:
            #print event.button
            pos = py.mouse.get_pos()
            if b.collidepoint(pos):
                if screenIndex == 0:
                    screenIndex = 1
                elif screenIndex > 0:
                    screenIndex = 0


            # print(xm,ym)
    gameDisplay.fill(white)


    screens[screenIndex].update()
    py.display.update()
    clock.tick(60)
    # do stuff...


py.quit()
quit()
