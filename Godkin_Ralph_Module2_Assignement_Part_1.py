# Module 2 Assignment
# Question 1
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
cars_df = pd.read_csv("Module-2/mtcars.csv")

# Find the mean, median, and mode of the column wt.
sample_mean = cars_df['wt'].mean()
sample_median = cars_df['wt'].median()
sample_mode = cars_df['wt'].mode()

# Print the mean, median, and mode
print(f"\n\twt Mean:   {sample_mean:>10,.5f}")
print(f"\twt Median: {sample_median:>10,.5f}")
print(f"\twt Mode: {sample_mode}\n")
