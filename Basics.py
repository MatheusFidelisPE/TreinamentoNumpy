import numpy as np



a = np.array([1,2,3])

print(np.__version__)
print(a)  #impressão do array
print(a.shape) #Pegando as dimensões do array
print(a.dtype) #Imprimindo o tipo de dado do array
print(a.ndim) #Imprimindo a quantidade de dimensões do array
print(a.size) #Imprimindo o tamanho do array. O tamanho total do array.
print(a.itemsize)# Imprimindo o tamanho de cada elemento do array em bytes.
print(a[0:]) #indexando elementos do array

b = a * np.array([2,4,6]) #Criando b, fazendo multiplicação entre dois arrays.
c = a * np.array([3]) #Criando um array multiplicando todos os elementos de a por 3.
print(a)
print(b)
print(c)
print(np.sqrt(c)) #Imprimindo a raiz de cada elemento do array
print(np.log10(c)) #Imprimindo o log na base 10 de cada elemento do array
