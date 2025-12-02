import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip metadata lines)
df = pd.read_csv("dataset.csv", skiprows=4, quotechar='"')

# Convert all year columns to numeric
year_columns = [str(y) for y in range(1960, 2025)]
for col in year_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ================================
# 1️⃣ HISTOGRAM → Population distribution in 2020
# ================================

plt.figure(figsize=(10, 5))
df["2020"].plot(kind="hist", bins=30)
plt.title("Population Distribution Across All Countries (2020)")
plt.xlabel("Population (2020)")
plt.ylabel("Frequency")
plt.grid()
plt.show()

# ================================
# 2️⃣ BAR CHART → Population of selected countries in 2020
# ================================

selected_countries = ["India", "China", "United States", "Brazil", "Indonesia"]

subset = df[df["Country Name"].isin(selected_countries)]

plt.figure(figsize=(10, 5))
plt.bar(subset["Country Name"], subset["2020"])
plt.title("Population of Selected Countries in 2020")
plt.xlabel("Country")
plt.ylabel("Population (2020)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()
