cant_pos = 0
cant_neg = 0
cont_int = 0
cant_total = 0

corte = input("Ingrese 1 para entrar, 0 para salir ")
corte = int(corte)
while corte == 1:
	num = input("Ingrese el número ")
	num = int(num)
	cant_total += 1
	if num > 0:
		cant_pos += 1
	elif num < 0:
		cant_neg += 1
	if 138 <= num <= 1635:
		cont_int += 1
	corte = input("Ingrese 1 para entrar, 0 para salir ")
	corte = int(corte)
porc_int = cont_int * 100 / cant_total
print("Hay ",cant_pos, " números positivos, y ", cant_neg, " son negativos")
print("El porcentaje de números que pertenecen al intervalo [138;1635] es de ", porc_int, "%")
