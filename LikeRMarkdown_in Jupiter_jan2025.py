####Jupyter Notebooks are one of the most common and powerful tools for combining text (using Markdown), code, and output (tables, plots, visualizations) in Python.
#### Steps to Use Jupyter Notebooks: 1. Install a Jupyter Notebook:
pip install notebook

#2. start the Jupyter environment
jupyter notebook
#3. Start the Jupyter environment ## Shell Script Jupyter notebook
#. 1. Create a new notebook, and you'll have two main cell types:
# Markdown Cells**: Write text in Markdown format.
# Code Cells**: Write and execute Python code.

#### Example Markdown in Jupyter: Inside a **Markdown Cell**, you can use Markdown syntax like the following:
# Title: Heatmap Analysis Report
#This is a dynamically generated report for visualizing **data**.

## Data Visualization
#The following heatmap displays trends:
# #### Adding Python Code:
# You can add Python code in a separate code cell, and the output will directly follow the cell execution:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
df = pd.DataFrame(data)

# Create heatmap
sns.heatmap(df, annot=True, cmap='YlGnBu')
plt.show()
