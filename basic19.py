
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
# print exampo
# Open a file
fo = open("foo.txt", "w")
fo.write("Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

