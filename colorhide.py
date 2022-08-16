import numpy as np
from string import printable
from numba import jit

@jit
def fill(lenght, color):
    
    canvas = np.zeros( #GENERATING IMAGE
        (
            lenght, 128, 3
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

    if not keymap:

        keymap = dict()
        
        for char in range(len(printable)):
            keymap[printable[char]] = char

    color = sum([keymap[secure_key[i]] + i ^ 2 for i in range(len(secure_key))])
    color = ((color*2)%255, (color*3)%255, (color*4)%255)

    canvas = fill(len(text), color)

    for y in range(len(canvas)):
        canvas[y][keymap[text[y]]] = np.array([color])

    return canvas

def readit(canvas, secure_key = None, keymap = None):

    if not keymap:

        keymap = dict()

        for char in range(len(printable)):
            keymap[char] = printable[char]

    textmap = list()
    scalemap = dict()

    for char in range(len(printable)):
            scalemap[printable[char]] = char

    color = sum([scalemap[secure_key[i]] + i ^ 2 for i in range(len(secure_key))]) % 255
    color = ((color*2)%255, (color*3)%255, (color*4)%255)

    for y in range(len(canvas)):
        for x in range(len(canvas[0])):
            if np.array_equal(canvas[y][x], np.array(color, np.uint8)): 
                textmap.append(x)
                break
    
    return "".join([keymap[textmap[i]] for i in range(len(textmap))])

#Author: Serhat Dogan
#github.com/serhatdog
