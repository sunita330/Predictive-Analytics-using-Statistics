# Data Generation using Modelling and Simulation for Machine Learning

## Assignment Description
This project demonstrates how modelling and simulation can be used to generate synthetic data for machine learning applications. A simulation-based approach is adopted to model a real-world system and generate a dataset which is then used to train and compare multiple machine learning models.

---

## Simulation Tool Used
**SimPy** is a Python-based discrete-event simulation framework used to model real-world systems such as queues, hospitals, networks, and service systems.

Reference:
https://en.wikipedia.org/wiki/SimPy

---

## Simulation Model
A **hospital OPD queue system** is simulated where:
- Patients arrive randomly
- Doctors serve patients
- Patients wait if all doctors are busy
- Average waiting time is recorded

---

## Simulation Parameters and Bounds

| Parameter | Description | Lower Bound | Upper Bound |
|---------|-------------|------------|------------|
| arrival_rate | Patient arrival rate | 1 | 10 |
| service_rate | Doctor service rate | 2 | 15 |
| num_doctors | Number of doctors | 1 | 5 |

---

## Data Generation Process
- Random values are generated within defined bounds
- Parameters are passed to the simulator
- Average waiting time is recorded
- 1000 simulation runs are performed
- A synthetic dataset is created and stored in CSV format

### Dataset Columns
- arrival_rate
- service_rate
- num_doctors
- avg_wait_time

---

## Machine Learning Models Used
The problem is treated as a regression task. The following models were trained:

1. Linear Regression  
2. Decision Tree Regressor  
3. Random Forest Regressor  
4. K-Nearest Neighbors (KNN)  
5. Support Vector Regressor (SVR)  

---

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Results
All models were evaluated and compared. Based on RMSE and R² score, **Random Forest Regressor** performed the best.

---

## Visualizations
- Model comparison bar chart
- Actual vs Predicted waiting time plot
- Feature importance plot

---

## Conclusion
This project successfully demonstrates simulation-based data generation using SimPy. A total of 1000 simulations were performed to generate synthetic data. Multiple machine learning models were trained and evaluated, and Random Forest Regressor was identified as the best-performing model.

---

## How to Run
1. Open the notebook in Google Colab
2. Run all cells sequentially
3. Dataset and graphs will be generated automatically

