
palabra=input("Introduce la Palabra:")
letra=input("Letra a buscar:")
def contador(palabra,letra):
	contador1=0
	print("La Palabra es: ",palabra)
	print("La letra a buscar es:", letra)
	for letras in palabra:
		if letras == letra:
			contador1=contador1+1
	if float(contador1)==1:
		print("La letra se encuentra",contador1,"vez")
	else:
		print("La letra se encuentra",contador1,"veces")

contador(palabra,letra)

#contador(palabra,letra)
#if contador(palabra,letra)==1 :
#	print ("La palabra esta:",contador(palabra,letra),"vez")
#else :
#    print ("La palabra esta:",contador(palabra,letra),"veces")

