import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import itertools
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import _tree
from sklearn.preprocessing import LabelEncoder

plt.style.use('fivethirtyeight')

newData = pd.read_csv('datasets_575188_1041634_modified_COVID19_open_line_list.csv')
newData["symptom"] = None

newData.loc[newData['outcome'] == 1, ['symptom']] = "Negatif Covid mild"
newData.loc[newData.outcome == 0, ['symptom']] = "Negatif Covid"
newData.loc[newData.outcome == 2, ['symptom']] = "Positif Covid moder"
newData.loc[newData.outcome == 3, ['symptom']] = "Positif Covid sever"

training_dataset = newData[['age', 'gender', 'onset_symptoms_to_admission_hospital',
                            'admission_hospital_to_confirmation', 'fever', 'caugh', 'chills',
                            'nausea', 'dyspnea', 'anorexia', 'pneumonitis', 'rhinorrhea',
                            'diarrhea', 'fatigue', 'sore muscle', 'sore throat',
                            'respiratory symptoms', 'headache', 'weakness', 'dizziness',
                            'pleural effusion', ' chest pain', 'symptom']]

corr_matrix = training_dataset.corr()
cor_target = abs(corr_matrix)
# Selecting highly correlated features
relevant_features = cor_target[cor_target > 0.4]

training_data = training_dataset.iloc[:, :-1]
corr = training_data.corr()

columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i + 1, corr.shape[0]):
        if corr.iloc[i, j] >= 0.8:
            if columns[j]:
                columns[j] = False
selected_columns = training_data.columns[columns]
training_data = training_data[selected_columns]

data = training_data

selected_columns = selected_columns[1:].values


def backwardElimination(x, Y, sl, columns):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(Y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
                    columns = np.delete(columns, j)

    regressor_OLS.summary()
    return x, columns


SL = 0.05
data_modeled, selected_columns = backwardElimination(data.iloc[:, 1:].values,
                                                     data.iloc[:, 0].values, SL, selected_columns)

result = pd.DataFrame()
result['diagnosis'] = data.iloc[:, 0]

data = pd.DataFrame(data=data_modeled, columns=selected_columns)

# Dimensionality Reduction for removing redundancies
dimensionality_reduction = training_dataset.groupby(training_dataset['symptom']).max()

# Slicing and Dicing the dataset to separate features from predictions
X = training_dataset.iloc[:, 0:21].values
y = training_dataset.iloc[:, -1].values

# Encoding String values to integer constants
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

# Splitting the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Saving the information of columns
cols = training_dataset.columns
cols = cols[:-1]


def chatbot():
    print("Reponsez yes/Yes or no/No pour les symptomes")

    def print_disease(node):
        # print(node)
        node = node[0]
        # print(len(node))
        val = node.nonzero()
        # print(val)
        disease = labelencoder.inverse_transform(val[0])
        return disease

    def tree_to_code(tree, feature_names):
        tree_ = tree.tree_
        # print(tree_)
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]
        # print("def tree({}):".format(", ".join(feature_names)))
        symptoms_present = []

        def recurse(node, depth):
            indent = "  " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                print(name + " ?")
                ans = input()
                ans = ans.lower()
                if ans == 'yes':
                    val = 1
                else:
                    val = 0
                if val <= threshold:
                    recurse(tree_.children_left[node], depth + 1)
                else:
                    symptoms_present.append(name)
                    recurse(tree_.children_right[node], depth + 1)
            else:
                present_disease = print_disease(tree_.value[node])
                print("D'après les symptomes vous avez " + present_disease)
                red_cols = dimensionality_reduction.columns
                symptoms_given = red_cols[dimensionality_reduction.loc[present_disease].values[0].nonzero()]
                print("symptoms present  " + str(list(symptoms_present)))
                print("symptoms given " + str(list(symptoms_given)))
                confidence_level = (1.0 * len(symptoms_present)) / len(symptoms_given)
                print("indice de confiance " + str(confidence_level))

        recurse(0, 1)

    tree_to_code(classifier, cols)


chatbot()
