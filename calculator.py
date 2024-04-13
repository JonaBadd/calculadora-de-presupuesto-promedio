#Bienvenida al usuario
bienvenida = "Bienvenido a la calculadora de presupuesto v2\n"
print(bienvenida)

#Inputs para saber los meses
month_1 = input("Ingrese el mes en que comienza su presupuesto:")
month_1 = month_1

month_2 = input("Ingrese el segundo mes de su presupuesto:")
month_2 = month_2

month_3 = input("Y ahora ingrese el ultimo mes de su presupuesto:")
month_3 = month_3

#Sub-texto para el usuario de confirmacion de los meses
print("\nSu presupuesto sera calculado para los meses de", month_1, month_2, "y", month_3)

#Sub-texto para el input del trimestre
print("\nAhora le pediremos los valores que desea ultilizar para calcular el trimestre\n")

#Inputs para el presupuesto
buget_1 = input(f"Ingrese el presupuesto en USD para el mes de {month_1}: ")
buget_1 = int(buget_1)

buget_2 = input(f"Ingrese el presupuesto en USD para el mes de {month_2}: ")
buget_2 = int(buget_2)

buget_3 = input(f"Ingrese el presupuesto en USD para el mes de {month_3}: ")
buget_3 = int(buget_3)

#Sub-texto para el usuario de confirmacion del presupuesto
print("\nSu presupuesto en USD es:", month_1, buget_1, month_2, buget_2, "y", month_3, buget_3)

#Calculo total y de promedio
buget_total = buget_2 + buget_2 + buget_3
print("\nSu presupuesto total en USD es:", buget_total)

buget_promedio = buget_total / 3
print("\nSu presupuesto promedio en USD es:", buget_promedio)