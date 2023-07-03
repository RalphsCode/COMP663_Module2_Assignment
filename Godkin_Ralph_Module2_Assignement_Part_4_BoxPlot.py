# Module 2 Assignment
# Question 4
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame
internet_df = pd.read_csv("Module-2/internetusage.csv")

# Create the subset
population_df = internet_df[['State', 'Population']]

# BoxPlot
sns.boxplot(y=population_df["Population"]).set(xlabel='US States',ylabel="Population (10's of Millions)")
# Customize y-axis ticks
plt.yticks([0, 10000000, 20000000, 30000000, 40000000])

plt.show()