import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def str_column_to_int(dataset, column):
    class_values = dataset[column].values
    unique = set(class_values)
    lookup = dict()
    result = list()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset[column].values:
        result.append(lookup[row])
    dataset[column] = result
    return dataset.astype(float)
    
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if predicted[i] == actual[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0, (actual, predicted)
 
def evaluate_algorithm(algorithm, num_neighbors, X_train, X_test, y_train, y_test):
    scores = list()
    predicted = algorithm(X_train, X_test, num_neighbors, y_train)
    actual = y_test
    accuracy, parans = accuracy_metric(actual, predicted)
    scores.append(accuracy)
    return scores, parans
 
def get_neighbors(X_train, test_row, num_neighbors):
    distances = list()
    distances = np.linalg.norm(X_train - test_row, axis=1)
    neighbors = distances.argsort()[:num_neighbors]
    return neighbors
 
def predict_classification(X_train, test_row, num_neighbors,y_train):
    neighbors = get_neighbors(X_train, test_row, num_neighbors)
    output_values = y_train[neighbors]
    prediction = output_values.mean().round()
    return prediction
 
def k_nearest_neighbors(X_train, test, num_neighbors, y_train):
    predictions = list()
    for row in test:
        output = predict_classification(X_train, row, num_neighbors, y_train)
        predictions.append(output)
    return(predictions)

def knn(filename):
    dataset = pd.read_csv(filename, header=None)
    dataset.columns = ["Index","Gender","Height","Weight"]
    str_column_to_int(dataset, dataset.columns[1])
    X = dataset.drop("Index", axis=1)
    X = X.values
    y = dataset["Index"]
    y = y.values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)
    num_neighbors = 4
    scores, parans = evaluate_algorithm(k_nearest_neighbors, num_neighbors, X_train, X_test, y_train, y_test)
    print(scores[0])
    ConfusionMatrixDisplay.from_predictions(parans[0], parans[1])
    plt.show()
filename = 'AB2/KNN/bmi.csv'
knn(filename)

# biggerMean = 0
# bestValue = 2
# for num_neighbors in range(2,21):
#     scores = evaluate_algorithm(k_nearest_neighbors, num_neighbors, X_train, X_test, y_train, y_test)
#     mean = sum(scores)/float(len(scores))
#     if mean > biggerMean:
#         biggerMean = mean
#         bestValue = num_neighbors
# print(bestValue)
# print(biggerMean)
