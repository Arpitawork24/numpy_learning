# Broadcasting means NumPy automatically expands smaller arrays so operations between different shapes become possible.

import numpy as np

a = np.array([15,65,11,55])
b = 10
res1 = np.add(a,b)
res1 = a + b
print(res1)

c = np.array([[5,3,4,6] , [2,4,6,8]])
res2 = a + c
print(res2)

res3 = a*c
print(res3)

#conditional broadcasting
d = np.array(["ADULT", "MINOR"])
res4 = np.where(a>18,d[0],d[1])
print(res4)

corr = np.array([1.5,-0.2,4.7])
res5 = corr[:,None]
print(res5)