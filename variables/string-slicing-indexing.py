# parrot = "Norwegian Blue"…
# Parrot[3] - will print "w"..

# Negative indexing…
# The string array indexed starting from the last character i.e. e is indexed -1 and l as -2 and so on
# Negative indexes can be obtained by subtracting the string length and character index

# Slicing…
# Parrot[0:6] - will give Norweg… i.e. from index 0 to 5, does not include 6
# Parrot[:6] - gives the same result as the above 
# Parrot[6:] - gives the chars from index 6 to the end of string
# Parrot[:] - prints the entire string

# Slicing with negative indexes…
# Parrot[-4: 2 ] - would not return anything as the first index point to an index after 2, order should be maintained… 
# Parrot[-4:-2], parrot[-4: 12] - will give the same result, Bl

# Using step in slicing…
# Steps defaults to one…
# Parrot[0:6:2] - returns "Nre"… from 0 to 5 but in steps of 2
# Parrot[0:6:3] - returns "Nw"… from 0 to 5 but in steps of 3
# Parrot[1::2] - scans all the indexes from 1 and take steps of 2

# Slicing backwards…
# Letters = "abcdefghijklmnopqrstuvwxyz"…
# Backwards = letters[25:0:-1] - returns letters in reverse and leaves char a
# Letters[25:-1:-1] - can use end index -1 as it’s a negative index (25 itself)
# Letters[25: : -1] - this will give us the entire list in reverse including a
# Letters[:: -1 ] - another way of achieving the above, also known as python slicing idiom
# Since the step is negative the start index must be greater than end index.

# Slicing idioms…
# Letters[::-1] - known for reversing the string
# Letters[-4:] - last four letters
# Letters[-1:] - last letter
# Letters[:1] - first letter
# If the string was empty…
# Letters= ""
# Letters[:1] - returns an empty string, won't crash the code
# Letters[0] - throws an error

