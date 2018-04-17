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

class GUI():
    black = (0,0,0)
    white = (255,255,255)
    bx = 700
    by = 100

    font = py.font.SysFont("couriernew",32)

    def __init__(self,gD):
        self.gD = gD

    def update(self):
        self.gD.fill(white)
        box = py.surface.Surface((self.bx, self.by))
        txt_surf = self.font.render("Data Viz!", False, self.white)  # bottom line
        txt_rect = txt_surf.get_rect(center=(105, 40))
        box.blit(txt_surf, txt_rect)
        self.gD.blit(box,(30,0))



gui = GUI(gameDisplay)

while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYUP:
            if event.key == py.K_q:
                running = False
    # gameDisplay.fill(white)


    gui.update()
    py.display.update()
    clock.tick(60)
    # do stuff...


py.quit()
quit()
