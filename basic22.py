#!/usr/bin/python3
def functionName( level ):
   if level <1:
      raise Exception('value must be greater than 1')
      # The code below to this would not be executed
      # if we raise the exception
   return level

# print(functionName(0))
# print(functionName(5))

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument:",e.args[0])

