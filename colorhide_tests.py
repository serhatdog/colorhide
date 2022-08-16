"""
HOW TO USE & EXPLANATION & TEST
"""
import numpy as np
from cv2 import imread, imwrite, IMWRITE_PNG_COMPRESSION
from string import printable
from numba import jit

@jit
def fill(lenght, color):
    canvas = np.zeros( #GENERATING IMAGE
        (
            len(text), 128, 3
        ),
        np.uint8
    )
    for y in range(len(canvas)):
        for x in range(len(canvas[0])): #FILLING THE IMAGE WITH RANDOM COLORS

            if np.random.randint(0,2) == 1: color1 = np.random.randint(color[0]+1, 255)
            else: color1 = np.random.randint(0, color[0]-1)

            if np.random.randint(0,2) == 1: color2 = np.random.randint(color[1]+1, 255)
            else: color2 = np.random.randint(0, color[1]-1)

            if np.random.randint(0,2) == 1: color3 = np.random.randint(color[2]+1, 255)
            else: color3 = np.random.randint(0, color[2]-1)

            canvas[y][x] = color1, color2, color3
    return canvas

def hideit(text, secure_key = None, keymap = None): 

    if not keymap: #GENERATING KEYMAP

        keymap = dict()
        
        for char in range(len(printable)):
            keymap[printable[char]] = char

    color = sum([keymap[secure_key[i]] + i ^ 2 for i in range(len(secure_key))]) #GENERATING KEY
    color = ((color*2)%255, (color*3)%255, (color*4)%255) # GENERATING COLORS FROM THE KEY

    canvas = fill(len(text), color)

    for y in range(len(canvas)): #PUTTING LETTERS (COLORS) INTO IMAGE
        canvas[y][keymap[text[y]]] = np.array([color]) 

    return canvas

def readit(canvas, secure_key = None, keymap = None):

    if not keymap: #GENERATING KEYMAP

        keymap = dict()

        for char in range(len(printable)):
            keymap[char] = printable[char]

    textmap = list()
    scalemap = dict()

    for char in range(len(printable)):
            scalemap[printable[char]] = char

    color = sum([scalemap[secure_key[i]] + i ^ 2 for i in range(len(secure_key))]) % 255 #DECODING KEY
    color = ((color*2)%255, (color*3)%255, (color*4)%255)

    for y in range(len(canvas)):
        for x in range(len(canvas[0])): #READING PIXELS
            if np.array_equal(canvas[y][x], np.array(color, np.uint8)): 
                textmap.append(x)
                break
    
    return "".join([keymap[textmap[i]] for i in range(len(textmap))])

text = """
colorhide test
"""

#WRITING IMAGE
from time import time as zaman
start = zaman()
imwrite("encodedimage.png", hideit(text, "s39951dcEa2"), [IMWRITE_PNG_COMPRESSION, 0])
print(zaman()-start)
st = zaman()
#READING FROM IMAGE
print(readit(imread("encodedimage.png"), "s39951dcEa2")) 
print(zaman()-st)
print(zaman()-start)

#300 letter without numba (jit)
#0.33/s write (opencv - png - compression 0)
#0.05/s read
#0.38/s total

#300 letter with numba (jit)
#0.04/s write (opencv - png - compression 0)
#0.06/s read
#0.1/s total

#15.850 letter without numba (jit)
#17.37/s write (opencv - png - compression 0)
#2.51/s read 
#19.88/s total

#30.058 letter with numba (jit)
#0.94/s write (opencv - png - compression 0)
#5.01/s read
#5.95/s total