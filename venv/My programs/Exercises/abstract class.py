#abstract class cannot be instatiated. we cannot create objects or instances with this classes.
#it is used for inherting or use as base class.

print(sum(range(1,10)))

import sys
print(dir(sys))

sys.stdout.write("test")
print(sys.argv)

for i in sys.argv:
    print(i)

print(sys.maxsize)
print(sys.path)