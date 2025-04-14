"""
Weather Pattern Decoder (Extended)
----------------------------------
This script simulates and decodes seasonal weather patterns using
Seaborn's built-in 'flights' dataset as a temperature proxy.

We perform:
- normalization per year
- statistical summaries
- smoothed seasonal trend detection
- outlier detection using IQR
- per-season analysis (Winter, Spring, Summer, Autumn)
- inter-year delta between hottest and coldest months
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew

# Load dataset
df = sns.load_dataset("flights").copy()
df.rename(columns={"passengers": "temperature"}, inplace=True)

# Ensure month order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)

# Normalize temperature within each year
df["norm_temp"] = df.groupby("year")["temperature"].transform(lambda x: (x - x.mean()) / x.std())

# Statistical summaries
stats = df.groupby("month")["temperature"].agg(["mean", "median", "std", "min", "max"])
stats["variance"] = df.groupby("month")["temperature"].var()
stats["skewness"] = df.groupby("month")["temperature"].apply(skew)

print("\nSTATISTICAL SUMMARY BY MONTH:\n")
print(stats)

# Rolling seasonal trend (3-month average)
df_sorted = df.sort_values(by=["year", "month"])
df_sorted["seasonal_trend"] = df_sorted["norm_temp"].rolling(window=3, min_periods=1).mean()

# Plot seasonal trend (normalized)
plt.figure(figsize=(12, 6))
for year in df["year"].unique():
    subset = df[df["year"] == year]
    plt.plot(subset["month"], subset["norm_temp"], alpha=0.2)
plt.title("Normalized Seasonal Pattern per Year")
plt.ylabel("Normalized Temperature")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot rolling trend (smoothed)
plt.figure(figsize=(12, 5))
plt.plot(df_sorted["seasonal_trend"].values, label="Smoothed Trend", color="teal")
plt.title("Smoothed Seasonal Shift Over Time")
plt.ylabel("Smoothed Normalized Temp")
plt.xlabel("Time Index")
plt.tight_layout()
plt.show()

# Boxplot to show distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="month", y="temperature", palette="coolwarm")
plt.title("Monthly Temperature Distribution (Boxplot)")
plt.ylabel("Temperature")
plt.tight_layout()
plt.show()

# Histogram of all temperatures
plt.figure(figsize=(8, 5))
plt.hist(df["temperature"], bins=20, color="skyblue", edgecolor="black")
plt.title("Overall Temperature Histogram")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Detect outliers using IQR
q1 = df["temperature"].quantile(0.25)
q3 = df["temperature"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df["temperature"] < lower_bound) | (df["temperature"] > upper_bound)]

print("\nOUTLIER RECORDS (IQR method):\n")
print(outliers[["year", "month", "temperature"]])

# Delta between hottest and coldest month per year
peak = df.loc[df.groupby("year")["temperature"].idxmax()]
valley = df.loc[df.groupby("year")["temperature"].idxmin()]
delta = peak[["year", "temperature"]].reset_index(drop=True)
delta["coldest_temp"] = valley["temperature"].values
delta["difference"] = delta["temperature"] - delta["coldest_temp"]

print("\nYEARLY TEMPERATURE DIFFERENCE (Warmest - Coldest):\n")
print(delta)

# Heatmap by year x month
heatmap_data = df.pivot(index="month", columns="year", values="temperature")
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="YlOrRd", annot=True, fmt=".0f")
plt.title("Heatmap of Simulated Monthly Temperatures")
plt.tight_layout()
plt.show()

# Assign seasons
season_map = {
    "Dec": "Winter", "Jan": "Winter", "Feb": "Winter",
    "Mar": "Spring", "Apr": "Spring", "May": "Spring",
    "Jun": "Summer", "Jul": "Summer", "Aug": "Summer",
    "Sep": "Autumn", "Oct": "Autumn", "Nov": "Autumn"
}
df["season"] = df["month"].map(season_map)

# Average temperature by season
season_avg = df.groupby("season")["temperature"].mean().sort_values(ascending=False)

print("\nSEASONAL AVERAGES (Simulated):\n")
print(season_avg)

# Plot seasonal averages
plt.figure(figsize=(8, 5))
season_avg.plot(kind="bar", color="tomato")
plt.title("Average Temperature per Season")
plt.ylabel("Avg Temperature")
plt.tight_layout()
plt.show()
