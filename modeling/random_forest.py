from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def do_random_forest(data_path):
    raw_df = pd.read_csv(data_path)
    X = raw_df.drop(['profitable'], axis=1)
    y = raw_df['profitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=False)
    random_forest = RandomForestClassifier()
    random_forest.fit(X_train, y_train)
    train_acc = random_forest.score(X_train, y_train)
    test_acc = random_forest.score(X_test, y_test)
    print("Random Forest", data_path)
    print("Train acc:", train_acc)
    print("Test  acc:", test_acc)
    
    # importances = random_forest.feature_importances_
    # indices = np.argsort(importances)
    # fig, ax = plt.subplots()
    # ax.barh(range(len(importances)), importances[indices])
    # ax.set_yticks(range(len(importances)))
    # ytick = ["PC"+str(tick) for tick in np.array(X_train.columns)[indices]]
    # ax.set_yticklabels(ytick)
    # plt.title("Random Forest Feature importances")
    # plt.show()

do_random_forest("./datasets/clean.csv")
do_random_forest("./datasets/clean_binning.csv")
do_random_forest("./datasets/clean_reduction.csv")