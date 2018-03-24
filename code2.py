def hh(arg0sd):
    return arg0sd


print(hh('hsi'))

def my(x):
    if x==0:
        print("zero")
    elif x==1:
        print("one")
    elif x==3:
        print("three")
    else:
        print("i dont know")

import sys
import math

def testfor():

    for i in range(1,10):
        print(i)
        if i>5:
            sys.exit()


testfor()
my(1)
my(0)
my(2)
my(3)