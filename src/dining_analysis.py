# -*- coding: utf-8 -*-
"""
Create Date Time : 2025/08/16 13:00
Create User : sunny
Desc : 1
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#region 1. Load data
df = pd.read_csv('../data/tips.csv')
print(df.head())
print(df.info())
#endregion

#region 2. Add feature
df['per_person_bill'] = df['total_bill'] / df['size']
print(df.head())
print(df.info())
#endregion

#region 3. Multidimensional Visualization Report
#region 3.1. boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='per_person_bill',data=df, order=['Thur', 'Fri', 'Sat', 'Sun'], color='blue')
plt.title('Per Person Bill by Day (Thursday to Sunday)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=df, order=['Thur', 'Fri', 'Sat', 'Sun'], color='blue')
plt.title('Total Bill by Day (Thursday to Sunday)')
plt.show()
print(f'Conclusion on Spending and Day:\n'
      f'There has no big difference between total and per person bill,\n'
      f'but from cost perspective, We prefer per person bill is high, more customer means more cost.\n'
      f'so combine these we can find the Friday and Saturday is the gold time.')

gender_percentage = df['sex'].value_counts(normalize=True) * 100
print(gender_percentage)
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', data=df)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='per_person_bill', data=df, order=None, color='blue')
plt.title('per_person_bill by Sex (Thursday to Sunday)')
plt.show()
print(f'Conclusion on consume and gender:\n'
      f'There are more male customers than female customers\n'
      f'The average per-person spending of male customers is also higher\n'
      f'Male customers show more high-value outliers\n'
      f'The restaurant appears to attract slightly more male customers, '
      f'and males tend to have higher per-person spending and more outliers.')

plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='total_bill', data=df, order=None, color='blue')
plt.title('Total Bill by Gender (Thursday to Sunday)')
plt.show()
#endregion
#region 3.2. violinplot
plt.figure(figsize=(10, 6))
sns.violinplot(x='time', y='total_bill', hue='sex', data=df)
plt.title(f'Total Bill by time and gender')
plt.show()
print(f"We can see that people's consumption habits are similar,\n "
      f"but there is a large variation in dinner spending, with the overall level being higher.")
#endregion
#region 3.3. scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot( x="total_bill", y="tip", hue="time", style="day", size=None, data=df)
plt.title(f'Consume habit by time and day')
plt.show()
print(f'Saturday has the highest number of records,'
      f'we can also see a linear positive correlation with total_bill and tip.')
#endregion
#region 3.4. stripplot
plt.figure(figsize=(10, 6))
sns.stripplot(x='sex', y='tip', hue=None, data=df, order=None, hue_order=None, palette=None,jitter=True, dodge=False)
plt.title('Tips by Gender (Thursday to Sunday)')
plt.show()
print(f'Tips are mostly concentrated between 0–4.')

plt.figure(figsize=(10, 6))
sns.stripplot(x='day', y='tip', hue=None, data=df, order=None, hue_order=None, palette=None,jitter=True, dodge=False)
plt.title('Tips by Day (Thursday to Sunday)')
plt.show()
print(f'Saturday and Sunday show the strongest effects, with Saturday having the highest tip values.')

plt.figure(figsize=(10, 6))
sns.stripplot(x='time', y='tip', hue=None, data=df, order=None, hue_order=None, palette=None,jitter=True, dodge=False)
plt.title('Tips by Time (Thursday to Sunday)')
plt.show()
print(f'Significant difference in Dinner')
#endregion

#region 3.5. relplot
sns.relplot(data=df, x="total_bill", y="tip", hue="smoker",height=6, aspect=1.8)
plt.title('Relationship between Total Bill and Tip by Smoker',pad=20)
plt.tight_layout()
plt.show()
print(f'there has no big difference between smoker and non-smokers.')
#endregion
#endregion

#drop useless feature
dining_df = df.drop('smoker', axis=1)
print(dining_df.info())

print(
    "Reasons for dropping the 'smoker' feature:\n"
    "- Visualization shows no significant relationship between smoking status and spending/tipping.\n"
    "- From a business standpoint, smoking habits have weak correlation with dining behavior.\n"
    "- Simplifying the dataset improves efficiency for further analysis."
      )

# =====================
# ANALYSIS SUMMARY
# =====================
#region 4.ANALYSIS SUMMARY
sns.jointplot(
    x='total_bill', y='tip',
    data=dining_df,
    kind='scatter',
    hue='time',
    palette={'Dinner': 'blue', 'Lunch': 'red'},
    alpha=0.7,
    height=8
)
plt.title('ANALYSIS SUMMARY')
plt.tight_layout()
plt.show()

# Select all numeric columns for correlation
numeric_cols = dining_df.select_dtypes(include=['number']).columns
correlation_matrix = dining_df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    center=0,
    fmt='.2f',
    square=True
)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.show()
#endregion

#region 5.Report
print(
    """
=== Summary of Dining Data Analysis ===

1. Time-Based Spending Patterns
   - Friday and Saturday are peak spending periods with the highest traffic and bill amounts.
   - Dinner spending shows greater variance and is generally higher than lunch.

2. Customer Gender Analysis
   - Male customers outnumber female customers (64% vs 36%).
   - Males have higher per-person spending and total spending.
   - Males show more high-value outliers, indicating a high-spending segment.

3. Tipping Behavior
   - Tips are mainly concentrated between 0–4 USD.
   - Saturday shows the highest tipping behavior, followed by Sunday.
   - Dinner tips are noticeably higher than lunch tips.
   - Total bill and tip amount show a positive correlation.

4. Value of Feature Engineering
   - The engineered feature 'per_person_bill' provides a valuable new perspective.
   - It helps isolate true individual spending by removing the effect of party size.

5. Feature Selection Decisions
   - 'smoker' was removed due to its weak association with spending behavior.
   - Core features retained: total_bill, tip, sex, day, time, size, per_person_bill

Business Recommendations:
1. Develop targeted marketing strategies to further tap into the high-spending male segment while attracting more female customers.
2. Consider lunch promotions or meal bundles to increase noon traffic.
3. Increase staffing and optimize operations during Friday and Saturday dinner peaks.
"""
)
#endregion

#region 6.Save final dataset
dining_df.to_csv('restaurant_analysis_final.csv', index=False)
print("最终数据集已保存: restaurant_analysis_final.csv")
#endregion