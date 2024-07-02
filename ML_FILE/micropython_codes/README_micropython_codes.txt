This is the readme file used to understand the code that are inside the ESP32:
-All the code that are in the DAQ is also in the ESP32 file
- The code main_micropython.py is the main code from the DAQ file. It consist to take one model and to
run it on the ESP32. 
You can choose a model on the beginning of the code in MODEL = ...
You must after choose the TYPE of the model among "AI" or "TREE". Indeed, the type of input is not the 
same for those two models (either a List, or either a List of List). Choose the right type will allow 
the algorithm to use the good input then for the model.

-When you want to create an algorithm with the analysis' files, it will log the micropython models in 
"temporary_models". You can then choose to move the models in the file "models".

-To use the AI models, you have to copy paste the weights in the files "hyper:_params_acc.txt" and
"hyper_params_gyr.txt". The weights are in a list of array, in the following order w1, b1, w2, b2.
