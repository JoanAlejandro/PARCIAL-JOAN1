def crecimiento(x,y,z):
    pf=z+(z*(y/100)*x)
    return pf
A=25000000
B=18900000
tiempo=0
while A>=B:
    tiempo+=1
    A=crecimiento(tiempo,2,A)
    B=crecimiento(tiempo,3,B)
    if A>=B:
        A=2500000
        B=1890000
año=tiempo+2022
print(f"La poblacion B superera a la A en el: {año} ({tiempo} años despues) Con una poblacion de {B} millones mientras que la otra tendra una poblacion de {A} millones")