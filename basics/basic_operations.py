import numpy as np

#addition
a = np.array([7,9,8,10])
b = np.array([1,2,3,4])
res1 = np.add(a,b)
print(res1)

#subtraction
c = np.array([20,35,42,67]) 
d = np.array([15,7,31,59])
res2 = np.subtract(c,d) # its a - b
print(res2)

#multiplication
res3 = np.multiply(a,b)
print(res3)

#division
res4= np.divide(a,b) #its a divide to b
print(res4)

#exponent
res5= np.power(a,b) #its a raise to b
print(res5)

#modulus
res6 = np.mod(a,b)
print(res6)