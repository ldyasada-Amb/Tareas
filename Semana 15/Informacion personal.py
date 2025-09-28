informacion_personal = [{"nombre": "Priscila"},
                        {"edad": 27},
                        {"ciudad": "riobamba"},
                        ]
# se cambia y agrega ciudad y profesion
informacion_personal[2]["ciudad"]= "tena"
informacion_personal[2]["profesion"]= "doctor"

#verifica si exsite la clave telefono y se agrega
for datos in informacion_personal:
    if "telefono" in datos:
        print("existe")
    else:
        print("no existe")
        informacion_personal[2]["telefono"]= 900000000
print( informacion_personal)
# elimina edad
for datos in informacion_personal:
    if "edad" in datos:
        del datos["edad"]

# imprimir datos final
for datos in informacion_personal:
    for clave,valor in datos.items():
        print(clave, valor)


        

            
    
    
          
