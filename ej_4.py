flag = True
asc = True
desc = True

corte = input("Ingrese 1 para entrar, 0 para salir ")
corte = int(corte)
while corte == 1:
	num = input("Ingrese el número ")
	num = int(num)
	if flag == True:
		mayor = num
		menor = num
		flag = False
	else:
		if mayor > num and desc == True:
			mayor = num
		else:
			desc = False
		if menor < num and asc == True:
			menor = num
		else:
			asc = False
	corte = input("Ingrese 1 para entrar, 0 para salir ")
	corte = int(corte)
	
if asc == True:
	print("ORDEN CRECIENTE")
elif desc == True:
	print("ORDEN DECRECIENTE")
else:
	print("ESTÁN DESORDENADOS")
