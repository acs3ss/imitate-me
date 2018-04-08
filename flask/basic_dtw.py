#!/bin/env python
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def get_dtw(x, y):
    distance, path = fastdtw(x, y, dist=euclidean)
    return distance
