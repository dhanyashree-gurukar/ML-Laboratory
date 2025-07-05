import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split

class NaiveBayesClassifier:
    def __init__(self):
        self.prior = {}
        self.conditional = {}

    def fit(self, X, y):
        self.classes = np.unique(y)
        for c in self.classes:
            self.prior[c] = np.mean(y==c)

        for feature in X.columns:
            self.conditional[feature] = {}
            for c in self.classes:
                feature_values = X[feature][y==c]
                self.conditional[feature][c] ={'mean':np.mean(feature_values), 'std':np.std(feature_values)}

    def predict(self, X):
        y_pred = []
        for _ , sample in X.iterrows():
            probabilities = {}
            for c in self.classes:
                probabilities[c] = self.prior[c]
                for feature in X.columns:
                    mean = self.conditional[feature][c]['mean']
                    std = self.conditional[feature][c]['std']
                    x = sample[feature]
                    probabilities[c] *= self._gaussian_pdf(x, mean, std)
            y_pred.append(max(probabilities, key = probabilities.get))
        return y_pred

    def _gaussian_pdf(self, x, mean, std):
        exponent = np.exp(-((x-mean)**2)/(2*std**2))
        return (1/(np.sqrt(2*np.pi)*std)) * exponent 
    
def iris():
    iris = pd.read_csv(r"Iris.csv")
    iris.head()

    X = iris.iloc[:, :-1]
    y = iris.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    classifier = NaiveBayesClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print("Accuracy is: ", accuracy_score(y_test, y_pred))

def titanic():
    df = pd.read_csv("TitanicDataset.csv")
    df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    df['Embarked'] = df['Embarked'].map({'C':0, 'Q':1, 'S':2})
    train, test = train_test_split(df, test_size=0.2)

    X_train = train.drop('Survived', axis=1)
    y_train = train['Survived']
    X_test = test.drop('Survived', axis=1)
    y_test = test['Survived']

    classifier = NaiveBayesClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    print("\n\nConfusion matrix:\n", cm)
    accuracy = np.mean(y_pred == y_test)
    print("Accuracy: ", accuracy)

iris()
titanic()


#OUTPUT:
'''
                 precision    recall  f1-score   support

    Iris-setosa       1.00      1.00      1.00        11
Iris-versicolor       1.00      1.00      1.00        13
 Iris-virginica       1.00      1.00      1.00         6

       accuracy                           1.00        30
      macro avg       1.00      1.00      1.00        30
   weighted avg       1.00      1.00      1.00        30

[[11  0  0]
 [ 0 13  0]
 [ 0  0  6]]
Accuracy is:  1.0


Confusion matrix:
 [[95 18]
 [39 27]]
Accuracy:  0.6815642458100558
'''