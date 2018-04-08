#!/bin/env python
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def get_dtw(x, y):
    distance, path = fastdtw(x, y, dist=euclidean)
    return distance

x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4]])
print(get_dtw(x, y))
