# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:24:50 2020

@author: comet
"""

import numpy as np


tmp = np.linspace(0,15,16).reshape(-1,1)
color_map = np.repeat(tmp, 4, axis=1)

img_index = np.random.randint(16, size=(50,50))
img = color_map[img_index,:]
