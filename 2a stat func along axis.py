import numpy as np
x = np.array([[6,2,3,1],[0,8,5,9]])
print("\nOriginal array:") print(x)
print("\nMaximum and Minimum value along the first axis:") 
print(np.amax(x, 0),np.amin(x, 0))
print("\nMaximum and Minimum value along the second axis:")
print(np.amax(x, 1),np.amin(x, 1))
