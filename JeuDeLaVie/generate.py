import pygame as pg
import numpy as np
import random 
import time
import sys
import os

def generate(lin, col, density):
    array = np.zeros((lin, col), dtype=int)
    cpt = 0
    for i in range(1, lin-1):
        for j in range(1, col-1):
            r = random.randint(1, 101)
            if r <= density and cpt <= ((lin * col) * density / 100 ):
                array[i][j] = 1
    return array
