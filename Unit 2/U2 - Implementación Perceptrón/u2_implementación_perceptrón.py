# -*- coding: utf-8 -*-
"""U2 - Implementación Perceptrón.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dI3SxFpDNSL2bCgYuOL_xbBtjOlMAmUL

#codigo en celdas diferentes
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Definir la función de activación (función escalón)
def activation_function(x):
    return 1 if x >= 0 else 0

# Definir el perceptrón
class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                y_pred = self.predict(X[i])
                update = self.learning_rate * (y[i] - y_pred)
                self.weights += update * X[i]
                self.bias += update

    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        return activation_function(linear_output)

# Cargar el conjunto de datos de cáncer de mama
data = load_breast_cancer()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el perceptrón
perceptron = Perceptron(learning_rate=0.01, n_iterations=1000)
perceptron.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = [perceptron.predict(x) for x in X_test]

# Calcular la precisión del perceptrón
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del perceptrón: {:.2f}%".format(accuracy * 100))

"""#codigo en una misma celda"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Definir la función de activación (función escalón)
def activation_function(x):
    return 1 if x >= 0 else 0

# Definir el perceptrón
class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                y_pred = self.predict(X[i])
                update = self.learning_rate * (y[i] - y_pred)
                self.weights += update * X[i]
                self.bias += update

    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        return activation_function(linear_output)

# Cargar el conjunto de datos de cáncer de mama
data = load_breast_cancer()
X, y = data.data, data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el perceptrón
perceptron = Perceptron(learning_rate=0.01, n_iterations=1000)
perceptron.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = [perceptron.predict(x) for x in X_test]

# Calcular la precisión del perceptrón
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del perceptrón: {:.2f}%".format(accuracy * 100))