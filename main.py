import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Data cleaning
df.dropna(inplace=True)

# ===============================
# Bar Chart: Average Score by Subject
# ===============================
avg_scores = df.groupby("Subject")["Score"].mean()

plt.figure()
avg_scores.plot(kind="bar")
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("visualizations/avg_score_subject.png")
plt.close()

# ===============================
# Line Chart: Study Hours vs Score
# ===============================
plt.figure()
plt.plot(df["Study_Hours"], df["Score"], marker="o")
plt.title("Study Hours vs Student Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("visualizations/study_hours_vs_score.png")
plt.close()

# ===============================
# Print Insights
# ===============================
print("Student Performance Analysis Completed")
print("Highest Average Score Subject:", avg_scores.idxmax())
print("Lowest Average Score Subject:", avg_scores.idxmin())
