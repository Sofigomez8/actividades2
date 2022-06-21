print ("Vamos a calcular cuál fue su salario por dia durante el mes de mayo")
salario = float(input("¿Cuál es su salario mensual?: "))
horas = float(input("Introduzca sus horas de trabajo: "))
paga = salario / 31 / horas
print (f"Su salario por dia en el mes de mayo fue $ {paga}")
