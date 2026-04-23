# ✈️ Commercial Flight Delay Prediction: Optimizing Recall with Deep Learning

## 📖 About the Project
This Data Science project aims to predict commercial flight delays at the exact moment the aircraft doors close (**Gate-Level Prediction**). 

In civil aviation, the cost of a **False Negative** (failing to predict an actual delay) is extremely high, leading to missed connections and severe logistical costs. The core focus of this project was not just building a predictive model, but aligning Artificial Intelligence with business pain points by optimizing the decision threshold to maximize the capture of actual delays before takeoff.

## ⚙️ Data Engineering (ETL Pipeline)
Working with millions of aviation records in raw CSV format can easily exhaust RAM in cloud environments like Google Colab. 

To solve this, we built a local ETL script (`preparar_dataset.py`) that handles the ingestion of multiple CSV files, concatenates them into a single dataframe, and exports the data to a highly optimized columnar format (`.parquet`). This reduced file size and drastically improved reading speeds for the Deep Learning pipeline.

## 🎯 Key Challenges & Solutions (Highlights)

1. **Mitigating Data Leakage:**
   * **The Problem:** Applying transformations (like `MinMaxScaler` and `Target Encoding`) on the entire dataset before splitting caused test distributions to leak into the model's training phase.
   * **The Solution:** We implemented a strict *Train-Test Split* first. Airport encoding metrics and scaling boundaries were learned strictly on the training data, ensuring a 100% honest evaluation in production.

2. **Handling Class Imbalance (18% Delayed vs 82% On-Time):**
   * **The Solution:** Instead of using SMOTE (which demands high computational costs by generating millions of synthetic rows), we utilized Keras' `class_weight` hyperparameter to heavily penalize the neural network when misclassifying the minority class. The primary evaluation metric was shifted from ROC AUC to **PR AUC (Precision-Recall Curve)**.

3. **Decision Threshold Optimization:**
   * **The Result:** By shifting the probabilistic cutoff from the default `0.50` down to `0.35`, the model became strategically more sensitive to delays. We achieved a **Recall of 84%**, successfully capturing nearly 90,000 delayed flights before takeoff. We accepted a controlled drop in precision to prioritize logistical safety over false alarms.

## 🛠️ Technology Stack & Architecture

* **Language & Data Manipulation:** Python, Pandas (Parquet engine), NumPy.
* **Machine Learning Pipeline:** Scikit-Learn (`MinMaxScaler`, `train_test_split`, `compute_class_weight`, evaluation metrics).
* **Deep Learning:** TensorFlow / Keras.
  * *Architecture:* Shallow MLP (Dense Layers: 64 -> 32 -> 1).
  * *Optimizer & Metric:* Adam and direct Recall tracking.
  * *Regularization:* Early Stopping monitoring validation loss (`val_loss`) with best weights restoration.
* **Data Visualization:** Matplotlib and Seaborn.

## 📊 Final Performance (Threshold 0.35)
* **Recall (Class 1 - Delays):** 0.84
* **Precision (Class 1 - Delays):** 0.64
* **PR AUC:** 0.868

*(For Confusion Matrices and Learning Curves, please refer to the Jupyter Notebook in this repository).*

## 🚀 How to Run
1. Clone this repository: `git clone https://github.com/[your-username]/[repo-name].git`
2. Install the requirements: `pip install pandas pyarrow scikit-learn tensorflow matplotlib seaborn`
3. Run the ETL pipeline to consolidate the raw data (place your CSVs in the root folder): 
   ```bash
   python preparing_dataset.py
