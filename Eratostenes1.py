import math
print('El siguiente programa implementa la criba de Eratostenes \n')
x=int(input('Ingrese un entero positivo x mayor que 1 \n'))
if(x>3):
    y= math.floor(math.sqrt(x))
else:
    y=x
print()
numeros = []
primos = []
numeros.append(0)
for i in range(1,x+1):
    numeros.append(1)
print('Vamos a obtener los números primos dentro de los siguientes enteros:\n')
#Vamos a escribir en formato de 10 en 10 los enteros hasta x
filas = x//10
digits= math.floor(math.log10(x))
for j in range(0,filas+1):
    if(j<filas):
        for i in range(1+j*10,1+(j+1)*10):
            if(numeros[i]==1):
                print(i, end=' '*(1+digits-math.floor(math.log10(i))))
            if(i == (j+1)*10):
                print('\n')
    else:
        for i in range(1+10*filas,x+1):
            if(numeros[i]==1):
                print(i, end=' '*(1+digits-math.floor(math.log10(i))))
            if(i == x):
                print('\n')
print('Basta cribar por los primos menores o iguales que', y,'\n')
for k in range(1,y+1):
    if(k==1):
        print('Tachamos el 1 pues este no es primo: \n')
        numeros[1]= 0
        for j in range(0,filas+1):
            if(j<filas):
                for i in range(1+j*10,1+(j+1)*10):
                    if(numeros[i]==1):
                        print(i, end=' '*(1+digits-math.floor(math.log10(i))))
                    else:
                        print('X',end = ' '*(1+digits))
                    if(i == (j+1)*10):
                        print('\n')
            else:
                for i in range(1+10*filas,x+1):
                    if(numeros[i]==1):
                        print(i, end=' '*(1+digits-math.floor(math.log10(i))))
                    else:
                        print('X',end = ' '*(1+digits))
                    if(i == x):
                        print('\n')
    else:
        if(numeros[k]==1):
            for t in range(k,1+x//k):
                numeros[k*t]=0
            print('Cribando los multiplos del primo p =',k,'los enteros que quedan son: \n')
            for j in range(0,filas+1):
                if(j<filas):
                    for i in range(1+j*10,1+(j+1)*10):
                        if(numeros[i]==1):
                            print(i, end=' '*(1+digits-math.floor(math.log10(i))))
                        else:
                            print('X',end = ' '*(1+digits))    
                        if(i == (j+1)*10):
                            print('\n')
                else:
                    for i in range(1+10*filas,x+1):
                        if(numeros[i]==1):
                            print(i, end=' '*(1+digits-math.floor(math.log10(i))))
                        else:
                            print('X',end = ' '*(1+digits))    
                        if(i == x):
                            print('\n')
for i in range(2,x+1):
    if(numeros[i]==1):
        primos.append(i)
Pix=len(primos)
print('Hay',Pix,'números primos menores o iguales que x =',x,'. Estos son: \n')
print(primos)
print()
print('El cociente x/log(x) para x =',x,'es igual con', x/math.log(x))
print()
primos1mod4=[]
primos3mod4=[]
for i in range(0,Pix):
    if(primos[i] % 4==1):
        primos1mod4.append(primos[i])
    if(primos[i] % 4==3):
        primos3mod4.append(primos[i])
print('De estos hay',len(primos1mod4),'primos de la forma 4k+1: \n')
print(primos1mod4)
print()
print('Así como',len(primos3mod4),'primos de la forma 4k+3: \n')
print(primos3mod4)
print()



