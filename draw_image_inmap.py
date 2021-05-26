# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Eric Einspaenner
"""

from PIL import Image, ImageDraw
from operator import itemgetter

#%% Function

# draw image in map
def markers_station(cards, im):
    # read txt-file and save coord in lists
    with open("data/Messstellen.txt") as data:
        ids = []
        y_coords = []
        x_coords = []
        lines = data.readlines()
        for line in lines[1:]:
              ids.append(int(line[0]))
              y_coords.append(int(line[2:4]))
              x_coords.append(int(line[6:]))

    # call specific positions
    new_x = itemgetter(1,4,0)(x_coords)
    new_y = itemgetter(1,4,0)(y_coords)

    # draw images at specific position in map
    for y,x in zip(new_y, new_x):
        sqr_center = [x,y]
        sqr_length = 12

        cards.paste(im.resize((20,20)), (int(sqr_center[0] - sqr_length / 2), int(sqr_center[1] - sqr_length / 2)))

    return cards

#%% main
if __name__=="__main__":
    # open map
    cards = Image.open("data/Karte.png")
    
    # open image
    bus_im = Image.open("Output/bus_station_blau.png")
    
    cardssize = cards.size
    print('Mode:', cards.mode,'Größe:',cardssize)
    
    # call functions
    map_wMarkers = markers_station(cards, bus_im)
    map_wMarkers.show()
    map_wMarkers.save('Output/Map_with_bus_Markers.png')