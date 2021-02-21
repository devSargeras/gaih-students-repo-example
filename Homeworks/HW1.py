import random

primeNumbers = list()

for i in range(2, 100):
    kontrol = True
    for j in range(2, i):
        if (i % j == 0):
            kontrol = False
            break
    if kontrol == True:
        primeNumbers.append(i)
print(primeNumbers)

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# ya da  matrix = g[[0 for i in range(3)] for j in rane(3)]

for satir in range(len(matrix)):
    for sutun in range(len(matrix[0])):     
        matrix[satir][sutun] = primeNumbers.pop(random.randint(0, len(primeNumbers) - 1))

print(primeNumbers)
print(matrix)
