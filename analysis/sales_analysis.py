import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visuals directory if it doesn't exist
os.makedirs('visuals', exist_ok=True)

df = pd.read_csv('data/processed_tips_data.csv')

# 1. Barplot - Avg Tip % by Day and Time
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='day', y='avg_tip_pct', hue='time')
plt.title('Average Tip % by Day and Time')
plt.ylabel('Avg Tip %')
plt.savefig('visuals/avg_tip_pct_by_day_time.png')
plt.close()

# 2. Histogram - Total Bill Distribution
tips_full = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
plt.figure(figsize=(8, 6))
sns.histplot(tips_full['total_bill'], bins=20, kde=True)
plt.title('Distribution of Total Bills')
plt.xlabel('Total Bill')
plt.savefig('visuals/total_bill_distribution.png')
plt.close()

# 3. Scatter - Tip % vs Total Bill
tips_full['tip_pct'] = (tips_full['tip'] / tips_full['total_bill']) * 100
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips_full, x='total_bill', y='tip_pct', hue='time')
plt.title('Tip % vs Total Bill')
plt.savefig('visuals/tip_pct_vs_total_bill.png')
plt.close()

# 4. Count Plot - Number of Tips by Day
plt.figure(figsize=(8, 6))
sns.countplot(data=tips_full, x='day', hue='time')
plt.title('Number of Records by Day and Time')
plt.savefig('visuals/tips_by_day_count.png')
plt.close()

print("All visualizations saved in /visuals")
