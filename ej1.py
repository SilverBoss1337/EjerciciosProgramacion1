def es_divisible_entre_3(n):
    if n % 3 == 0:
        return True
    else:
        return False
print(es_divisible_entre_3(9))

"""
x = input("Escriba un numero entero para saber si es dibisible entre 3: ")
temp = 1

def es_divisible_entre_3(n):
    if n % 3 == 0:
        return True
    else:
        return False

while(temp==1):
    if x.isdigit():
        y = int(x)
        if es_divisible_entre_3(y) == True:
            print(f"Correcto, {x} es divisible entre 3 ")
        else:
            print(f"Falso, {x} no es divisible entre 3 ")
        temp = temp -1
    
    else:
        x = input("escriba un numero entero por favor: ")
"""
