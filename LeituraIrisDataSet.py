import numpy as np

listaAtributos = []
def valor_classe(data):
    global listaAtributos
    for i in range(150):
        if (data[i, 4] == 'Iris-setosa'):
            data[i, 4] = 1
        elif (data[i, 4] == 'Iris-versicolor'):
            data[i, 4] = 2
        else:
            data[i, 4] = 3
    data = data.astype('float')
    return data

data = np.genfromtxt("iris.data",delimiter=',',dtype= str)
data1 = np.genfromtxt("iris.data",delimiter=',',dtype= str)


print(data.shape)
data = valor_classe(data)
print(data)
print(data[:,0].mean())
print('Média: ', data[:,0].sum()/150)
print("Mínimo valor: ", data[:,0].min())
print("Máximo valor: ", data[:,0].max())

Iris_virginica = data[:,4] == 1
#print(data[Iris_virginica])
'''print("Mínimo valor: ", data[Iris_virginica,0].min())
print("Máximo valor: ", data[Iris_virginica,0].max())
print('Média: ', data[Iris_virginica,0].mean())
print('Variancia: ', np.var(data[Iris_virginica,0]))
print('Mediana: ', np.median(data[Iris_virginica,0]))
print('Desvio Padrão: ', np.std(data[Iris_virginica,0]))
'''
print()
for i in range(4):
    print('COLUNA: ', i)
    print('Média dos valores: ',i ,np.mean(data[:,i:i+1]))
    print('Mediana: ', np.median(data[:,i]))
    print('Mínimo: ', data[:, i].min())
    print('Máximo: ', data[:,i].max())
    print('Vâriancia: ', np.var(data[:,i]))
    print('Desvio Padrão: ', np.std(data[:,i]))
    print('Desvio padrão calculado usando variancia: ', np.sqrt(np.var(data[:,i])))
    print()

print(np.sqrt(10))