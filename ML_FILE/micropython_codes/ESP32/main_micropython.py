## Standard
import gc
import time
import os
import machine
import math
from machine import Timer
from ucollections import deque
from ulab import numpy as np
## tinyml
from tinyml.model.model_gyr import clf_gyr
## WPC
import pywpc
DR = np.pi / 180 
class Queue(list):
    # first in, first out - FIFO
    def __init__(self, list):
        self.list = list
        self.size = len(list)
    
    def add(self, item):
        self.list.pop(0)
        self.list.append(item)

map_acc = {0 : "No_predicted acceleration", 1 : "X_acc", 2 : "Y_acc", 3 : "Z_acc"}

def most_frequent(list, return_max_freq = False):
    if not list:  # For the case of an empty list
        return (None, 0) if return_max_freq else None

    ## most_freq : most frequent element
    ## max_freq : frequence of the most frequent element
    most_freq_el = list[0]
    max_freq = 1
    h =  {}
    for items in list:
        if items not in h:
            h[items] = 1
        else:
            h[items] += 1

        if h[items] > max_freq:
            max_freq = h[items]
            most_freq_el = items
    if return_max_freq:
        return most_freq_el, max_freq
    return most_freq_el

data_acc = np.zeros(3)

data_bygone_gyr = np.zeros(3)
data_current_gyr = np.zeros(3)
data_diff_gyr = data_current_gyr - data_bygone_gyr

pred_acc = Queue([0 for i in range(7)])
pred_gyr = Queue([0 for i in range(7)])

wide_tab = np.zeros(42)
# wide_tab : "concatenation of seven classic tabs, 6x7 = 42, hence a such result

def read(g):
    t0 = time.ticks_ms()
    global data_acc, data_bygone_gyr, data_current_gyr, data_diff_gyr, wide_tab
    '''Read AI data.'''


    data_bygone_gyr = data_current_gyr
    data_current_gyr = np.array(pywpc.AHRS_getOrientation())
    data_diff_gyr = data_current_gyr - data_bygone_gyr

    data_acc = np.array(pywpc.AHRS_getAcceleration()) - 9.81*np.array([np.sin(DR*data_current_gyr[1]),
                                                np.sin(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1]), 
                                                np.cos(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1])]) 
    
    wide_tab = np.concatenate((data_acc, data_diff_gyr, wide_tab[:-6]))
    
    pred = clf_gyr(wide_tab)

    state = map_acc[pred]
    print(f"Sending move: pred: {pred}, type: { state} move {time.ticks_add(time.ticks_ms(), -t0)}")
    return pred

def read_sensor():
    pywpc.AHRS_start()
    '''Timer to periodically read sensor values.'''
    ##Timer(0).init(freq=config.READ_SENSOR_FREQ,
    ##             mode=Timer.PERIODIC,
    ##              callback=read)
    preds = []
    for i in range(17):
        preds.append(read(0))
        time.sleep(0.05)
    print(map[most_frequent(preds[7:])])
        
print('[Main] Starting script')

read_sensor()
