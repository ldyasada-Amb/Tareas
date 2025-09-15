def promedio_temperatura():
    temperaturas = [
    [{"lunes":17,  #Ciudad 1
     "martes":18,
     "miercoles":17,
     "jueves":20,
     "viernes":18,
     "sabado":16,
     "domingo":19}
],

    [{"lunes":17,   #Ciudad 2
     "martes":16,
     "miercoles":19,
     "jueves":20,
     "viernes":18,
     "sabado":16,
     "domingo":15}
     ],
     [{"lunes":17, #ciudad 3
     "martes":19,
     "miercoles":19,
     "jueves":20,
     "viernes":18,
     "sabado":17,
     "domingo":16}],
    ]
    promedio = 0
    for capas in temperaturas:
        for clave,valor in capas[0].items():
                promedio += valor
        print( "temperatura promedio", promedio/7)
        promedio = 0
        print("+"*20)
    return promedio
        
valor = promedio_temperatura()