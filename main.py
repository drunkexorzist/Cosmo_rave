import pygame as py

py.init()

window = py.display.set_mode((800, 600))

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()

py.quit()
quit()