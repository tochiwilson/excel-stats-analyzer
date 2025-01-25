import pandas as pd

# Load an Excel File and Get Basic Stats

# Description:
# Create a script that loads an Excel file and calculates statistics
# such as the mean, sum, maximum, and minimum of numerical columns.
# Provide an overview of column names, the number of rows, and the number of missing values per column.

# Challenge:
# Add data visualizations. Use the matplotlib or pandas library to generate graphs,
# such as histograms for numerical columns or a boxplot to visualize the spread.
# This helps make the statistics more insightful.


excel_file = 'products_data.xlsx'
dataframe = pd.read_excel(excel_file)
print(dataframe)

print("\nColumn names:")
print(dataframe.columns)

print("\nNumber of rows:")
print(len(dataframe.index))

print("\nNumber of missing values:")
print(dataframe.isnull().sum())

price_quantity_df = dataframe[['Price', 'Quantity']]
print("\nStatistics for the columns 'Price' and 'Quantity':")

print("Average:")
print(price_quantity_df.mean())

print("\nSum:")
print(price_quantity_df.sum())

print("\nMax:")
print(price_quantity_df.max())

print("\nMin:")
print(price_quantity_df.min())
