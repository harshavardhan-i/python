# df.set_index( "colname") - sets col from the body to index or row...
# df.reset_index() - resets the previous actions
# df.reset_index(drop=True) - removes the colname that was to reset
# df.loc[["val1", "val2"]] - subsets wrt to the values provided...filters on index values
# Values don't need to be unique in the indexes to perform loc

# Multilevel indexed a.k.a hierarchical indexes???
# df.set_index(["colname1", "colname2"]) - colname2 is nested within colname1
# df.loc[["value1", "value2"]] - subsets outerlevel(value1, value2) with a list 
# df.loc[[(outVal1, inVal1), (outVal2, inVal2)]] - subsets wrt to the tuples provided
# df.sort_index() - sorts indexes...default sorts from outer to inner levels in ascending order
# df.sort_index( level=["index1", "index2"], ascending=[ True, False ] )

# Drawbacks of using indexes...
# indexes are just data - kept in different form, makes it harder to think
# Breaks the "tidy data" principle(tabular format, each row contains single observation, each variable stored in it's own column)... breaks the third rules as index values don't get their own columns
# syntaxes for working wit indexes is different from working with columns
