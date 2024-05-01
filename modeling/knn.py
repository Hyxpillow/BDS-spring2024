import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class KNNClassifier():
    def __init__(self, K=5) -> None:
        self.K = K
        self.feature_matrix = None
        self.label_vector = None
    def fit(self, features, labels):
        self.feature_matrix = features
        self.label_vector = labels
    def score(self, feature_matrix, label_vector):
        assert feature_matrix.shape[0] == label_vector.shape[0]
        input_size = feature_matrix.shape[0]
        hit = 0
        for i in range(input_size):
            features = feature_matrix.iloc[i]
            # Calculate the distance between current input and observations in train data.
            distance_list = 0
            for col in self.feature_matrix.columns:
                distance_list += (self.feature_matrix[col] - features[col]) ** 2
            distance_list = np.sqrt(distance_list)
            # Select K nearest observations and predict.
            k_nearest_idx = distance_list.nsmallest(n=self.K).index
            prediction = self.label_vector[k_nearest_idx].mode()[0]
            # Compare our prediction with actual label
            label = label_vector.iloc[i]
            if prediction == label:
                hit += 1 
        return hit / input_size

def do_knn(data_path):
    raw_df = pd.read_csv(data_path)
    X = raw_df.drop(['profitable'], axis=1)
    y = raw_df['profitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=False)
    knn = KNNClassifier()
    knn.fit(X_train, y_train)
    train_acc = knn.score(X_train, y_train)
    test_acc = knn.score(X_test, y_test)
    print("KNN", data_path)
    print("Train acc:", train_acc)
    print("Test  acc:", test_acc)
