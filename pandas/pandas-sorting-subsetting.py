# Pandas built on top of matplotlib and numpy
# Df.shape.... Is an attribute therefore does not contain parenthesis gives (rows, columns) count
# Df.describe() ... Is a method which gives mean, std,min, max, quartile etc.
# Df.values... Attr displays a 2d array of values stored..
# Df.columns... Attr gives column names in a 1d array(index or row of colnames)
# Df.index... Attr give an array of row indexes, contains index object of row numbers

# Sorting & subsetting...
# Df.sort_values("colName", ascending=False).... Sorts df wrt to colname in ascending order
# Df.sort_values(["colName1", "colName2"], ascending=[True, False])... Sorts col1 & col2 in respective orders..
# Df[[col1, col2]]... Displays two columns side by side, This is also called subsetting
# Df["height_cms"]>90... Also subsetting, there are a lot of ways of doing so
# Df[ date > "2019-05-30"]... Here the mentioned date is in international format.
# Df["col_name_color"].isin(["black", "brown")].... Filters dataframe for black and brown color


# Adding a new column...
# Df["new_col"] = df["old_col"]/100.... New column is created in the dataframe
