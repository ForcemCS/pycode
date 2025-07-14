import  numpy as np 

arr = np.array([1, 2, 3, 4],dtype=np.int8)
print(arr)

arr[0] = -100 
print(arr)

a1 = np.eye(5)
print(a1[(1,1)])