# =========================================================
# ADVANCED TEMPERATURE DATA ANALYSIS PROJECT
# =========================================================

# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

# Load CSV file
df = pd.read_csv("temperature_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set date as index
df.set_index('Date', inplace=True)

# Display first rows
print("\nFIRST 5 ROWS OF DATASET")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing temperature values with mean
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())

# ---------------------------------------------------------
# 2. OVERALL TEMPERATURE STATISTICS
# ---------------------------------------------------------

print("\n================================================")
print("OVERALL TEMPERATURE STATISTICS")
print("================================================")

overall_avg = df['Temperature'].mean()
overall_max = df['Temperature'].max()
overall_min = df['Temperature'].min()
overall_std = df['Temperature'].std()
overall_median = df['Temperature'].median()

print(f"Average Temperature : {overall_avg:.2f}")
print(f"Maximum Temperature : {overall_max:.2f}")
print(f"Minimum Temperature : {overall_min:.2f}")
print(f"Median Temperature  : {overall_median:.2f}")
print(f"Standard Deviation  : {overall_std:.2f}")

# ---------------------------------------------------------
# 3. MONTHLY TEMPERATURE ANALYSIS
# ---------------------------------------------------------

# Extract month and year
df['Month'] = df.index.month_name()
df['Month_Number'] = df.index.month
df['Year'] = df.index.year

# Monthly average
monthly_avg = df.groupby('Month_Number')['Temperature'].mean()

# Reorder month names correctly
month_labels = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

print("\nMONTHLY AVERAGE TEMPERATURE")
for i, value in enumerate(monthly_avg):
    print(f"{month_labels[i]} : {value:.2f}")

# ---------------------------------------------------------
# 4. HOTTEST & COLDEST DAYS
# ---------------------------------------------------------

hottest_day = df.loc[df['Temperature'].idxmax()]
coldest_day = df.loc[df['Temperature'].idxmin()]

print("\n================================================")
print("HOTTEST DAY")
print("================================================")
print(hottest_day)

print("\n================================================")
print("COLDEST DAY")
print("================================================")
print(coldest_day)

# ---------------------------------------------------------
# 5. SEASON CLASSIFICATION
# ---------------------------------------------------------

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['Season'] = df.index.month.map(get_season)

seasonal_avg = df.groupby('Season')['Temperature'].mean()

print("\nSEASONAL AVERAGE TEMPERATURE")
print(seasonal_avg)

# ---------------------------------------------------------
# 6. MOVING AVERAGE TREND ANALYSIS
# ---------------------------------------------------------

# 7-day moving average
df['7_Day_MA'] = df['Temperature'].rolling(window=7).mean()

# 30-day moving average
df['30_Day_MA'] = df['Temperature'].rolling(window=30).mean()

# ---------------------------------------------------------
# 7. VISUALIZATIONS
# ---------------------------------------------------------

sns.set_style("darkgrid")

# ---------------------------------------------------------
# Plot 1: Monthly Average Bar Chart
# ---------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.barplot(
    x=month_labels,
    y=monthly_avg.values,
    palette='coolwarm'
)

plt.title("Monthly Average Temperature", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Plot 2: Temperature Trend Over Time
# ---------------------------------------------------------

plt.figure(figsize=(15, 6))

plt.plot(
    df.index,
    df['Temperature'],
    color='lightgray',
    label='Daily Temperature'
)

plt.plot(
    df.index,
    df['7_Day_MA'],
    color='blue',
    linewidth=2,
    label='7-Day Moving Average'
)

plt.plot(
    df.index,
    df['30_Day_MA'],
    color='red',
    linewidth=3,
    label='30-Day Moving Average'
)

plt.title("Temperature Trend Analysis", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Plot 3: Seasonal Average Temperature
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

season_order = ['Winter', 'Spring', 'Summer', 'Autumn']

sns.barplot(
    x=seasonal_avg.index,
    y=seasonal_avg.values,
    order=season_order,
    palette='viridis'
)

plt.title("Seasonal Average Temperature", fontsize=16)
plt.xlabel("Season")
plt.ylabel("Average Temperature")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Plot 4: Temperature Distribution
# ---------------------------------------------------------

plt.figure(figsize=(10, 5))

sns.histplot(
    df['Temperature'],
    bins=20,
    kde=True,
    color='orange'
)

plt.title("Temperature Distribution", fontsize=16)
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Plot 5: Heatmap of Monthly Temperatures
# ---------------------------------------------------------

monthly_yearly = df.pivot_table(
    values='Temperature',
    index='Year',
    columns='Month_Number',
    aggfunc='mean'
)

plt.figure(figsize=(12, 6))

sns.heatmap(
    monthly_yearly,
    cmap='coolwarm',
    annot=True,
    fmt=".1f"
)

plt.title("Yearly Monthly Temperature Heatmap", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Year")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 8. EXTREME WEATHER DETECTION
# ---------------------------------------------------------

# Define thresholds
high_threshold = df['Temperature'].quantile(0.95)
low_threshold = df['Temperature'].quantile(0.05)

extreme_hot = df[df['Temperature'] >= high_threshold]
extreme_cold = df[df['Temperature'] <= low_threshold]

print("\n================================================")
print("EXTREME HOT DAYS")
print("================================================")
print(extreme_hot[['Temperature']].head())

print("\n================================================")
print("EXTREME COLD DAYS")
print("================================================")
print(extreme_cold[['Temperature']].head())

# ---------------------------------------------------------
# 9. SAVE RESULTS
# ---------------------------------------------------------

# Save processed dataset
df.to_csv("processed_temperature_analysis.csv")

print("\nAnalysis Complete!")
print("Processed file saved as 'processed_temperature_analysis.csv'")