import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for Seaborn
sns.set(style="whitegrid")
# Load Data
df = pd.read_csv('expenses.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
df['Week'] = df['Date'].dt.to_period('W')

# Filter out expenses
expenses = df[df['Type'] == 'Expense']

daily_expenses = expenses.groupby('Date')['Amount'].sum()
plt.figure(figsize=(10, 6))
plt.plot(daily_expenses.index, daily_expenses.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Daily Expenses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

weekly_expenses = expenses.groupby('Week')['Amount'].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=weekly_expenses.index.astype(str), y=weekly_expenses.values, palette='viridis')
plt.xlabel('Week')
plt.ylabel('Amount')
plt.title('Weekly Expenses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

monthly_expenses = expenses.groupby('Month')['Amount'].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=monthly_expenses.index.astype(str), y=monthly_expenses.values, palette='magma')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Expenses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

category_expenses = expenses.groupby('Category')['Amount'].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=category_expenses.index, y=category_expenses.values, palette='coolwarm')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('Expenses by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart of Expenses by Category:
plt.figure(figsize=(10, 6))
category_expenses.plot.pie(autopct='%1.1f%%', colors=sns.color_palette('coolwarm', len(category_expenses)))
plt.ylabel('')
plt.title('Expenses by Category')
plt.tight_layout()
plt.show()
