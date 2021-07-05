# Import Statements….
# Modules - group of libraries or functions…
# Import numpy as np…. Common aliases….

# Variables….
# Variable cannot start with numbers or special characters… And only contain alphanumeric letters and underscore… Usually starts with lower case letters.
# You end up with a "name" error while using strings if quotes not used properly …

# Functions…
# Positional arguments - Parameters passed to a function with positional arguments must come in order
# Good practice to put space after a comma
# Keyword argument - comes after positional arguments…. If there are multiple arguments they can come in any order
# E.x. - plt.plot( xaxis positional argument, yaxis positional argument, label = " Ransom" )…  last parameter is keyword argument also a legend parameter in this example.

# Pandas…
# Helps load tabular data from different source like databases or spreadsheets(CSV - comma seperated values)…
# Search particular row and columns
# Easy to find aggregates, avg, deviations
# Combining data from multiple sources
# Pandas introduces dataframe, new kinda data type
# Import pandas as pd…
# Df.head() … is a method, different from other functions… how?
# Df.info()… method that tells no of rows, columns, columns type etc.
# Df.read_csv("filename.ext")… loads the file into dataframe
# String notation and dot notation…. Df['column colName'], df.column_name respectively

# Df.price > 20…. Filters out column values where the statement is true.
# Df[ df.price > 20 ]… filters out the rows where the statement is true.
