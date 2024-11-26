##Voy a declarar las variables y a crear el menú
##Primero puse las opciones
print("Bienvenido a Gaseosas.SAS\nConozca nuestros productos de gaseosas en botellas de 1.5L: \n1.)Pepsi\n2.)Coca Cola\n3.)Colombiana")
Producto_seleccionado=int(input("Por favor escriba:\n1\n si desea adquirir PEPSI\n2\n si desea adquirir COCA COLA\n3\n si desea adquirir COLOMBIANA \n"))
if Producto_seleccionado==1:
    print("Usted ha seleccionado el producto:\n1.)Pepsi\nExitosamente")
elif Producto_seleccionado==2:
    print("Usted ha seleccionado el producto:\n2.)Coca Cola\nExitosamente")
elif Producto_seleccionado==3:
    print("Usted ha seleccionado el producto:\n3.)Colombiana\nExitosamente")
##AQUI HAY UN PROBLEMA SI SE PONE EL ELSE SIGUE CON EL SIGUIENTE PRINT,NO RETORNA AL MENU PRINCIPAL
else:
    print("Usted no ha seleccionado ninguno de los productos disponibles")
Cantidad_deseada=int(input("Por favor indique la cantidad de botellas de 1.5L que desea:\n"))
if Cantidad_deseada>0 and Cantidad_deseada!=1:
##AQUI HAY OTRO PROBLEMA Y ES QUE PRODUCTO SELECCIONADO SOLO ES UN NUMERO ENTONCES DIRA BOTELLAS DE 1.5L DE 1 , 2 O 3 NO DIRA EL NOMBRE DEL PRODUCTO 
    print("Usted ha seleccionado","\n",Cantidad_deseada,"botellas de 1.5L de ",Producto_seleccionado,"\nExitosamente")
elif Cantidad_deseada==1:
    print("Usted ha seleccionado\n",Cantidad_deseada,"botella de 1.5L de ",Producto_seleccionado,"\nExitosamente")
else:
    print("Usted no ha seleccionado ninguna cantidad de ",Producto_seleccionado)


#///////////////////////////// prueba carga de datos desde el visual de mi pc