The folder "Analyis" gather the files that can be used to train new models. Two kind of files are 
actualy useful if you want to train models easely : Acc_analysis.ipynb and 
Gyr_analysis.ipynb, some others files that where used for the conception of the models are
log in the sub-folder "archives", there is an other text file that quiclky described these files.

How to train with new data : 

-If you don't want to modify the model (i.e. train on a simple decision tree), you just have to add
the data on the "Data Processing" part. 
Let's says your datas come from the csv file "data.csv" in the folder data_sensor, this is done by adding :

alldata = pd.read_csv('data_sensor/data.csv')

You also have to add alldata in the list Ldata

Please, check that your data are balanced, and if if you want to add neutral data (data with no movement), 
ensure the number of neutral data is similar to the number of the others data.