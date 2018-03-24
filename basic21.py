a =10
b = 0

my_list = []

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return (Temperature)



# print(my_list[0])

try:
    # print(my_list[0])
    c = a / b
    print(c)
except Exception as e:
    print(e)

# Try catch with file handling
try:
   fh = open("twewrestfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()




try:
   fh = open("mynewfile", "r")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")



#!/usr/bin/python3
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

# try:
#    l = functionName(-10)
#    print ("level = ",l)
# except Exception as e:
#    print ("error in level argument",e.args[0])
print(functionName(0))
print(functionName(5))
