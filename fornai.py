v1=0
v2=0

v=int(input("cual es la cantidad de votantes :"))
for i in range(v):
    voto=int(input(f"por quien votara. 1.candidato 2.Candidato "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("voto no valido")
if v1>v2:
    print("gano candidato 1")
else:
    print("gano el candidato 2")
