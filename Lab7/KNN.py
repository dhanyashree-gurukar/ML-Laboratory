import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

def manhattan_distance(x1, x2):
    distance = np.sum(np.abs(x1-x2))
    return distance

class KNN:
    def __init__(self, k, distance_fn):
        self.k = k
        self.distance_fn = distance_fn

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self, x):
        distances = [self.distance_fn(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]
    
def glass():
    df = pd.read_csv("glass.csv")
    y = df['Type'].values
    X = df.drop('Type', axis=1).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    clf_euclidean = KNN(k=3, distance_fn=euclidean_distance)
    clf_euclidean.fit(X_train, y_train)

    predictions_euclidean = clf_euclidean.predict(X_test)

    accuracy_euclidean = np.sum(predictions_euclidean == y_test) / len(y_test)
    print("Glass:")
    print("Accuracy with euclidean distance: ", accuracy_euclidean)

    clf_manhattan = KNN(k=3, distance_fn=manhattan_distance)

    clf_manhattan.fit(X_train, y_train)
    predictions_manhattan = clf_manhattan.predict(X_test)
    accuracy_manhattan = np.sum(predictions_manhattan == y_test) / len(y_test)

    print("Accuracy with manhattan distance: ", accuracy_manhattan)

def fruits():
    df = pd.read_csv("fruits.csv")

    y = df['fruit_label'].values
    X = df[['mass', 'width', 'height', 'color_score']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

    clf_euclidean_custom = KNN(k=5, distance_fn=euclidean_distance)
    clf_euclidean_custom.fit(X_train, y_train)
    predictions_euclidean_custom = clf_euclidean_custom.predict(X_test)

    accuracy_euclidean_custom = np.sum(predictions_euclidean_custom == y_test) / len(y_test)
    print("\nFruits:")
    print("Accuracy with euclidean distance: ", accuracy_euclidean_custom)

    clf_manhattan_custom = KNN(k=5, distance_fn=manhattan_distance)
    clf_manhattan_custom.fit(X_train, y_train)
    predictions_manhattan_custom = clf_manhattan_custom.predict(X_test)

    accuracy_manhattan_custom = np.sum(predictions_manhattan_custom == y_test) / len(y_test)
    print("Accuracy distance with manhattan distance: ", accuracy_manhattan_custom)

glass()
fruits()