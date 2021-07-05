# df.mean(axis="index") - finds mean for each row, does rows by default if axis not specified.
# df.mean(axis="columns") - finds mean for each columns
# axis argument does not make sense for normal dataframes, as they have different values in columns.... but makes sense for pivot tables as all the values are the same.

# dataframe["column"].dt.component - access the components of a date (year, month and day) 
# dataframe["column"].dt.month - month component 
# dataframe["column"].dt.year - year component 

# Pivot table is a dataframe with sorted indexes







