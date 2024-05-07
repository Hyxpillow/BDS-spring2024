import pandas as pd
from sklearn.decomposition import PCA
import numpy as np


def reduction(df: pd.DataFrame):
    tmp = df['profitable']
    df = df.drop(['profitable'], axis=1)
    # Firstly, do the following and get all eigenvalues
    # pca = PCA()
    # pca.fit(raw_df)

    # pick PC1 ~ PC12
    pca = PCA(n_components=5)
    pca.fit(df)

    df = pd.DataFrame(pca.transform(df))
    df['profitable'] = tmp
    return df