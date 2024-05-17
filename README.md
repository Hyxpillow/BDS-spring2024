
# CSCI-GA 3033 Big Data Science Final Project

## Team Members

- Sophia Shan
- Yuxiang Huang
- Yuheng Lu

## Project Overview

Our project is divided into two main components: the Movie Profitability Prediction and the Movie Recommender System. Each part utilizes distinct datasets and employs various models and algorithms to achieve its objectives.

### Movie Revenue Prediction

**Pre-requisites:**
The initial dataset required for this component is pre-downloaded. You can find it at `./download/raw.csv`.

**Steps to run:**

1. Since the raw data is already downloaded, you can skip directly to preprocessing.
2. Execute the preprocessing script:
   ```bash
   python3 ./preprocess/main.py
   ```
3. After preprocessing, the outputs (figures and processed datasets) are available in `./figures/` and `./datasets/`.
4. Open and run the `best_performance.ipynb` notebook located in the notebook folder to access the our best features and performance measures.

### Movie Recommender System

**Dataset Setup:**

1. Refer to the `README.md` in the `datasets/movie_lens` folder for instructions on how to download the necessary dataset.

**Execution Instructions:**

1. Open and run the `movie_recommendation.ipynb` notebook located in the notebook folder.
2. The notebook guides you through data preprocessing, exploration, model training, evaluation, and finally, deploying the recommendation system.
