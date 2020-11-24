import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(a[:, 2])
print(a)
print(np.linalg.det(a))
print(np.diag(a))
print(a.T)
print(np.linalg.inv())