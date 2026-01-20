import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

subjects = ["math score", "reading score", "writing score"]

df["Average_Marks"] = df[subjects].mean(axis=1)

plt.figure()
plt.plot(df["Average_Marks"], marker='o', linestyle='-')
plt.title("Trend-based Student Performance Progression")
plt.xlabel("Student Index")
plt.ylabel("Average Marks")
plt.show()

subject_mean = df[subjects].mean()
difficulty_index = 100 - subject_mean

print("Subject-wise Difficulty Index:")
print(difficulty_index)

plt.figure()
plt.bar(subjects, difficulty_index)
plt.title("Subject-wise Difficulty Index")
plt.ylabel("Difficulty Level")
plt.show()

df["Consistency_Score"] = df[subjects].std(axis=1)

print("Sample Consistency Scores (Lower = More Consistent):")
print(df["Consistency_Score"].head())

df["Risk_Status"] = np.where(df["Average_Marks"] < 50, "At Risk", "Safe")

at_risk_students = df[df["Risk_Status"] == "At Risk"]
print("Number of At-Risk Students:", len(at_risk_students))

correlation_matrix = df[subjects].corr()

print("Correlation between Subjects:")
print(correlation_matrix)

plt.figure()
plt.imshow(correlation_matrix)
plt.xticks(range(3), ["Math", "Reading", "Writing"])
plt.yticks(range(3), ["Math", "Reading", "Writing"])
plt.title("Correlation Heat Analysis")
plt.colorbar()
plt.show()

plt.figure()
plt.boxplot([df["math score"], df["reading score"], df["writing score"]])
plt.xticks([1, 2, 3], ["Math", "Reading", "Writing"])
plt.title("Subject-wise Marks Distribution")
plt.ylabel("Marks")
plt.show()
