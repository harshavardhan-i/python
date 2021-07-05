# df["colname"].mean() - calculates the mean... median, min, max, quantiles, mode, var, std, sum. cumsum(cumulative sum), cummin, cummax, cumprod
# If mean >> median ... There are large values 
# Statistics can be applied to dates as well, as long as they have a fromat of "datetime64"

# df.colname.agg() - helps you define custom functions for aggregation purposes
# E.x:-
# 	# A custom IQR function, inter quartile range
# 	def iqr(column):
# 	    return column.quantile(0.75) - column.quantile(0.25)
	    
# 	# Print IQR of the temperature_c column
# 	print(sales.temperature_c.agg(iqr))

# df["col1", "col2", "col3"].agg() - performs aggregations on multiple columns
# df["col1", "col2", "col3"].agg([fucn1, func2]) - two custom functions can be called

# Counting...
# df.drop_duplicates(subset="colName") - drops duplicate rows wrt the chosen col
# df.drop_duplicates(subset=["col1", "col2"] -drops duplicates wrt the unique tuple ...
# df.colName.value_counts() - counts the occurrence of a particular value in col
# df.colName.value_counts( sort=True) - brings the top count to the top
# df.colName.value_counts( normalize = True) - converts the counts into proportions

# Grouped Summary...
# df.groupby("col1")["col2"].mean() - groupby helps group by different values in col1, then different functions can be performed. like agg etc.
# df.groupby(["col1", "col2"])["col3"]. mean() - groupby multiple columns
# df.groupby(["col1", "col2"])[["col3", "col4"]]. mean() - groupby multiple columns & aggregate by multiple columns 

# Groupby to pivot tables...
# df.pivot_table( values="col1", index="col2") - groups by index and displays mean value for each group by default
# df.pivot_table( values="col1", index="col2", aggfunc=np.max) - takes aggfunc to perform custom operations...
# df.pivot_table( values="col1", index="col2", aggfunc=[np.max, np.min]) - for multiple agg functions
# df.pivot_table( values="col1", index="col2", columns="col3") - takes in two columns as parameters .... col2 & col3
# df.pivot_table( values="col1", index="col2", columns="col3", fill_value=0) - replaces null values with 0, replaces missing values with a real value (known as imputation)

# df.pivot_table( values="col1", index="col2", columns="col3", fill_value=0, margins=True)- provides mean excluding the filled values.. for columns and indexes...

# Spreadsheets - indexes & values???
