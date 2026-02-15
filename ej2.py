
def promedio_cuatro(a, b, c, d):
    return (a+b+c+d)/4
print (promedio_cuatro(10,10,10,10))

"""
tot_exams = input("Cuantos examenes has tenido: ")
notas = []
temp = 1
temp2 = 0

def promedio_cuatro(examenes):
    x=sum(examenes)/len(examenes)
    return x
    
while(temp == 1):
    if tot_exams.isdigit():
        tot_exams = int(tot_exams)
        for i in range(tot_exams):
            temp2 = 1
            while(temp2 == 1):
                inp = input(f"Ingrese la nota del examen {i+1}: ")
                if inp.isdigit():
                    nota = float(inp)
                    notas.append(nota)
                    temp2 = 0
                else:
                    print(f"Ingrese la nota del examen {i+1} (formato numero) ")   
                   
    
        print(f"Tu promedio es {promedio_cuatro(notas)}")
        temp = temp + 1

    else:
        tot_exams = input("Ingresa un numero")

"""
