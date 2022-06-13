def cliente(informacion:dict)->dict:

    id_cliente=informacion['id_cliente']
    nombre = informacion['nombre']
    edad = informacion['edad']
    primer_ingreso = informacion['primer_ingreso']
    
    if informacion['edad'] > 18:
        atraccion = "X-Treme"
        valor_boleta = 20000
        apto = "true"
        descuento = 0.05
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = "Carros chocones"
        valor_boleta = 5000
        apto = "true"
        descuento = 0.07
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion = "Sillas voladoras"
        valor_boleta = 10000
        apto = "true"
        descuento = 0.05
    else:
        atraccion = "N/A"
        valor_boleta = "N/A"
        apto = "false"
        descuento = 0.0  
    
    if primer_ingreso==True:
            Total = valor_boleta-(valor_boleta*descuento)
    else:  
            Total = valor_boleta
    mensaje = {'nombre': nombre, 'edad': edad, 'atraccion': atraccion, "apto": apto, "primer_ingreso": primer_ingreso, "total boleta": Total}
    return mensaje

informacion = {}
informacion['id_cliente'] = int(input("introduzca el id del usuario: "))
informacion['nombre'] = str(input("introduzca el nombre del usuario: "))
informacion['edad'] = int(input("introduzca la edad del usuario: ")) 
informacion['primer_ingreso'] =str(input("Primer ingreso? "))
#print (informacion)
print (cliente(informacion))

