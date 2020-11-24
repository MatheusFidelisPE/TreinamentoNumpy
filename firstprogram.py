import numpy as np



d = np.random.randint(0,15,10)
print(d)
b = a + np.array([2,3,5]) # o array numpy é capaz de realizar operações matemáticas
c = a * 2
print(c)
print(b)

e = np.array([[1,2,3], [5,6,7],[8,9,10]])

print(e)

bool_index = (e >= 4);
print(bool_index.dtype,'\n', bool_index)
a = e[bool_index]
print(a)