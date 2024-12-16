import time

# Init the count
start = time.time()
def multi_arrays_form1(a, b):
    c = [n * m for n,m in zip(a, b)]
    return c

def multi_arrays_form2(a, b):
    c = []
    for i in range(len(a)):
        num = a[i] * b[i]
        c.append(num)
    return c

a = [1,2,3,4,4,4,4,5,5,6,7,8,8,89,9,12]
b = [2,3,4,2,34,54,3,34,3,4,43,4,4,9,12,456]
c = multi_arrays_form1
print(c)

#Finalice the count
end = time.time()

# Calculate execution time
tiempo_ejecucion = end - start

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
