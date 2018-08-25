while True:
	try:
		valor_de_entrada=float(input ("Introduce valor entre 0 y 1: "))
		if valor_de_entrada >= 0.0 and valor_de_entrada <= 1.0:
			True
		else:
			valor_de_entrada=float("z")
		break
	except ValueError:
		print("Favor de introducir un valor entre 0 y 1")

def calcula_calificacion(valor_de_entrada):	
	print("Calificacion:", str(valor_de_entrada))
	if valor_de_entrada >= 0.9:
		print("Tu calificacion es excelente")
	elif valor_de_entrada >= 0.8:
		print("Tu calificacion es notable")
	elif valor_de_entrada >= 0.7:
		print("Tu calificacion es buena")
	elif valor_de_entrada >= 0.6:
		print("Tu calificacion es suficiente")
	elif valor_de_entrada < 0.6:
		print("ESTAS REPROBADO")
calcula_calificacion(valor_de_entrada)
input()

