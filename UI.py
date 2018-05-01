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
    bg = py.image.load('mainFigures/Bb-2.jpg')
    bg = py.transform.rotate(bg,270)
    w,h = bg.get_size()
    bg = py.transform.scale(bg,(int(w*.7),int(h*.7)))

    def __init__(self,gD,name):
        """
        gD: gameDisplay for pygame
        figres: list of figures (pygame img)
        locs: list of location (tuple)
        clickbox: list of clickbox blits (pygame rectangle)


        """
        self.gD = gD
        self.name = name
        self.figures = []
        self.locs = []
        self.clickbox = []


        button = py.image.load('mainFigures/button.png')
        scale = .25
        w,h = button.get_size()
        button = py.transform.scale(button,(int(w*scale),int(h*scale)))

        self.figures.append(button)
        self.locs.append((1220,850))
        self.clickbox.append(gameDisplay.blit(button,(1220,850)))

    def addFigure(self,fig,xl,yl,scale):
        fig: String of filename
        """Creates a figure and places it at xl,yl
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

    def update(self,viewBackButton):
        """ Updates the screen with all necesarry details
        Does it IN ORDER so be careful


        """
        self.gD.fill(black)
        self.gD.blit(self.bg,(0,-600))
        # box = py.surface.Surface((self.bx, self.by))
        # box.fill(self.white)
        # txt_surf = self.font.render("Data Viz!", False, self.black)  # bottom line
        # txt_rect = txt_surf.get_rect(center=(105, 40))
        # box.blit(txt_surf, txt_rect)
        # self.gD.blit(box,(30,0))
        start = 0 if viewBackButton else 1
        for x in range(start,len(self.locs)):
            pos = self.locs[x]
            # txt_surf = self.font.render(self.name, False, self.black)  # bottom line
            # txt_rect = txt_surf.get_rect(center=(105, 40))
            # box.blit(txt_surf, txt_rect)
            # bos = py.surface.Surface((pos[0],pos[1] - 20))
            #
            self.gD.blit(self.figures[x],pos)
            # self.gD.blit(self.clickbox[x])

""" Create the GUIs """
mainScreen = Screen(gameDisplay,None)

tlx,tly = 70,70
g1x,g1y = 0,0
g2x,g2y = 650,0
g3x,g3y = 0,550
g4x,g4y = 650,550
mainScreen.addFigure('mainFigures/farmer.jpeg',tlx,tly,.6)
mainScreen.addFigure('mainFigures/phys.jpeg',tlx+1130,tly,.4)
mainScreen.addFigure('mainFigures/software.jpg',tlx+530,tly,.35)

mainScreen.addFigure('mainFigures/surg.jpg',tlx,tly+400,.8)
mainScreen.addFigure('mainFigures/meche.jpg',tlx+530,tly+400,1)

mainScreen.addFigure('mainFigures/acc.jpg',tlx,tly+800,.45)
mainScreen.addFigure('mainFigures/plumb.JPG',tlx+530,tly+750,.12)

phys = Screen(gameDisplay,'Physicist')
phys.addFigure('mainFigures/income_for_physicist.png',g1x,g1y,.9)
phys.addFigure('mainFigures/Pie Chart for Physicists.png',g2x,g2y,.9)
phys.addFigure('mainFigures/Suicide Rate for Physicists.png',g3x,g3y,.9)
phys.addFigure('mainFigures/Population circle diagram for Physicist.png',g4x,g4y,1)

farmer = Screen(gameDisplay,'Farmer')
farmer.addFigure('mainFigures/income_for_farmers.png',g1x,g1y,.9)
farmer.addFigure('mainFigures/Pie Chart for Farmers.png',g2x,g2y,.9)
farmer.addFigure('mainFigures/Suicide Rate for Farmers.png',g3x,g3y,.9)
farmer.addFigure('mainFigures/Population circle diagram for Farmers.png',g4x,g4y,1)

software = Screen(gameDisplay,'Software Developer')
software.addFigure('mainFigures/income_for_software_developer.png',g1x,g1y,.9)
software.addFigure('mainFigures/Pie Chart for Software Developer.png',g2x,g2y,.9)
software.addFigure('mainFigures/Suicide Rate for Software Developers.png',g3x,g3y,.9)
software.addFigure('mainFigures/Population circle diagram for softdev.png',g4x,g4y,1)


surgeon = Screen(gameDisplay,'Surgeon')
surgeon.addFigure('mainFigures/income_for_surgeons.png',g1x,g1y,.9)
surgeon.addFigure('mainFigures/Pie Chart for Surgeons.png',g2x,g2y,.9)
surgeon.addFigure('mainFigures/Suicide Rate for Surgeons.png',g3x,g3y,.9)
surgeon.addFigure('mainFigures/Population circle diagram for Surgeons.png',g4x,g4y,1)

meche = Screen(gameDisplay,'Mechanical Engineer')
meche.addFigure('mainFigures/income_for_meche.png',g1x,g1y,.9)
meche.addFigure('mainFigures/Pie Chart for Mechanical Engineers.png',g2x,g2y,.9)
meche.addFigure('mainFigures/Suicide Rate for Mechanical Engineers.png',g3x,g3y,.9)
meche.addFigure('mainFigures/Population circle diagram for meche.png',g4x,g4y,1)

accountant = Screen(gameDisplay,'Accountant')
accountant.addFigure('mainFigures/income_for_accountant.png',g1x,g1y,.9)
accountant.addFigure('mainFigures/Pie Chart for Accountant.png',g2x,g2y,.9)
accountant.addFigure('mainFigures/Suicide Rate for Accountants.png',g3x,g3y,.9)
accountant.addFigure('mainFigures/Population circle diagram for accountants.png',g4x,g4y,1)

plumber = Screen(gameDisplay,'Plumber')
plumber.addFigure('mainFigures/income_for_plumbers.png',g1x,g1y,.9)
plumber.addFigure('mainFigures/Pie Chart for Plumbers.png',g2x,g2y,.9)
plumber.addFigure('mainFigures/Suicide Rate for Plumbers.png',g3x,g3y,.9)
plumber.addFigure('mainFigures/Population circle diagram for Plumbers.png',g4x,g4y,1)

# ADD IN ORDER!!
screens = [mainScreen,farmer,phys,software,surgeon,meche,accountant,plumber]

# b = gameDisplay.blit(mainScreen.figures[0],mainScreen.locs[0])

screenIndex = 0
while running:
    currentInterface = screens[screenIndex]

    for event in py.event.get():
        # print(event)
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYUP:
            if event.key == py.K_q:
                running = False
        if event.type == py.MOUSEBUTTONDOWN and py.mouse.get_pressed()[0]:
            pos = py.mouse.get_pos()
            for x in range(len(currentInterface.locs)):
                if currentInterface.clickbox[x].collidepoint(pos):
                    if screenIndex == 0:
                        screenIndex = x
                    elif screenIndex > 0 and x == 0:
                        screenIndex = 0


            # print(xm,ym)
    gameDisplay.fill(white)

    viewButton = True if screenIndex > 0 else False
    currentInterface.update(viewButton)
    if
    py.display.update()
    clock.tick(60)
    # do stuff...


py.quit()
quit()
