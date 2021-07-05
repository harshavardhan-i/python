# 	• An iterator represents a object which contains/returns a stream of data, returns one element at a time
# 	• Object that support iteration are called iterables… e.g. strings, lists
	
# string = "1234567890"
# for char in string:
# 	print(char)
# 	• Here an iterator is created from the string var
# 	• for loop uses the iterator to return each item of the string var
# 	• when the list is exhausted the iterator throws an error which is handled by the for loop

# my_iterator = iter(string) - creates/returns an iterator
# print(my_iterator) - returns the memory location of the iterator
# print(next(my_iterator)) - returns the number in first index

# for char in string: - the iterator is created implicitly
# for char in iter(string)): - the iterator is created explicitly, another way of writing above code
 
	
	
