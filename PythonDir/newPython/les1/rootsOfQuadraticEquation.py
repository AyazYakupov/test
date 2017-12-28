import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = int((-b+math.sqrt(b**2-4*a*c))/2*a)
x2 = int((-b-math.sqrt(b**2-4*a*c))/2*a)
print(str(x1)+'\n'+str(x2))
