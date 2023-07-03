# Module 2 Assignment
# Question 2
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import scipy.stats as st

# Create the DataFrame
NBA2019_df = pd.read_csv("Module-2/NBA2019.csv")
# print(NBA2019_df.head())

# Ask for user selection (defaults to 1 - Points Per Game)
user_choice_code = input("Select a column, enter 1 for Points per game (default), 2 for 2P%, 3 for Rebounds per game, 4 for Assists per game: ") or '1'

# Translate the code to the column name
if user_choice_code == "1":
    user_choice = 'PointsPerGame'
elif user_choice_code == "2":
    user_choice = '2P%'
elif user_choice_code == "3":
    user_choice = 'ReboundsPerGame'
elif user_choice_code == "4":
    user_choice = 'AssistsPerGame'
else:
    print('\nYour choice was not recognized, please enter a number between 1 and 4.\n')
    exit(0)

# Create the subset of the data
NBA2019_df_column = NBA2019_df[user_choice]

# Calculate the Standard Deviation
sample_s = st.tstd(NBA2019_df_column)

# Print the result
print(f"\n\tThe Standard Deviation for {user_choice} is: {sample_s:.2f}\n")