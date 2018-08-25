#while True:
#	try:
#	linea = input("Introduce un numero: ")
#
#		if linea="fin"
#		break
#	except ValueError:
#		print("Favor de poner un valor numerico")
#linea = input("Introduce un numero: ")
n=0
linea=[]
while True:
	try:
		valores= input("Introduce un numero: ")
		if valores=="fin" :
			break
		else :
			valores=float(valores)
			linea.append(valores)
			#print(valores)
			#print(n)
			#print(linea)
			n=n+1
	except ValueError:
		print("Favor de poner un valor numerico") 	
	
def minimo(linea):
	menor=None
	for valor1 in linea:
		if menor is None or float(valor1) < menor:
			menor=valor1
	return menor
	

def maximo(linea):
	mayor=None
	for valor2 in linea:
		if mayor is None or float(valor2) > mayor:
			mayor=valor2
	return mayor
	

def numero_total(linea):
	contador=0
	for valor3 in linea:
		contador=contador+1
	return contador
	

def suma_total(linea):
	contador1=0
	for valor4 in linea:
		contador1=contador1+float(valor4)
	return contador1
	
media=suma_total(linea)/numero_total(linea)

print("Suma Total: ",suma_total(linea))
print("Media: ",media)    
print("Numero de Elementos: ", numero_total(linea))
print("Valor maximo: ", maximo(linea))
print("Valor minimo", minimo(linea))
#print(numero_total(linea),suma_total(linea),maximo(linea),minimo(linea),media)
input()


