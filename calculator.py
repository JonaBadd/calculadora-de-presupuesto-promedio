# Bienvenida al usuario
bienvenida = "¡Bienvenido a la calculadora de presupuesto v2!\n"
print(bienvenida)

# Inputs para saber los meses
month_1 = input("Ingrese el mes en que comienza su presupuesto: ")
month_1 = month_1

month_2 = input("Ingrese el segundo mes de su presupuesto: ")
month_2 = month_2

month_3 = input("Y ahora ingrese el último mes de su presupuesto: ")
month_3 = month_3

# Sub-texto para el usuario de confirmación de los meses
print("\nSu presupuesto será calculado para los meses de", month_1, ",", month_2, "y", month_3)

# Sub-texto para el input del trimestre
print("\nAhora le pediremos los valores que desea utilizar para calcular el trimestre.\n")

# Inputs para el presupuesto
budget_1 = input(f"Ingrese el presupuesto en USD para el mes de {month_1}: ")
budget_1 = int(budget_1)

budget_2 = input(f"Ingrese el presupuesto en USD para el mes de {month_2}: ")
budget_2 = int(budget_2)

budget_3 = input(f"Ingrese el presupuesto en USD para el mes de {month_3}: ")
budget_3 = int(budget_3)

# Sub-texto para el usuario de confirmación del presupuesto
print("\nSu presupuesto en USD es:", budget_1, "para", month_1 + ",", budget_2, "para", month_2 + ",", "y", budget_3, "para", month_3)

# Cálculo total y de promedio
budget_total = budget_1 + budget_2 + budget_3
print("\nSu presupuesto total en USD es:", budget_total)

budget_promedio = budget_total / 3
print("\nSu presupuesto promedio en USD es:", budget_promedio)
