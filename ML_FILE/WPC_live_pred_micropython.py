# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_GetData.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.




#always check the map dictionaries and adapt if necessary

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog
import pyqtgraph as pg
import pretty_errors
## Python
import datetime
import os
import glob
import csv
import time
import pickle
import pandas as pd
import numpy as np
## WPC
from wpcsys import pywpc

from micropython_codes.ESP32.temporary_models.test_tree_gyr import WPC_test_orientation_tree
from micropython_codes.ESP32.temporary_models.test_tree_acc import WPC_test_acceleration_tree

from micropython_codes.ESP32.temporary_models.micropython_gyr_AI import neural_network_gyr
from micropython_codes.ESP32.temporary_models.micropython_acc_AI import neural_network_acc


PATH: str = 'data_sensor/'

DEG_TO_RAD = np.pi / 180

if os.path.basename(os.getcwd()) != "ML_FILE":
    os.chdir('ML_FILE')


## choose the model HERE:
MODEL_GYR, MODEL_ACC = WPC_test_orientation_tree, WPC_test_acceleration_tree
TYPE = "TREE" #type is AI or in TREE
assert(TYPE in {"AI", "TREE"})


map_tree_acc = {0 : "No_predicted acceleration", 1 : "X_acc", 2 : "Y_acc", 3 : "Z_acc"}
map_tree_gyr = {0: "No predicted orientation", 1: "Pitch", 2: "Roll", 3: "Yaw"}
map_ai_acc = {0: "X_acc", 1: "Y_acc", 2: "Z_acc", 3: "No predicted acceleration"}
map_ai_gyr = {0: 0, 1: 1, 2: 2, 3: 3}
mapping_by_model = {WPC_test_acceleration_tree: map_tree_acc, WPC_test_orientation_tree: map_tree_gyr,
                     neural_network_acc: map_ai_acc, neural_network_gyr: map_ai_gyr}
map_gyr = mapping_by_model[MODEL_GYR]
map_acc = mapping_by_model[MODEL_ACC]

class Queue(list):
    def __init__(self, list):
        self.list = list
        self.size = len(list)
    
    def add(self, item):
        self.list.pop(0)
        self.list.append(item)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(458, 180)
        self.VerticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.FormLayout = QtWidgets.QFormLayout()
        self.FormLayout.setObjectName("FormLayout")
        self.LabelIP = QtWidgets.QLabel(Dialog)
        self.LabelIP.setObjectName("LabelIP")
        self.FormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelIP)
        self.LineEditIP = QtWidgets.QLineEdit(Dialog)
        self.LineEditIP.setObjectName("LineEditIP")
        self.FormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEditIP)
        self.OnlyInt = QtGui.QIntValidator()
        self.LabelIntervalTime = QtWidgets.QLabel(Dialog)
        self.LabelIntervalTime.setObjectName("LabelIntervalTime")
        self.FormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.LabelIntervalTime)
        self.LineEditSamplingTime = QtWidgets.QLineEdit(Dialog)
        self.LineEditSamplingTime.setObjectName("LineEditSamplingTime")
        self.LineEditSamplingTime.setValidator(self.OnlyInt)
        self.FormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LineEditSamplingTime)
        self.VerticalLayout.addLayout(self.FormLayout)
        self.ButtonBoxOkCancel = QtWidgets.QDialogButtonBox(Dialog)
        self.ButtonBoxOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBoxOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ButtonBoxOkCancel.setObjectName("ButtonBoxOkCancel")
        self.VerticalLayout.addWidget(self.ButtonBoxOkCancel)        

        self.retranslateUi(Dialog)
        ## The connection with Ok and Cancel button for the Dialog
        self.ButtonBoxOkCancel.accepted.connect(Dialog.accept) 
        self.ButtonBoxOkCancel.rejected.connect(Dialog.reject) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    ## Get the parameters filled from the Dialog    
    def get_parameters(self):
        IPSENSOR = self.LineEditIP.text()
        SAMPLINGTIME = int(self.LineEditSamplingTime.text())
        return IPSENSOR, SAMPLINGTIME

    ## Establish the text for the Dialog
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LabelIP.setText(_translate("Dialog", "IP adress"))
        self.LineEditIP.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.LineEditIP.setText(_translate("Dialog", "192.168.5.39"))
        self.LabelIntervalTime.setText(_translate("Dialog", "Interval Time (ms)"))
        self.LineEditSamplingTime.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.LineEditSamplingTime.setText(_translate("Dialog", "50"))

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 477)
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.VerticalLayout = QtWidgets.QVBoxLayout(self.CentralWidget)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.HorizontalLayoutInput = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutInput.setObjectName("HorizontalLayoutInput")
        self.LineEditIP = QtWidgets.QLineEdit(self.CentralWidget)
        self.LineEditIP.setObjectName("LineEditIP")
        self.HorizontalLayoutInput.addWidget(self.LineEditIP)
        self.LineEditSamplingTime = QtWidgets.QLineEdit(self.CentralWidget)
        self.LineEditSamplingTime.setObjectName("LineEditSamplingTime")
        self.HorizontalLayoutInput.addWidget(self.LineEditSamplingTime)
        
        
        self.SartStopButton = QtWidgets.QPushButton(self.CentralWidget)
        self.SartStopButton.setObjectName("SartStopButton")
        self.HorizontalLayoutInput.addWidget(self.SartStopButton)
        self.SartStopButton.clicked.connect(lambda : self.toggle_timer('Roll'))
        
        
        self.QuitButton = QtWidgets.QPushButton(self.CentralWidget)
        self.QuitButton.setAutoFillBackground(False)
        self.QuitButton.setObjectName("QuitButton")
        self.QuitButton.clicked.connect(lambda: self.quit(MainWindow = MainWindow))
        self.HorizontalLayoutInput.addWidget(self.QuitButton)
        self.VerticalLayout.addLayout(self.HorizontalLayoutInput)
        
        self.GraphicsViewRot = pg.PlotWidget(self.CentralWidget)
        self.GraphicsViewRot.setBackground('w')
        self.GraphicsViewRot.showGrid(x = True, y = True, alpha = 0.5)
        self.GraphicsViewRot.setObjectName("GraphicsViewRot")
        
        self.GraphicsViewAcc = pg.PlotWidget(self.CentralWidget)
        self.GraphicsViewAcc.setBackground('w')
        self.GraphicsViewAcc.showGrid(x = True, y = True, alpha = 0.5)
        self.GraphicsViewAcc.setObjectName("GraphicsViewAcc")
        
        
        
        self.VerticalLayout.addWidget(self.GraphicsViewRot)
        self.VerticalLayout.addWidget(self.GraphicsViewAcc)
        
        self.ProgressBar = QtWidgets.QProgressBar(self.CentralWidget)
        self.ProgressBar.setProperty("value", 100)
        self.ProgressBar.setObjectName("ProgressBar")
        self.VerticalLayout.addWidget(self.ProgressBar)
        

        self.VerticalLayoutPred = QtWidgets.QVBoxLayout(self.CentralWidget)
        self.VerticalLayoutPred.setObjectName("VerticalLayoutPred")

        self.LineEditTypeAcc = QtWidgets.QLineEdit(self.CentralWidget)
        self.LineEditTypeAcc.setObjectName("LineEditTypeAcc")
        self.VerticalLayoutPred.addWidget(self.LineEditTypeAcc)

        self.LineEditTypeOri = QtWidgets.QLineEdit(self.CentralWidget)
        self.LineEditTypeOri.setObjectName("LineEditTypeOri")
        self.VerticalLayoutPred.addWidget(self.LineEditTypeOri)

        self.HorizontalLayoutInput.addLayout(self.VerticalLayoutPred)
        
        MainWindow.setCentralWidget(self.CentralWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 632, 22))
        self.MenuBar.setObjectName("MenuBar")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.connection_started = False
        
        self.sampling_time = 50 #ms, defaut value, #interval time of the data
        self.dev = pywpc.WifiDAQE3AH()
        self.read_delay = 0.5 #second
        self.sampling_period_device = 0.003
        self.timeout = 1 #second # 3 seconds by default
        self.data = None
        self.timer_running =False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LineEditIP.setText(_translate("MainWindow", IPSENSOR))
        self.LineEditIP.setReadOnly(True)
        self.LineEditSamplingTime.setText(_translate("MainWindow", f"sampled time: {SAMPLINGTIME} ms"))
        self.LineEditSamplingTime.setReadOnly(True)
        self.LineEditTypeAcc.setText(_translate("MainWindow", f"Neutral"))
        self.LineEditTypeAcc.setReadOnly(True)
        self.LineEditTypeOri.setText(_translate("MainWindow", f"Neutral"))
        self.LineEditTypeOri.setReadOnly(True)
        self.SartStopButton.setText(_translate("MainWindow", "Start"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))
        
        
    def toggle_timer(self, type):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False
        else:
            if not self.connection_started:
                self.connect()
                self.data = []   
                self.add_measure(data = self.data, sampling_time = SAMPLINGTIME)
            else:        
                self.timer.start()
                self.timer_running = True

    #use a list of dict, because calcul are more efficient in time than with a dataframe from pandas
    def csv_to_list_dict(self, path):
        with open(path, mode = 'r') as file:
            reader = csv.DictReader(file)
            list_dict = [row for row in reader] 
        return list_dict

    def get_max_ID(self, data: list):
        ids = [int(d['ID']) for d in data if 'ID' in d.keys()]
        return max(ids) if ids!=[] else 0
    
    
    def connect(self):
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')
        ## Prediction part, we compute 7 values of acceleration to compute rolling std then
        self.values_for_tab_acc = pd.DataFrame({'X_acc' : 0, 'Y_acc' : 0, 'Z_acc' : 0}, index = range(7))
        self.values_for_tab_ori = pd.DataFrame({'diff_Roll' : 0, 'diff_Pitch' : 0, 'diff_Yaw' : 0}, index = range(7))
        self.wide_tab = np.zeros(42)
             
        self.data_acc = np.zeros(3)

        self.data_bygone_gyr = np.zeros(3)
        self.data_current_gyr = np.zeros(3)
        self.data_diff_gyr = self.data_current_gyr - self.data_bygone_gyr

        self.pred_acc = Queue([0 for i in range(7)])
        self.pred_gyr = Queue([0 for i in range(7)])
  
        self.ip_address = self.LineEditIP.text()
        self.port = 0
        try:
                self.dev.connect(self.ip_address) ## Depend on your device
        except Exception as err:
            pywpc.printGenericError(err)
            ErrorMsgBox = QMessageBox()
            ErrorMsgBox.setIcon(QMessageBox.Information)
            ErrorMsgBox.setText("Error: " + str(err))
            ErrorMsgBox.setWindowTitle("Error")
            ErrorMsgBox.setStandardButtons(QMessageBox.Ok)

            ## Show the messagebox
            ErrorMsgBox.exec_()
            return
        self.dev.AHRS_open(self.port, self.timeout)
        self.dev.AHRS_start(self.port, self.timeout)
        self.connection_started = True
    
    
    ## there is two function to add data:
    ## add_measure is to add a set of labelled data
    ## add_row is to add a row of data to the temprary list of same label data
    def add_measure(self, data: list, sampling_time: float = 50):
        
        ## we append the value of the last measure if it exists, 
        ## this method is used to easily suppress last measure if needed (cf. supress_last_measure method)        
        self.sampling_time = sampling_time
        
        ##to avoid error if type is not correct
        
        self.GraphicsViewRot.clear()
        self.GraphicsViewRot.addLegend()
        
        self.GraphicsViewAcc.clear()
        self.GraphicsViewAcc.addLegend()
        
        ##plot the curves for the orientation and acceleration
        self.curve_roll = self.GraphicsViewRot.plot(pen = {'color' : '#8CB9BD', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#8CB9BD',name = 'Roll')
        self.curve_pitch = self.GraphicsViewRot.plot(pen = {'color' : '#ECB159', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#ECB159',name = 'Pitch')
        self.curve_yaw = self.GraphicsViewRot.plot(pen = {'color' : '#B67352', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#B67352',name = 'Yaw')
        
        self.curve_x_acc = self.GraphicsViewAcc.plot(pen = {'color' : '#a70f34', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#a70f34',name = 'X_acc')
        self.curve_y_acc = self.GraphicsViewAcc.plot(pen = {'color' : '#3d90be', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#3d90be',name = 'Y_acc')
        self.curve_z_acc = self.GraphicsViewAcc.plot(pen = {'color' : '#7c6ca4', 'width' : 3}, symbol = 'o', symbolPen = 'w', symbolBrush = '#7c6ca4',name = 'Z_acc')
        
        self.time = [0]
        
        self.yaw = [0]
        self.roll = [0]
        self.pitch = [0]
        self.x_acc = [0]
        self.y_acc = [0]
        self.z_acc = [0]
        ## each time the timer reach a sampling time, we add a row to the data list and we plot the new data
        self.timer = QtCore.QTimer()
        self.timer.setInterval(sampling_time)
        self.timer.timeout.connect(lambda: self.add_row(data, sampling_time))
        self.timer.start()
        self.timer_running = True

    def stop_timer(self):
        self.timer.stop() 
    
    def get_type(self, list):
        unique, counts = np.unique(list, return_counts=True)
        return(unique[np.argmax(counts)])
        
        
    def add_row(self, data: list, sampling_time: float = 50):
        if self.time is None:
            self.time = [0]
        if self.roll is None:
            self.roll = [0]
        if self.pitch is None:
            self.pitch = [0]
        if self.yaw is None:
            self.yaw = [0]
        if self.x_acc is None:
            self.x_acc = [0]
        if self.y_acc is None:
            self.y_acc = [0]
        if self.z_acc is None:
            self.z_acc = [0]

        start_time = 1000*time.time()
        mode = 3 ## 0: Orientation, 1: Acceleration, 3: Orientation + Acceleration
        
        self.AHRS_list = np.array(self.dev.AHRS_getEstimate(self.port, mode, self.read_delay))
        self.data_bygone_gyr = self.data_current_gyr
        self.data_current_gyr = np.array(self.AHRS_list[:3])
        self.data_diff_gyr = self.data_current_gyr - self.data_bygone_gyr

        self.data_acc = self.AHRS_list[3:] - 9.81*np.array([np.sin(DEG_TO_RAD*self.data_current_gyr[1]),
                                                np.sin(DEG_TO_RAD*self.data_current_gyr[0])*np.cos(DEG_TO_RAD*self.data_current_gyr[1]), 
                                                np.cos(DEG_TO_RAD*self.data_current_gyr[0])*np.cos(DEG_TO_RAD*self.data_current_gyr[1])]) 

        self.new_row = {'Roll': self.AHRS_list[0], 
                        'Pitch': self.AHRS_list[1], 'Yaw': self.AHRS_list[2], 
                        'X_acc': self.AHRS_list[3] - 9.81 * np.sin(DEG_TO_RAD * self.AHRS_list[1]),
                        'Y_acc': self.AHRS_list[4] - 9.81  * np.sin(DEG_TO_RAD * self.AHRS_list[0]) * np.cos(DEG_TO_RAD * self.AHRS_list[1]), 
                        'Z_acc': self.AHRS_list[5] - 9.81 * np.cos(DEG_TO_RAD * self.AHRS_list[0]) * np.cos(DEG_TO_RAD * self.AHRS_list[1]) ,
                        'Interval Time': sampling_time, 'Time': datetime.datetime.now()}
        if len(self.time) < 20:
            self.time.append(self.time[-1] + sampling_time)
            self.roll.append(self.new_row['Roll'])
            self.pitch.append(self.new_row['Pitch'])
            self.yaw.append(self.new_row['Yaw'])
            self.x_acc.append(self.new_row['X_acc'])
            self.y_acc.append(self.new_row['Y_acc'])
            self.z_acc.append(self.new_row['Z_acc'])
        else:
            self.time = self.time[1:] +[self.time[-1] + sampling_time]
            self.roll = self.roll[1:] + [self.new_row['Roll']]
            self.pitch = self.pitch[1:] + [self.new_row['Pitch']]
            self.yaw = self.yaw[1:] + [self.new_row['Yaw']]
            self.x_acc = self.x_acc[1:] + [self.new_row['X_acc']]
            self.y_acc = self.y_acc[1:] + [self.new_row['Y_acc']]
            self.z_acc = self.z_acc[1:] + [self.new_row['Z_acc']]


        self.wide_tab = np.concatenate((self.data_acc, self.data_diff_gyr, self.wide_tab[:-6]))

        if TYPE == "AI":
            pred_acc = MODEL_ACC([self.wide_tab])
        else:
            pred_acc = MODEL_ACC(self.wide_tab)
        self.pred_acc.add(pred_acc)
        pred_acc = self.get_type(self.pred_acc.list)
        self.LineEditTypeAcc.setText(f"{map_acc[pred_acc]}")

        if TYPE == "AI":
            pred_ori = MODEL_GYR([self.wide_tab])
        else:
            pred_ori = MODEL_GYR(self.wide_tab)
        print(pred_ori)
        self.pred_gyr.add(pred_ori)
        pred_ori = self.get_type(self.pred_gyr.list)
        self.LineEditTypeOri.setText(f"{map_gyr[pred_ori]}")
        
        
        
        
        self.curve_roll.setData(self.time, self.roll)
        self.curve_pitch.setData(self.time, self.pitch)
        self.curve_yaw.setData(self.time, self.yaw)
        self.curve_x_acc.setData(self.time, self.x_acc)
        self.curve_y_acc.setData(self.time, self.y_acc)
        self.curve_z_acc.setData(self.time, self.z_acc)
        
        end_time = 1000*time.time()
        print(f"Time to add row: {end_time - start_time} ms")
        
        
    def quit(self, MainWindow = None):
        
        if not self.connection_started:
            print("No action intended, nothing happened in this session")
            MainWindow.close()
            return
        
        self.timer.stop()
        self.dev.AHRS_stop(self.port, self.timeout)
        print(f"AHRS_close in port {self.port}")
        self.dev.disconnect()
        MainWindow.close()
        self.dev.close()
            
            
def main(): 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    if dialog.exec_() == QDialog.Accepted:
        global IPSENSOR, SAMPLINGTIME
        IPSENSOR, SAMPLINGTIME = dialog.get_parameters()
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()