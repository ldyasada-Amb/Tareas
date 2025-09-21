list_productos=[]
def datos_personales():
    nombre = input("ingrese el nombre")
    apellido = input("ingrese el apellido")
    direccion = input("ingrese su direccion")
    return nombre, apellido, direccion

def lista_productos():
    while True:
        productos = {"nombre": input("ingrese el nombre del producto"),
            "precio" :float(input("ingrese el precio del producto")),
            "cantidad" : int(input("ingrese la cantidad del producto")),
        }
        list_productos.append(productos)
        opcion = input("ingresara producto si/no:")
        if opcion.lower() == "no":
            break
            

def descuento_por (nombre,apellido,direccion):
    total = 0
    print(f"nombre:{nombre}")
    print(f"apellido:{apellido}")
    print(f"direccion:{direccion}")

    for productos in list_productos:
        total += productos ["precio"]*productos["cantidad"]
    print(f"El total : {total} ")
    return total

def descuento_total (total):
    porcentage = int(input("ingrese el porcentage"))
    descuento = ( total * porcentage)/100
    total_final = total - descuento
    print(f"Descuento aplicado: {descuento}")
    print(f"Total con descuento: {total_final}")
    return total_final

datos_clientes = datos_personales()
pro_list = lista_productos()
factu_t = descuento_por(*datos_clientes) 
final_total = descuento_total(factu_t)


 
