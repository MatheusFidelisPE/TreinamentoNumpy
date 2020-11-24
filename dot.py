import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]
#Maneira mais lenta de se fazer o produto notável. Primeiro por trabalhar com listas e por fazer um for para
#resultar o produto notavel, que em inglês chama-se dot product.

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]

print(dot)

a1 = np.array(l1)
a2 = np.array(l2)

#Forma mais eficaz de se fazer esse tipo de operação
dot = np.dot(a1,a2)
print(dot)

#Forma não tão eficaz.
dot = (a1 * a2).sum()
print(dot)


