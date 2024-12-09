def cuadrado(a):
    return a*a
num=0
while num>=0:
    num=int(input("Digite un numero: "))
    if num>=0:
        print("Su cuadrado es: ",cuadrado(num))
    else:
        print("El numero no es positivo")
