#by ssk TechCree
#lern micropython Example 4
import os

# 128  64  32  16  8  4  2  1
#  0    0   0   0  0  0  0  1  = 1

#test_bytes = input("Type one as bytes as 8 0 or 1: ")
test_bytes = 0b0000100

print (test_bytes)

if test_bytes == 1:
    print("1 is equal")
    
if test_bytes == 2:
    print("not equal 1")

elif test_bytes != 1:
    print("not equal 1")
        
else:
    print("ready")
