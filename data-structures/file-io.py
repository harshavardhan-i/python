	# • 
	# • We get Errno 2 for file not found
	# • pwd - present working directory
	# • myfile.read() - prints everything within file, running it consecutively will return '' as the file cursor has moved 
	# • To resolve this we have to use .seek(0) method
	# • Then read again
	
	# • myfile.readlines() - returns a list of lines within file
	# • 
	# • for external files
	# • myfile.close() - must be used
	# • 
	# • new way of opening files, closes file by default

	# • 
	# • modes 
	# 	○ a - append
	# 	○ w - overwrite or creates a new file
	# 	○ r - read
	# 	○ r+ - read and write
	# 	○ w+ - writing and reading… overwrites or creates new
	# • myfile.write('something') - writes to the file
		
