import sys
import warnings
import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Perceptron

sys.path.append('../utils')
from car_detect_datareader import split_data


X_train, X_test, X_val, y_train, y_test, y_val = split_data()


x_train = []
x_test = []

for img in X_train:
    x_train.append(img.flatten())

for img in X_test:
    x_test.append(img.flatten())

X_train = np.array(X_train)
X_mean = X_train.mean()
X_std = X_train.std()

x_train = (x_train - X_mean) / X_std
x_test = (x_test - X_mean) / X_std

# gs_perceptron = GridSearchCV(
#                estimator=SVC(),
#                param_grid=[
#                    {'kernel': ['linear', 'rbf', 'poly', 'sigmoid', 'precomputed'],
#                    'degree': [3, 4, 5, 6],
#                    'max_iter': [-1, 1000, 10000, 100000, 100, 10],
#                    'tol': [1e-3, 1e-4, 1e-2, 1e-1],
#                    }], cv=5)


gs_perceptron = GridSearchCV(
                estimator=Perceptron(),
                param_grid=[
                {'max_iter': [10, 5]}], cv=8)

lr = GridSearchCV(
      estimator=LogisticRegression(),
      param_grid=[
      {'penalty': ['l1', 'l2', 'elasticnet'],
      'max_iter': [10, 5],
      'C': [1.0, 0.8, 0.5, .1]}], cv=8)

gs_perceptron.fit(x_train, y_train)
print(gs_perceptron.best_score_)
print(gs_perceptron.best_params_)
print(gs_perceptron.score(x_test, y_test))

lr.fit(x_train, y_train)
print(lr.best_score_)
print(lr.best_params_)
print(lr.score(x_test, y_test))
