import pandas as pd
import matplotlib.pyplot as plt

# Sample expense data
data = {
    'Category': ['Rent', 'Groceries', 'Entertainment', 'Utilities', 'Transportation', 'Savings'],
    'Amount': [1200, 400, 150, 200, 100, 500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Pie chart for expense distribution
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
plt.title('Expense Distribution')

# Bar chart for expenses
plt.subplot(1, 2, 2)
plt.bar(df['Category'], df['Amount'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Amount ($)')
plt.title('Expenses by Category')
plt.xticks(rotation=45)

# Show plots
plt.tight_layout()
plt.show()
