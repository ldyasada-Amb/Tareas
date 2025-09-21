def calculo_descuento():
    print("Bienvenido al sitema")
    ventas = [] 
    while True:
        print("1 ingrese los productos")
        print("2 lista productos y precios")
        print("3 calculo total")
        print("4 calculo el descuento total")
        print("5 cerrar")
        opcion = int(input("ingrese una opcion"))
        if opcion == 1:
            articulo = input("ingrese el producto")
            precio = float(input("ingrese el precio"))
            producto = {"nombre":articulo,
                        "precio": precio }
            ventas.append(producto)
            print(" artitulo añadido")
            print("+"*20)
        elif opcion == 2:
            for producto in ventas:
                for clave, valor in producto.items():
                    print(f"{clave}:{valor}")
            print("+"*20)
        elif opcion == 3:
            total = 0
            for producto in ventas:
                for clave, valor in producto.items():
                        if clave == "precio":
                            total = total + valor
            print("Precio Total", total)
            print("total con descuento", )
            print("+"*20)      
        elif opcion == 4:
            descuento = total * 0.1
            total_con_descuento= total - descuento
            print("EL total con descuento es", total_con_descuento)
        elif opcion == 5:
            print("gracias")
            break
        else:
            print("dato no valido")
    return 
    
calculo = calculo_descuento()


