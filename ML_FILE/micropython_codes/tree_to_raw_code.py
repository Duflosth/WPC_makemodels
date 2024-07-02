import pickle


from sklearn.tree import _tree
import numpy as np

pkl_name = 'WPC_test_acceleration'
micropython_name = 'newmodel_micropython'

def tree_to_code(tree, feature_names, pkl_name):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    code_list = []
    code_list.append(f"def {pkl_name}_tree(x):")
    def recurse(node, depth):
        indent = "  " * (depth)
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            code_list.append(f"{indent}if x[{name}] <= {np.round(threshold, 2)}:")
            recurse(tree_.children_left[node], depth + 1)
            code_list.append(f"{indent}else:  # if x[{name}] > {np.round(threshold, 2)}")
            recurse(tree_.children_right[node], depth + 1)
        else:
            code_list.append(f"{indent}return {np.argmax(tree_.value[node])}")

    recurse(0, 1)
    return '\n'.join(code_list)

# Exemple d'utilisation :
from sklearn.tree import DecisionTreeClassifier

#Set pkl_name as the name of the file you want to 
with open(f"classifiers/{pkl_name}.pkl", 'rb') as f:
    model_ori = pickle.load(f)

# Convertir le modèle en code brut
raw_code = tree_to_code(model_ori, [i for i in range(42)], pkl_name)

# Write the raw code in a separate file
with open(f'micropython_codes/ESP32/temporary_models/{micropython_name}.py', 'w') as file:
    file.write(raw_code)