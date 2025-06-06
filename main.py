import pygame as pg

pg.init()
print('Setup Start')
window = pg.display.set_mode(size = (600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Check of all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # Close Window
            quit()    # end pygame