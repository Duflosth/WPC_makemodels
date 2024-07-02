This README File will only explains the content of the code of the following files : 
"WPC_Generator.py", "WPC_live_pred_micropython.py", and "WPC_live_pred".

There is other README fils in the subfolders of ML_FILE to explains how other files work.

                                    ----WPC Generator----
WPC_Generator is used to create data sets. There is a first dialog box where you can choose several
parameters that you would like to modify. 
Theses parameters are : 
-The IP adress of the DAQ
-The name of the csv file that you want to create
-The sampling time (I recommand to let it to 50 ms, but you can modify it if you want to try new things)
-The measured period (1000 m by default), it's the time you want to measure a set of samples.
- A checkbox "new file". If it is not activated, and you put the name of a file that already exists, it will append the new datas after the data of the csv file. If you click on new file, it wille EREASE all the data of the new csv file and then add the data you registered.

-Then, an other window is displayed, you can see the parameters you've put and some new buttons as "Roll", "Pitch", "Yaw", "X_acc", "Y_acc", "Z_acc". Let says you want to log a "Roll" movement, you just have to click on the "Roll" button and does the movement of a Roll movement. It is the same process for all the movements.
If you made error on the movement, you can click on the button "Delete last measure" and it will delete the last measured data. The disappearance of the curves means that the removal of the last measurement has been successful.

-Once you have finished to classify, click on save and quick. If you just click on the red cross, the data will not be saved. 
Clicking on the 'red cross' is also a good way to exit the display without registering anything.







                                    ----WPC live pred micropytthon----

If you want to train a new model with the analysis files, it will log two files : one .pkl file 
that save the SKlearn modeln and one .py file that save a model that can be directly copy-paste 
in micropython. This file "WPC live pred micropython" will allow you to verify this model in live. 
You just have to put the right IP in the first dialog post, and after you will be able to see the 
prediction of the models you put in the code in real time. You just have to click on quit then 
to quit the interface. 
When you save a new model, the output will be among {1, 2, 3, 4} instead of
{X_acc, Y_acc, Z_acc, No movement} or {Roll, Pitch, Yaw, No acceleration}. 
It is why there is the utilisation of dictionary to associate the numbers to the name of the movement.
If you create a new model, please verify the association of the numbers with the names is
still correct, or change it to make it correct. 


                                    ----WPC live pred ----

Approximatly the same file than "WPC live pred micropython" but it uses the pkl file instead of the 
micropython files. I recommand prioritizing the use of the "WPC live pred micropython" file 
over of this one.
