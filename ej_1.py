# contadores
cont_int = 0
cont_mult = 0
cont_pos = 0
cont_neg = 0
cont_gral = 0

corte = int(input("Ingrese 1 para entar, 0 para salir "))
while corte == 1:
	num = int(input("Ingrese el número "))
	cont_gral += 1
	if -107 < num < 59:
		cont_int += 1
	mult_2 = num % 2
	mult_3 = num % 3
	if mult_2 == 0 and mult_3 == 0:
		cont_mult += 1
	if num < 0:
		cont_neg += 1
	elif num > 0:
		cont_pos += 1
	corte = int(input("Ingrese 1 para entar, 0 para salir "))

porc_pos = int(cont_pos * 100 / cont_gral)
porc_neg = int(cont_neg * 100 / cont_gral)

print("Hay ", cont_int, " números comprendidos entre -107 y 59")
print(cont_int, " son múltiplos de 2; 3 y 6")
print("Del total de números, ", porc_pos, "% son positivos, y ", porc_neg, "% son negativos")
