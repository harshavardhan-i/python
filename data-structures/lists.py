# 	• Lists: They are ordered sequences containing variety of object types
# 	• lists are mutable
# 	• Lists are intended to contain items of the same type although not enforced

# seq_var.count(".") - Counts the number of occurrence of . 
# list_var.append("something") - Appends the value to the list
# num_var.sort() - sorts the number list in place i.e. does not create or return an object , ascending order
# num_var.sort(reverse=True) - sorts in descending order
# sorted(num_var) - a built in func in python, it sorts the num_var and returns a new, ascending order list/object
# sorted(num_var, reverse=True) - sorts the list in descending order


# 	• num_in_order = sorted(num_var)
# 	• Here the sorted list and original list when compared won't be equal as the numbers are in different order
# 	• Where as if we compare sorted(num_var) & num_in_order they would be equal
# 	• num_in_order = num_var - this is passing by reference and both will point to the same list
# 	• num_in_oreer = list(num_var) - This creates a new list and both are pointing to two separate lists
# 	• num_in_order is num_var - Here "is" compares the two vars and tells if both are pointing to the same list
# 	• list_1 = [] - creates empty list
# 	• list_2 = list() - Also creates an empty list, here we are using list constructor
	
# 	• Iterables - Are the object which return it's member one at a time
# 	• All the sequence types are iterables…
# 	• list("Hello World!") - returns a list like ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
# NoneType - data of type None