# 	• In python 3 ranges are a built in type
# 	• In python 2 ranges are a function
# 	• xrange in python 2 has now become part of ragne in python 3

# print(range(100)) - prints "range(0, 100)"

# my_list = list( range(100) )
# print(my_list)  - returns [0, 1, 2, 3… 99]
# 	• Range itself is gonna take same amount of memory be it 10 or 10000 elements
# 	• Making a list out of that range will take more memory depending on the magnitude of range
# 	• All the operations performed on a sequence cannot be performed on ranges, as ranges follow a defined pattern… e.g. modification or concatenation is not supported

# small_decimals  = range(0, 10) - creates a list of numbers
# small_decimals[3] - prints the number in index 3
# small_decimals.index[3] - returns the index of 3
# range(99, 0, -2) - prints range in reverse order from 99 to 1
# range(0, 100)[::-2] - prints the same as above as slicing with negative steps gives us -1, -3 …

# 	• range(0, 80) is also a generator,  a special kind of function that generates info without storing it in memory
