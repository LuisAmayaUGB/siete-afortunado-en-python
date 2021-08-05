from random import randint
a=randint(1, 10)
b=randint(1, 10)
c=randint(1, 10)

print(f"Los números generados: ",a,b,c)


if(a==7) and (b==7) and (c==7):
    print("Ganaste!!!!!")
else:
        print("Perdiste!!!!!")
