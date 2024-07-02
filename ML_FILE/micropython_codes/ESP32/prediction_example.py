'''
TinyML - Movement classification.py.

This example demonstrates how to detect the acceleration or the rotation of movement from time-series data.

The read_and_predict function uses measured acceleration and orientation to predict the movement.
Then, It will predict four situation:
-which is X-move, Y-move and Z-move and No Movement if you choose a model to predict acceleration.
-which is Roll, Pitch and Yaw and No Orientation if you choose a model to predict rotation.

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

import time
from ulab import numpy as np
import pywpc

## tinyml
from test_tree_acc import WPC_test_acceleration_tree
from test_model.tree_gyr import WPC_test_orientation_tree

from micropython_acc_AI import neural_network_acc
from micropython_gyr_AI import neural_network_gyr


## WPC
DR = np.pi / 180 
class Queue:
   '''First In, First Out - FIFO'''
    def __init__(self, n):
        self.list = np.zeros(n)
        self.size = n
        self.head = 0
    
    def add(self, item):
        self.list[self.head] = item
        self.head = (self.head + 1) % self.size

def most_frequent_element(list, return_max_freq = False):
    '''Returns most frequent element of a list, and optionally, the frequency of this element'''
    if not list:  # For the case of an empty list
        return (None, 0) if return_max_freq else None
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



def initialization(model, type = "TREE"):
    '''defines all the variables for prediction'''
    global data_acc, data_paste_gyr, data_current_gyr, data_diff_gyr, pred_acc, pred_gyr, wide_tab, MODEL, TYPE, MAP
    data_acc = np.zeros(3)

    data_past_gyr = np.zeros(3)
    data_current_gyr = np.zeros(3)
    data_diff_gyr = data_current_gyr - data_past_gyr

    pred_acc = Queue(7)
    pred_gyr = Queue(7)

    '''wide_tab is the "concatenation" of seven current tabs, 6x7 = 42, hence a such result'''
    wide_tab = np.zeros(42)

    MODEL = model
    TYPE = type
    '''type is in AI or TREE'''
    assert(TYPE in {"AI", "TREE"})


    map_tree_acc = {0 : "No_predicted acceleration", 1 : "X_acc", 2 : "Y_acc", 3 : "Z_acc"}
    map_tree_gyr = {0: "No predicted orientation", 1: "Pitch", 2: "Roll", 3: "Yaw"}
    map_ai_acc = {0: "X_acc", 1: "Y_acc", 2: "Z_acc", 3: "No predicted acceleration"}
    map_ai_gyr = {0: "No predicted orientation", 1: "Roll", 2: "Pitch", 3: "Yaw"} #can not be accurate for ai gyr


    mapping_by_model = {WPC_test_acceleration_tree: map_tree_acc, WPC_test_orientation_tree: map_tree_gyr, neural_network_acc: map_ai_acc, neural_network_gyr :map_ai_gyr}
    MAP = mapping_by_model[MODEL]



def read_and_predict(g):
    '''it reads the current data, and predicts the movement based on the last 7 data read'''
    global data_acc, data_current_gyr, data_diff_gyr, wide_tab
    t0 = time.ticks_ms()

    '''Read AI data.'''
    data_past_gyr = data_current_gyr
    data_current_gyr = np.array(pywpc.AHRS_getOrientation())
    data_diff_gyr = data_current_gyr - data_past_gyr

    '''remove the gravity component'''
    data_acc = np.array(pywpc.AHRS_getAcceleration()) - 9.81*np.array([np.sin(DR*data_current_gyr[1]),
                                                np.sin(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1]), 
                                                np.cos(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1])]) 
    
    wide_tab = np.concatenate((data_acc, data_diff_gyr, wide_tab[:-6]))
    
    
    if TYPE == "AI":
        pred = MODEL([wide_tab])
    else:
        pred = MODEL(wide_tab)
    
    state = MAP[pred]
    print(f"Sending move: pred: {pred}, type: { state} move {time.ticks_add(time.ticks_ms(), -t0)}")
    return pred


def main():
    '''predicts movement for 10 iterations, and return the most frequent prediction'''
    pywpc.AHRS_start()
    initialization(model = WPC_test_orientation_tree, type = "TREE")
    time.sleep(1)
    
    preds = []
    for i in range(17):
        preds.append(read_and_predict(0))
        time.sleep(0.05)
    print(MAP[most_frequent_element(preds[7:])])
       
print('[Main] Starting script')

main()