from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def do_decision_tree(data_path):
    raw_df = pd.read_csv(data_path)
    X = raw_df.drop(['profitable'], axis=1)
    y = raw_df['profitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=False)
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, y_train)
    train_acc = decision_tree.score(X_train, y_train)
    test_acc = decision_tree.score(X_test, y_test)
    print("Decision Tree", data_path)
    print("Train acc:", train_acc)
    print("Test  acc:", test_acc)
    
    # importances = decision_tree.feature_importances_
    # indices = np.argsort(importances)
    # fig, ax = plt.subplots()
    # ax.barh(range(len(importances)), importances[indices])
    # ax.set_yticks(range(len(importances)))
    # ytick = ["PC"+str(tick) for tick in np.array(X_train.columns)[indices]]
    # ax.set_yticklabels(ytick)
    # plt.title("Decision Tree Feature importances")
    # plt.show()

do_decision_tree("./datasets/clean.csv")
do_decision_tree("./datasets/clean_binning.csv")
do_decision_tree("./datasets/clean_reduction.csv")