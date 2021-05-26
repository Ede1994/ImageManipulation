# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Eric Einspaenner
"""
from PIL import Image, ImageDraw

#%% Function

# Change background from black to blue
def correctImagecolor(img):
        img = img.convert('RGB')
        width,heigth = img.size

        # iterate over all pixels and change black pixel into blue        
        for x in range(0, width):
            for y in range(1, heigth):
                r,g,b = img.getpixel((x,y))
                if r < 190 and g < 190:
                    r = 190
                    g = 190
                if b < 255:
                    b = 255
                img.putpixel((x,y),(r,g,b))

        return img

#%% main
if __name__=="__main__":
    # open image
    img = Image.open("data/bus_station.png")

    # call function
    new_img = correctImagecolor(img)
    new_img.show()
    size = img.size
    print(size,img.mode, img.format)
    
    # save result
    img.save("Output/bus_station_blau.png")

