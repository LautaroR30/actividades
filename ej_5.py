flag_kwh = True
flag_imp = True

corte = input("Ingrese 1 para entrar, 0 para salir")
corte = int(corte)
while corte == 1:
	num_cue = input("Ingrese el número de cuenta ")
	ape = input("Ingrese el apellido ")
	ape = str(ape)
	nom = input("Ingrese el nombre ")
	nom = str(nom)
	kwh = input("Ingrese su consumo de kWh ")
	kwh = int(kwh)
	imp = input("Ingrese el importe a pagar ")
	imp = float(imp)
	apenom = ape + " " + nom
	if flag_kwh == True:
		menor = kwh
		menor_cue = num_cue
		menor_nom = apenom
		flag_kwh = False
	else:
		if menor > kwh:
			menor = kwh
			menor_cue = num_cue
			menor_nom = apenom
	if flag_imp == True:
		mayor = imp
		mayor_cue = num_cue
		mayor_nom = apenom
		flag_imp = False
	else:
		if mayor < imp:
			mayor = imp
			mayor_cue = num_cue
			mayor_nom = apenom
	corte = input("Ingrese 1 para entrar, 0 para salir")
	corte = int(corte)

print("El usuario con menor consumo es: ", menor_cue, " ", menor_nom)
print("El usuario con mayor importe a pagar es: ", mayor_cue, " ", mayor_nom)
