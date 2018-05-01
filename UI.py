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

    def addFromFolder(self,*args):
        """ Adds figures from folder
        make sure that the files are names such in fileNames below
        the position can be modified with a new list that gets passed in the function
        just make sure that it's a list of tuples
        """
        folder = args[0]
        pars  = args[1] if len(args) > 1 else [(50,50,.9),(700,50,.9),(50,650,.9),(700,600,1)]
        fileNames = ['income','time','mort','population']
        for x in range(len(fileNames)):
            self.addFigure(str(folder+fileNames[x]+'.png'),pars[x])


    def addFigure(self,*args):
        if len(args) == 4:
            fig = args[0]
            xl = args[1]
            yl = args[2]
            scale = args[3]
        if len(args) == 2:
            fig = args[0]
            xl = args[1][0]
            yl = args[1][1]
            scale = args[1][2]

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
mainScreen.addFigure('mainFigures/Farmer/rep.jpeg',tlx,tly,.6)
mainScreen.addFigure('mainFigures/Physicist/rep.jpeg',tlx+1130,tly,.4)
mainScreen.addFigure('mainFigures/Software Developer/rep.jpg',tlx+530,tly,.35)

mainScreen.addFigure('mainFigures/Surgeon/rep.jpg',tlx,tly+400,.8)
mainScreen.addFigure('mainFigures/Mechanical Engineer/rep.jpg',tlx+530,tly+400,1)

mainScreen.addFigure('mainFigures/Accountant/rep.jpg',tlx,tly+800,.45)
mainScreen.addFigure('mainFigures/Plumber/rep.JPG',tlx+530,tly+750,.12)

phys = Screen(gameDisplay,'Physicist')
phys.addFromFolder('mainFigures/Physicist/')

farmer = Screen(gameDisplay,'Farmer')
farmer.addFromFolder('mainFigures/Farmer/')

software = Screen(gameDisplay,'Software Developer')
software.addFromFolder('mainFigures/Software Developer/')

surgeon = Screen(gameDisplay,'Surgeon')
surgeon.addFromFolder('mainFigures/Surgeon/')

meche = Screen(gameDisplay,'Mechanical Engineer')
meche.addFromFolder('mainFigures/Mechanical Engineer/')

accountant = Screen(gameDisplay,'Accountant')
accountant.addFromFolder('mainFigures/Accountant/')

plumber = Screen(gameDisplay,'Plumber')
plumber.addFromFolder('mainFigures/Plumber/')

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
    py.display.update()
    clock.tick(60)
    # do stuff...


py.quit()
quit()
