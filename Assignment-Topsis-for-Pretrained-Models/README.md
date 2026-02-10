# Assignment – TOPSIS for Text Conversational Models

## 📌 Problem Statement
Apply **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** to identify the **best pre-trained conversational (chatbot) model** based on multiple evaluation criteria.

This task is assigned for **Text Conversational systems** as per roll number rule.

---

## 🎯 Objective
The objective of this assignment is to:
- Compare multiple **pre-trained conversational AI models**
- Evaluate them using **multiple conflicting criteria**
- Apply the **TOPSIS method**
- Rank the models and identify the **best chatbot model**

---

## 🛠️ Technologies Used
- **Python 3**
- **NumPy** – Numerical computation
- **Pandas** – Tabular data handling
- **Matplotlib** – Visualization (graph plotting)

All libraries used are open-source and available via PyPI.

---

## 🤖 Models Considered
The following popular pre-trained conversational models are evaluated:

1. DialoGPT-small  
2. DialoGPT-medium  
3. BlenderBot-400M  
4. BlenderBot-1B  
5. GPT-Neo-125M  

---

## 📊 Evaluation Criteria
The models are evaluated using the following criteria:

| Criterion | Description | Type |
|---------|------------|------|
| Response Quality | Quality of generated responses | Benefit |
| Conversational Coherence | Contextual consistency | Benefit |
| Latency (ms) | Response time | Cost |
| Model Size (MB) | Memory footprint | Cost |
| Ease of Fine-tuning | Adaptability | Benefit |

---

## ⚖️ TOPSIS Methodology
The following TOPSIS steps are implemented:

1. Construct the **decision matrix**
2. Normalize the decision matrix
3. Assign weights to each criterion
4. Create the weighted normalized matrix
5. Determine the **ideal best** and **ideal worst**
6. Compute distances from ideal solutions
7. Calculate **TOPSIS scores**
8. Rank the models
9. Identify the best model

---

## ▶️ How to Run the Code

### 1️⃣ Install Required Libraries
```bash
pip install numpy pandas matplotlib

