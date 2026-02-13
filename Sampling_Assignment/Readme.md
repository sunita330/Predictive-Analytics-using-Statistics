
# Assignment – Sampling Techniques on Imbalanced Dataset

## 📌 Objective
The objective of this assignment is to analyze how different sampling techniques affect the performance of machine learning models on a highly imbalanced credit card fraud dataset.

---

## 📂 Dataset
Dataset used: Credit Card Fraud Detection  
Source:  
https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv

The dataset contains highly imbalanced classes where fraudulent transactions are very rare compared to normal transactions.

---

## 🛠️ Steps Performed

1. Loaded and explored the dataset  
2. Verified class imbalance  
3. Applied feature scaling (StandardScaler)  
4. Created 5 balanced samples using different sampling techniques:
   - Random Undersampling
   - Random Oversampling
   - SMOTE
   - Tomek Links
   - SMOTE + Tomek

5. Applied 5 Machine Learning models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - K-Nearest Neighbors
   - Support Vector Machine

6. Evaluated model accuracy for each sampling method  
7. Compared results using a performance table  
8. Identified the best sampling technique for each model

---

## 📊 Evaluation

- Metric Used: Accuracy
- Total Experiments: 25 (5 Sampling × 5 Models)
- Results stored in a comparison table
- Best model–sampling combination selected based on highest accuracy

---

## 📦 Libraries Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Matplotlib

---

## ▶️ How to Run

```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib
python sampling_assignment.py
