def serie(x):
    if (x%2)==0:
        return x/2
    else:
        return (3*x) + 1

num=int(input("Digite un numero entero positivo: "))

if num>0:    
    while (num!=1):
        num=int(serie(num))
        print(num)
else:
    print("El numero no es entero positivo")