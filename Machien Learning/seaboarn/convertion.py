import nbformat as nbf
from nbconvert import HTMLExporter

# Create a new Jupyter notebook
nb = nbf.v4.new_notebook()

# Add markdown and code cells to the notebook
cells = []

# Adding Title and Introduction
cells.append(nbf.v4.new_markdown_cell("""# Pandas Useful Methods - Explained for Everyone
In this notebook, we will cover some useful methods and functions built into pandas. Each method will have a clear explanation, examples, and reasons for using it. These examples are simple and fun to help even kids understand them.

Let's get started!"""))

# Importing Pandas and NumPy
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np

# Sample data to use in examples
df = pd.read_csv('tips.csv')
df.head()"""))

# Explanation for apply method
cells.append(nbf.v4.new_markdown_cell("""## 1. The `apply()` method
The `apply()` method allows you to apply a function along an axis of the DataFrame. It is very useful when you want to perform custom operations on columns or rows.

For example, let's say you want to extract the last four digits of a credit card number."""))
cells.append(nbf.v4.new_code_cell("""# Example for apply method
def last_four(num):
    return str(num)[-4:]

df['last_four'] = df['CC Number'].apply(last_four)
df.head()"""))

# Explanation for apply with lambda
cells.append(nbf.v4.new_markdown_cell("""## 2. Using `apply()` with a Lambda Function
Lambda functions allow us to write small, one-line functions. These can be applied to pandas columns easily using `apply()`.

Let's say we want to calculate 18% of each total bill to see what a typical tip might be."""))
cells.append(nbf.v4.new_code_cell("""# Example for apply with lambda
df['tip_18_percent'] = df['total_bill'].apply(lambda bill: bill * 0.18)
df[['total_bill', 'tip_18_percent']].head()"""))

# Explanation for describe
cells.append(nbf.v4.new_markdown_cell("""## 3. The `describe()` method
The `describe()` method gives you a quick summary of the statistics for numeric columns. It's great for getting an overview of the data.

Let's see the summary of our dataset."""))
cells.append(nbf.v4.new_code_cell("""# Example for describe method
df.describe()"""))

# Explanation for sort_values
cells.append(nbf.v4.new_markdown_cell("""## 4. The `sort_values()` method
The `sort_values()` method is used to sort a DataFrame by one or more columns.

For example, let's sort our data by the tip amount."""))
cells.append(nbf.v4.new_code_cell("""# Example for sort_values
df_sorted = df.sort_values('tip', ascending=False)
df_sorted.head()"""))

# Explanation for corr
cells.append(nbf.v4.new_markdown_cell("""## 5. The `corr()` method
The `corr()` method is used to find the pairwise correlation between columns in the DataFrame.

Let's check the correlation between the total bill and tip."""))
cells.append(nbf.v4.new_code_cell("""# Example for corr method
df[['total_bill', 'tip']].corr()"""))

# Explanation for unique and nunique
cells.append(nbf.v4.new_markdown_cell("""## 6. The `unique()` and `nunique()` methods
The `unique()` method returns the unique values in a column, while `nunique()` returns the number of unique values.

Let's check the unique sizes of the tables and how many different sizes we have."""))
cells.append(nbf.v4.new_code_cell("""# Example for unique and nunique methods
df['size'].unique()
df['size'].nunique()"""))

# Explanation for duplicated
cells.append(nbf.v4.new_markdown_cell("""## 7. The `duplicated()` and `drop_duplicates()` methods
The `duplicated()` method checks for duplicate rows, and `drop_duplicates()` removes the duplicates.

Let's check for duplicates in our dataset."""))
cells.append(nbf.v4.new_code_cell("""# Example for duplicated and drop_duplicates
df.duplicated().sum()
df_cleaned = df.drop_duplicates()
df_cleaned.head()"""))

# Save the cells into the notebook
nb['cells'] = cells

# Writing the notebook to an .ipynb file
notebook_path = '/home/bharath/MYPROJECT/python-learning/Machien Learning/pandas/pandas_methods.ipynb'  # Change this path to the desired output path
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

# Convert the notebook to HTML (optional)
html_exporter = HTMLExporter()
html_exporter.exclude_input = True  # To hide code cells in the HTML output
(body, resources) = html_exporter.from_notebook_node(nb)

# Save the HTML file (optional)


print(f"Notebook saved at {notebook_path}")

