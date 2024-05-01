from bayes import do_naive_bayes
from knn import do_knn
from decision_tree import do_decision_tree
from random_forest import do_random_forest

do_naive_bayes("./datasets/clean.csv")
do_naive_bayes("./datasets/clean_binning.csv")
do_naive_bayes("./datasets/clean_reduction.csv")

do_knn("./datasets/clean.csv")
do_knn("./datasets/clean_binning.csv")
do_knn("./datasets/clean_reduction.csv")

do_decision_tree("./datasets/clean.csv")
do_decision_tree("./datasets/clean_binning.csv")
do_decision_tree("./datasets/clean_reduction.csv")

do_random_forest("./datasets/clean.csv")
do_random_forest("./datasets/clean_binning.csv")
do_random_forest("./datasets/clean_reduction.csv")