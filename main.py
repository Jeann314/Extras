#Série Fibonacci
from time import sleep
i = int(input("Digite quantos termos: "))
while i != 0:
    a, b = 0, 1
    c = 0
    while c < i:
        if a != 0:
            print(str(c+1)+": "+str(b)+"--------"+str(b/a))
            sleep(.5) #pequena pausa para mostrar a próxima linha
            a, b = b, a+b
            c += 1
        else:
            print(str(c+1)+": "+str(b))
            sleep(.5)
            a, b = b, a+b
            c += 1
    i = int(input("Digite quantos termos: "))
