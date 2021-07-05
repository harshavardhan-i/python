# In pandas missing data points are represented as NaN (Not a number0)
# df.isna() - Tells if the dataframe has any missing values, generates as boolean true/false tabular data
# df.isna().any() -  Tells if a column contains any missing values 
# df.isna().sum() - Tells the count of trues in a column
# df.isna().sum().plot(kind="bar") - Draws a bar plot for column bools and "True" count tells the missing values.
# df.dropna() - Drops the rows where data is not available, not ideal as we loose on a lot of observations
# df.fillna(0) - Replaces all the NaNs in the df with 0s 
