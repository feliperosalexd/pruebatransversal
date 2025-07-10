#diccionario para los produptos xd
productos = {
    "8475HD": ["hp", "15.6", "8GB", "DD", "1T", "intel core i5", "nvidia GTX1050"],
    "2175HD": ["lenovo", "14", "4GB", "SSD", "512GB", "intel core i5", "nvidia GTX1050"],
    "JjfFHD": ["asus", "14", "16GB", "SSD", "256GB", "intel core i7", "nvidia RTX2080ti"],
    "fgdxFHD": ["HP", "15.6", "8GB", "DD", "1T", "intel core i3", "Integrada"],
    "GF75HD": ["asus", "15.6", "8GB", "DD", "1T", "intel core i7", "nvidia GTX1050"],
    "123FHD": ["Lenovo", "14", "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", "15.6", "8GB", "DD", "1T", "AMD Ryzen 7", "nvidia GTX1050"],
    "UWU131HD": ["dell", "15.6", "8GB", "DD", "1T", "AMD Ryzen 3", "nvidia GTX1050"]
}



# diccionario stok
#el formato usado es mode, precio, stock
stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "GF75HD": [749990, 2],
    "UWU131HD": [349990, 1],
    "FS1230HD": [249990, 0]
}

def contarstock(marca):
    total = 0
    marca = marca.lower() #transformamos a minuscula xd
    for cod in productos:
        if productos[cod][0].lower() == marca:
            if cod in stock:
                total += stock[cod][1]
    print(f"Stock total de {marca.capitalize()}: {total}")
    #el papel no dice si escriben una marca no registrada pongo stock 0 o marca no registrada #edit, ya lo vi en el ejemplo xd 
def cambiar_precio(codigopc, nuevo_precio):
    if codigopc in stock:
        stock[codigopc][0] = nuevo_precio
        return True
    else:
        return False
    

def mostrar_precios(minprecio, maxprecio):
    lista = []
    for cod in productos:
        if cod in stock:
            precio = stock[cod][0]
            cant = stock[cod][1]
            if minprecio <= precio <= maxprecio and cant > 0:
                marca = productos[cod][0]
                pant = productos[cod][1]
                lista.append(f"{marca}--{pant} pulgdas")
    if lista:
        lista.sort()
        print("Compus entre esos precios:", lista)
    else:
        print("No hay compus en ese rango. :(")