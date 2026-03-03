"""
AUTHOR: Senait Gezaei
DATE: December 10, 2025 
CLASS: ISTA131
DESCRIPTION: This project visualizes obesity and physical activity data across the United States using various types of plots.
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# Scatter Plot: Obesity Rate vs Physical Activity Rate
plt.figure(figsize=(8,6))

average_obesity = df.groupby('LocationAbbr')['ObesityRate'].mean()
average_physical_activity = df.groupby('LocationAbbr')['PhysicalActivityRate'].mean()

plt.scatter(average_obesity, average_physical_activity, color='darkblue',alpha=0.7)

#  Regression Line
x = average_obesity
y = average_physical_activity

m, b = np.polyfit(x, y, 1) # slope & intercept
plt.plot(x, m*x + b, color='red', linewidth=2)  # regression line


# Set axis limits
plt.xlim(27,37)
plt.ylim(20,40)

#Set labels and title
plt.xlabel("Obesity Rate (%)", fontweight='bold')
plt.ylabel("Physical Activity Rate (%)", fontweight='bold')
plt.title("Obesity Rate vs Physical Activity Rate", fontweight='bold')

plt.show()


# Line Plot: Obesity Rate Over Time for Arizona
plt.figure(figsize=(10,6))

# Filter for Arizona
df_AZ = df[df["LocationAbbr"] == "AZ"]

plt.plot(df_AZ['YearStart'], df_AZ['ObesityRate'], marker='o', color='purple')

plt.grid(alpha=0.3)

# write each point with its obesity rate
for x, y in zip(df_AZ['YearStart'], df_AZ['ObesityRate']):
    plt.text(x, y+0.1, f"{y:.1f}", fontsize=9)

plt.xlabel("Year", fontweight='bold')
plt.ylabel("Obesity Rate (%)", fontweight='bold')
plt.title("Arizona's Obesity Rate Over Time", fontweight='bold')

plt.show()


# Horizontal Bar Chart: Obesity Rate by State in 2020
plt.figure(figsize=(8, 8))

# Filter for 2020
df_2020 = df[df["YearStart"] == 2020].copy()

# Sort by ObesityRate lowest to highest

top_10_df = df_2020.nlargest(10, 'ObesityRate')
bottom_10_df = df_2020.nsmallest(10, 'ObesityRate')
df_2020 = pd.concat([bottom_10_df, top_10_df])
df_2020 = df_2020.sort_values("ObesityRate")
# Horizontal bar chart
plt.barh(df_2020['LocationAbbr'], df_2020['ObesityRate'],
         color='darkgreen')

plt.xticks(np.arange(0, 38, 2))

for x, y in zip(df_2020['LocationAbbr'], df_2020['ObesityRate']):
    plt.text(y+0.1, x, f"{y:.1f}", fontsize=9)

plt.ylabel("State", fontweight='bold')
plt.xlabel("Obesity Rate (%)", fontweight='bold')
plt.title("2020's Obesity Rate: Top and Bottom 10 States", fontweight='bold')

plt.tight_layout()
plt.show()
