
while True:
	try:
		horas_trabajadas=float(input ("Introrduzca horas trabajadas: "))
		
		break
	except ValueError:
		print("Favor de poner un valor numerico")

while True:
	try:
		tarifa_hora=float(input ("Introduzca la tarifa por hora: "))
		break
	except ValueError:
		print("Favor de poner un valor numerico")

def calculo_salario(horas_trabajadas,tarifa_hora):
	if horas_trabajadas > 40.0:
		extra=horas_trabajadas-40.0
	else:
		extra=0
	salario_integro=float((horas_trabajadas-extra)*tarifa_hora)
	salario_extra=float(extra*tarifa_hora*1.5)
	salario=salario_integro+salario_extra
	print("Tu Salario Normal es: ", salario_integro)
	print("Tu Salario Extra es: ", salario_extra)
	print("Tu Salario TOTAL: ", salario)
calculo_salario(horas_trabajadas,tarifa_hora)
input()

