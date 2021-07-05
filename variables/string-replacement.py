# In python every data can be coerced into string…
# Age = 5
# Print("hello" + age) - will throw an error as 5 is an int
# Print("hello" + str(age)) - will convert the 5 into a string and print the statement

# In python 3 and above we've better options than str… using replacement fields and dot format method…e.g.
# Print("hello {0}".format(age)) - here the curly braces are the replacement fields and then we have dot format…
# Print("Hello there {0}, {1} & {3}".format(1, "harsh", "june")) - prints all three values by replacing respective replacement fields 
# The fields can be used more than once and they don't have to be in the order replacement fields are present… It's the indexes mentioned that matters.
# Print("hello there {1}, {0} & {0}".format(harsh, hero)) - this will return "hello hero, harsh & harsh"… works similarly with triple double quotes..

# String Formatting…
# I ** 2 - means I raised to the power 2
# Print("Hello {0:2}".format(2)) - this new replacement field value gives number a width of two chars… output would be "Hello  2" - the two characters are space and a number…
# Print("Hello {0:<2}".format(2)) - < char makes the value left aligned… similarly > makes it right aligned…and ^ (carat) symbol makes it center aligned…

# 	• float formatting {value:width.precision f}
# Print("{0:12}".format(22/7)) - defaults to printing 15 decimals since f is not utilized…
# Print("{0:12f}".format(22/7)) - defaults to printing 6 decimals  
# Print("{0:12.50f}".format(22/7)) - prints with 50 places with the decimal and ignores the 12 as it values precision over char limit
# Print("{0:52.50f}".format(22/7)) - prints total 52 chars out of which 50 are decimals
# Print("{0:72.54f}".format(22/7)) - maximum decimal precision for python is between 51 to 53 digits… so in this case after 51 decimal places the numbers would be padded by zeroes …
# Print("{0:>08b}".format(i)) - prints binary value of the number
# Print("{0:>02x}".format(i)) - prints hex values of the number
# Print(0b101010) - prints base ten values of the binary input

# Print("Hello {}, {} & {:4}".format(1, 2, 3)) - In this case since the indexes are not specified values can't repeat and the order would be used to map output, string formatters work without indexes as well…





