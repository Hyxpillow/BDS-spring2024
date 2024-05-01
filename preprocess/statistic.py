
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def statistic(df: pd.DataFrame):
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    for profitable in df["profitable"]:
        if profitable == 1:
            x1.append("profitable")
        else:
            x2.append("profitable")
    for year in df["year"]:
        if year == 2023:
            x1.append("year")
        elif year == 2022:
            x2.append("year")
        elif year == 2021:
            x3.append("year")
        elif year == 2020:
            x4.append("year")
    x = [x1, x2, x3, x4]

    # Histogram
    # fig, ax = plt.subplots()
    counts, bins, _ = plt.hist(x, histtype = "barstacked")
    # for count, bin in zip(counts, bins):
    #     plt.text(bin, count, str(int(count)), ha='center', va='bottom')
    plt.savefig('./figures/dataset.pdf', format="pdf")
    plt.clf()
