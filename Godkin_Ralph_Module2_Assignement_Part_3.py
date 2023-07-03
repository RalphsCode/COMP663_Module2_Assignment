# Module 2 Assignment
# Question 3
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
internet_df = pd.read_csv("Module-2/internetusage.csv")

# Print the 5 Categoty Summary
print("\n5 Category Summary: \n\tInternet Usage\n", internet_df['internet_usage'].describe(),"\n")