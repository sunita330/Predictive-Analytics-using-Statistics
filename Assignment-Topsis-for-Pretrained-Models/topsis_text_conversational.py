import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Define Models
# -----------------------------
models = [
    "DialoGPT-small",
    "DialoGPT-medium",
    "BlenderBot-400M",
    "BlenderBot-1B",
    "GPT-Neo-125M"
]

# -----------------------------
# STEP 2: Decision Matrix
# (Values based on literature & benchmarks)
# -----------------------------
# Columns:
# Response Quality, Coherence, Latency(ms), Model Size(MB), Ease of Fine-tuning
data = np.array([
    [7.5, 7.0, 120, 350, 8.5],   # DialoGPT-small
    [8.2, 8.0, 180, 800, 7.5],   # DialoGPT-medium
    [8.6, 8.4, 220, 900, 7.0],   # BlenderBot-400M
    [9.0, 9.1, 300, 2500, 6.0],  # BlenderBot-1B
    [8.0, 7.8, 200, 500, 8.0]    # GPT-Neo-125M
])

df = pd.DataFrame(
    data,
    index=models,
    columns=[
        "Response Quality",
        "Coherence",
        "Latency",
        "Model Size",
        "Ease of Fine-tuning"
    ]
)

print("\nDecision Matrix:\n")
print(df)

# -----------------------------
# STEP 3: Normalize the Matrix
# -----------------------------
norm_df = df / np.sqrt((df ** 2).sum())
print("\nNormalized Matrix:\n")
print(norm_df)

# -----------------------------
# STEP 4: Assign Weights
# -----------------------------
weights = np.array([0.30, 0.25, 0.15, 0.10, 0.20])

weighted_df = norm_df * weights
print("\nWeighted Normalized Matrix:\n")
print(weighted_df)

# -----------------------------
# STEP 5: Ideal Best & Worst
# -----------------------------
benefit_cols = ["Response Quality", "Coherence", "Ease of Fine-tuning"]
cost_cols = ["Latency", "Model Size"]

ideal_best = []
ideal_worst = []

for col in weighted_df.columns:
    if col in benefit_cols:
        ideal_best.append(weighted_df[col].max())
        ideal_worst.append(weighted_df[col].min())
    else:
        ideal_best.append(weighted_df[col].min())
        ideal_worst.append(weighted_df[col].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

# -----------------------------
# STEP 6: Distance Calculation
# -----------------------------
distance_best = np.sqrt(((weighted_df - ideal_best) ** 2).sum(axis=1))
distance_worst = np.sqrt(((weighted_df - ideal_worst) ** 2).sum(axis=1))

# -----------------------------
# STEP 7: TOPSIS Score
# -----------------------------
topsis_score = distance_worst / (distance_best + distance_worst)

df["TOPSIS Score"] = topsis_score
df["Rank"] = df["TOPSIS Score"].rank(ascending=False)

print("\nFinal Ranking (TOPSIS Result):\n")
print(df.sort_values("Rank"))

# -----------------------------
# STEP 8: Visualization
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(df.index, df["TOPSIS Score"])
plt.xticks(rotation=30)
plt.xlabel("Conversational Models")
plt.ylabel("TOPSIS Score")
plt.title("TOPSIS Ranking of Conversational AI Models")
plt.tight_layout()
plt.show()

# -----------------------------
# STEP 9: Best Model
# -----------------------------
best_model = df["TOPSIS Score"].idxmax()
print("\nBest Pre-trained Conversational Model according to TOPSIS:")
print(best_model)
