
from libpruebatrans import contarstock, cambiar_precio, mostrar_precios

# Menu principal
while True:
    print("\n*** MENU PRINCIPAL ***")
    print("(｡･∀･)ﾉﾞ (●'◡'●)")
    print("1. Ver Stock segun Marca")
    print("2. Buscar por Precio")
    print("3. Cambiar Precio de una compu")
    print("4. Salir del programa")

    opcion = input("elige una opcion: ")

    if opcion == "1":
        marca = input("marca de la compu que quiere ver: ")
        contarstock(marca)


    elif opcion == "2":
        while True:
            try:
                pmax = int(input("Precio maximo: "))
                pmin = int(input("Precio minimo: "))
                
                break
            except:
                print("ingrese un numero porfavor")
        mostrar_precios(pmin, pmax)


# cod es codigo xd 
    elif opcion == "3":
        while True:
            cod = input("Cual compu quieres actualizar (ingrese el codigo): ")
            try:
                nprecio = int(input("Nuevo precio a poner: "))
                hecho = cambiar_precio(cod, nprecio)
                if hecho:
                    print("el precio se actualizo con exito!")
                else:
                    print("Ese modelo no esta registrado losiento.")
            except:
                print("porfa, Solo numeros para el precio.")

            seguir = input("¿Cambiar otro? s para si, n para no (s/n): ").lower()
            if seguir != "s":
                break



    elif opcion == "4":
        print("adios, saliendo del sistema")
        break

    else:
        print("Opcion no valida, intente denuevo")

# ヾ(•ω•`)o

#┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻