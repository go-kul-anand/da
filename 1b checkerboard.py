import numpy as np 
print("Checkerboard pattern:") 
x = np.zeros((4,4),dtype=int) 
x[1::2,::2] = 1 
x[::2,1::2] = 1 
print(x) 
