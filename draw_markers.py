# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Eric Einspaenner
"""
from PIL import Image, ImageDraw

#%% Function
# draw markers in map
def markers(cards):
    # read txt-file and store coordinates in lists
    with open("data/Messstellen.txt") as data:
        ids = []
        y_coords = []
        x_coords = []
        lines=data.readlines()
        for line in lines[1:]:
              ids.append(int(line[0]))
              y_coords.append(int(line[2:4]))
              x_coords.append(int(line[6:]))

    # draw map
    draw = ImageDraw.Draw(cards)
    
    # draw squares at specific locations on the map
    for y,x in zip(y_coords,x_coords):
        sqr_center = [x,y]
        sqr_length = 12
        
        sqr = (
        (sqr_center[0] + sqr_length / 2, sqr_center[1] + sqr_length / 2),
        (sqr_center[0] + sqr_length / 2, sqr_center[1] - sqr_length / 2),
        (sqr_center[0] - sqr_length / 2, sqr_center[1] - sqr_length / 2),
        (sqr_center[0] - sqr_length / 2, sqr_center[1] + sqr_length / 2)
        )
        
        draw.polygon(sqr,outline="black")

    return cards

#%% main
if __name__=="__main__":
    # open map/image
    cards = Image.open("data/Karte.png")

    # get image size
    cardssize = cards.size
    print('Mode:', cards.mode,'Größe:',cardssize)
    
    # call function and save result as png
    map_wMarkers = markers(cards)
    map_wMarkers.save('Output/Map_with_Markers.png')
