#Una tienda aplica un 10% de descuento a un producto y después añade un 21% de iva
variable1=int(input("introduce el precio original del producto: "))
descuento = round(precio-precio*10/100,2)
iva = round (descuento+descuento*21/100,2)
print = (f"el producto con precio de ¨{precio}, tiene un descuento de y un total de {iva}")
preciototal = precio * (1-10/100) * (1+21/100)
print("nuevo resultado", preciototal)
print(f"precio total es {preciototal:.2f}")