# 	• Ordered set of data
# 	• They are immutable meaning it can't be changed. Appending an item to it will be error
# 	• But they do support indexing and slicing
# 	• A list is a mutable object

# t = ("a", "b", "c") - it's a tuple
# t =  "a", "b", "c" - also a tuple
# print("a", "b", "c") - will not print a tuple
# print(("a", "b", "c")) - will print a tuple



# t[0] - it'll print a
# t[0] = "d" - Throws an error as tuples are immutable and updating will throw an error
# t = t[0], "d", t[2] - is valid and does not throw error as var t is being reassigned not updated
# a, b, c = t - now individual values of tuple t will be assigned to var a, b  and c in order, this is also called upacking a tuple!

# 	• Tuples can contains more tuples
# 	• Tuples are immutable but if it contains a list then the list itself is mutable within it
# 	• Usage could be when we need to store album with info like release dates and singer name… which generally does not change
