import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def do_naive_bayes(data_path):
    raw_df = pd.read_csv(data_path)
    X = raw_df.drop(['profitable'], axis=1)
    y = raw_df['profitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=False)
    naive_bayes = GaussianNB()
    naive_bayes.fit(X_train, y_train)
    train_acc = naive_bayes.score(X_train, y_train)
    test_acc = naive_bayes.score(X_test, y_test)
    print("Naive Bayes", data_path)
    print("Train acc:", train_acc)
    print("Test  acc:", test_acc)

do_naive_bayes("./datasets/clean.csv")
do_naive_bayes("./datasets/clean_binning.csv")
do_naive_bayes("./datasets/clean_reduction.csv")
