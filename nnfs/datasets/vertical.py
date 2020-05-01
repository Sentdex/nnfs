import numpy as np


# Modified from:
# Copyright (c) 2015 Andrej Karpathy
# License: https://github.com/cs231n/cs231n.github.io/blob/master/LICENSE
# Source: https://cs231n.github.io/neural-networks-case-study/
def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        X[ix] = np.c_[np.random.randn(points)*.1 + (class_number)/3, np.random.randn(points)*.1 + 0.5]
        y[ix] = class_number
    return X, y
