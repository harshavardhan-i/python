# list[2:5] - slices the list from index 2 to 4, 5 isn't included
# list[:3] - returns the first three elements
# list[:] - returns the whole list

# Dataframes can be sliced too but we have to set_index and sort_index first...
# Then, df["indexName1" : "indexName2"] - slices the dataframe from indexName1 to indexName2, last index is included.

# df.loc[(touple1) : (touple2)] - slices inner level indexes 
# df.loc[ :, "col1" : "col2"] - subsets cols from col1 to col2 and includes all rows.
# df.loc[(touple1):(touple2), "col1":"col2"] - subsets from touple1 to touple2 and col1 to col2
# df.loc[""indexName1": "indexName2"] - subsets from indexName1 to indexName2
# df.loc["2014": "2016"] - subesets all the dates from year 2014 to 2016
# df.iloc[ 1:5, 2:6 ] - used for actual indexes, subsets rows 1 to 4 and columns 2 to 5... Dates should be in the format ISO8601 i.e. yyyy-mm-dd
