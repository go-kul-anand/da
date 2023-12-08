import numpy as np
X = np.array([1,0,2,3,5])
print("Original array:") 
print(X)
print("Size of the memory occupied by the said array:") 
print("%d bytes" % (X.size * X.itemsize))
