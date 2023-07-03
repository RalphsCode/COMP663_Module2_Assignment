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

#Get user input
state_index = int(input('Please enter a number from 1-50 (default is 4): ') or '4')

# Create variables
state_data = population_df.iloc[state_index]
state_name = state_data.iloc[0]
state_pop = state_data.iloc[1]

# Print the output
print("\nThe population of " + str(state_name) + " is " + str(state_pop)+ ".\n")

# # BoxPlot - this section is also in a seperate file.

# sns.boxplot(y=population_df["Population"]).set(xlabel='US States',ylabel="Population (10's of Millions)")
# # Customize y-axis ticks
# plt.yticks([0, 10000000, 20000000, 30000000, 40000000])

# plt.show()