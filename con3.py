#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:39:14 2018

@author: guttappa
"""

import numpy as np
import matplotlib.pyplot as plt
a = [1,-1,1,-1]
b= [0.5,-0.5]
h1 = np.convolve(a,b)
print(h1)
plt.subplot(3,1,1)
plt.stem(a)
plt.subplot(3,1,2)
plt.stem(b)
plt.subplot(3,1,3)
plt.stem(h1)