cant_lib = 0
suma_cos = 0
suma_precio = 0
cant_sup = 0
cant_inf = 0

corte = int(input("Ingrese 1 para entar, 0 para salir "))
while corte == 1:
	cant_lib += 1
	cod = int(input("Ingrese el código del libro "))
	costo = int(input("Ingrese el costo del libro "))
	precio = int(input("Ingrese el precio del libro "))
	suma_cos += costo
	suma_precio += precio
	if precio > 5700:
		cant_sup += 1
	if costo < 3500:
		cant_inf += 1
	corte = int(input("Ingrese 1 para entar, 0 para salir "))

prom_cos = suma_cos // cant_lib
prom_pre = suma_precio // cant_lib
porc_inf = cant_inf * 100 // cant_lib

print("Hay un total de ", cant_lib, " libros, el promedio del costo es ", prom_cos, " y el promedio del precio es ", prom_pre)
print(cant_sup, " libros tienen un precio superior a $5700")
print("El porcentaje de libros con un costo inferior a $3500 es ", porc_inf)
