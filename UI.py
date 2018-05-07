""" Data Visualization
authors @ coreyacl, allisonbusa, junwonlee5

Holds the user interface code for the program currently run off of Pygame.

"""

import pygame as py
import os.path



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
    font = py.font.SysFont("couriernew",25)
    title = py.font.SysFont("couriernew",50)
    bg = py.image.load('FinalFigures/Wb-5.jpg')
    w,h = bg.get_size()
    bg = py.transform.scale(bg,(int(w*.7),int(h*.7)))
    listOfNames  = ['Farmer','Software Developer','Surgeon','Mechanical Engineer',
                    'Physicist','Plumber','Accountant']

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


        button = py.image.load('FinalFigures/arrow.png')
        scale = .25
        lx,ly = 1400,1000
        w,h = button.get_size()
        button = py.transform.scale(button,(int(w*scale),int(h*scale)))

        self.figures.append(button)
        self.locs.append((lx,ly))
        self.clickbox.append(gameDisplay.blit(button,(lx,ly)))

    def addFromFolder(self,*args):
        """ Adds figures from folder
        make sure that the files are names such in fileNames below
        the position can be modified with a new list that gets passed in the function
        just make sure that it's a list of tuples
        """
        # try:
        #     if not os.path.exists(args[0]):
        #         raise ValueError("Folder doesn't exist!")

        folder = args[0]
        pars  = args[1] if len(args) > 1 else \
        [(700,600,.9),(700,50,.9),(700,50,.9),(550,600,1),(50,50,1),(0,0,.05),(50,650,1)]
        fileNames = ['income','time','mort','population','gender','race','map']
        for x in range(len(pars)):
            if os.path.isfile(folder+fileNames[x]+'.png'):
                self.addFigure(str(folder+fileNames[x]+'.png'),pars[x])
            else:
                print(fileNames[x] + " not found for " + self.name)

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
        # try:
        #     if not os.path.exists(args[0]):
        #         raise ValueError("Folder doesn't exist!")

        img = py.image.load(fig)
        w,h = img.get_size()
        img = py.transform.scale(img,(int(w*scale),int(h*scale)))
        self.figures.append(img)
        self.locs.append((xl,yl))
        self.clickbox.append(self.gD.blit(img,(xl,yl)))

    def renderText(self,txt,pos,titleq=False):
        if titleq:
            txt_surf = self.title.render(txt,False,self.black)
        else:
            txt_surf = self.font.render(txt,False,self.black)
        txt_rect = txt_surf.get_rect(topleft=pos)
        self.gD.blit(txt_surf,txt_rect)

    def update(self,viewBackButton):
        """ Updates the screen with all necesarry details
        Does it IN ORDER so be careful
        """
        self.gD.fill(black)
        self.gD.blit(self.bg,(0,-600))
        if self.name == None:
            # if Main Screen basically
            self.renderText("Occupation",(30,50),True)
            self.renderText("Visualization",(30,110),True)
            self.renderText("Made by:",(30,470))
            self.renderText("Alli Busa",(30,500))
            self.renderText("Corey Cochran-Lepiz",(30,530))
            self.renderText("Junwon Lee",(30,560))
            for x in range(len(self.listOfNames)):
                self.renderText(self.listOfNames[x],(self.locs[x+1][0],self.locs[x+1][1]-30))
        else:
            self.renderText(self.name,(20,20),True)
        start = 0 if viewBackButton else 1

        for x in range(start,len(self.locs)):
            pos = self.locs[x]
            self.gD.blit(self.figures[x],pos)

""" Create the GUIs """
mainScreen = Screen(gameDisplay,None)

tlx,tly = 530,70
sf = .3
folder = 'FinalFigures'

mainScreen.addFigure(folder+'/Farmer/rep.jpg',tlx,tly,.25)
mainScreen.addFigure(folder+'/Software Developer/rep.jpg',tlx+530,tly,.27)

mainScreen.addFigure(folder+'/Surgeon/rep.jpg',tlx,tly+400,.25)
mainScreen.addFigure(folder+'/Mechanical Engineer/rep.jpg',tlx+530,tly+400,.27)

mainScreen.addFigure(folder+'/Physicist/rep.jpg',20,tly+770,.37)
mainScreen.addFigure(folder+'/Plumber/rep.JPG',tlx,tly+770,.25)
mainScreen.addFigure(folder+'/Accountant/rep.jpg',tlx+530,tly+770,.275)

phys = Screen(gameDisplay,'Physicist')
phys.addFromFolder(folder+'/Physicist/')

farmer = Screen(gameDisplay,'Farmer')
farmer.addFromFolder(folder+'/Farmer/')

software = Screen(gameDisplay,'Software Developer')
software.addFromFolder(folder+'/Software Developer/')

surgeon = Screen(gameDisplay,'Surgeon')
surgeon.addFromFolder(folder+'/Surgeon/')

meche = Screen(gameDisplay,'Mechanical Engineer')
meche.addFromFolder(folder+'/Mechanical Engineer/')

accountant = Screen(gameDisplay,'Accountant')
accountant.addFromFolder(folder+'/Accountant/')

plumber = Screen(gameDisplay,'Plumber')
plumber.addFromFolder(folder+'/Plumber/')

# ADD IN ORDER!!
screens = [mainScreen,farmer,software,surgeon,meche,phys,plumber,accountant]

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
