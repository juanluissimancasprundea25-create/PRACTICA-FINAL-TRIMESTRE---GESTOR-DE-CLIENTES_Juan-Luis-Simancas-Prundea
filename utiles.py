def buscar_cliente(dni_list, total, dni_buscado):
    pos = -1
    i = 0
    while i < total and pos == -1:
        if dni_list[i] == dni_buscado:
            pos = i
        else:
            i += 1
    return pos

def alta_cliente(dni, nombre, apellidos, telefono, total, maximo):#FUNCION PARA AÑADIR A UN CLIENTE
    if total < maximo:
        nuevo_dni = input("Escribe el DNI del cliente que quieres dar de alta: ")
        pos = buscar_cliente(dni, total, nuevo_dni)
        if pos == -1:
            dni[total] = nuevo_dni
            nombre[total] = input("Escribe el nombre del cliente que quieres dar de alta: ")
            apellidos[total] = input("Escribe los apellidos del cliente que quieres dar de alta: ")
            telefono[total] = input("Escribe el telefono del cliente que quieres dar de alta: ")
            print("Hems añadido a tu cliente : )")
            total += 1
        else:
            print("No puedes poner un DNI igual al que otro cliente")
    else:
        print("No hay mas huecos , sorry :(")
    return total

def listar_clientes(dni, nombre, apellidos, telefono, total):#FUNCION PARA MOSTRAR TODOS LOS CLIENTES
    if total == 0:
        print("No has añadido a nungun cliente , fijate que los hayas gusrdado bien en el primer paso o si has cargado algun archivo anterior que poseas ;)")
    else:
        print("\nLa lista de clientes son :")
        i = 0
        while i < total:
            print(f"{dni[i]} - {nombre[i]} {apellidos[i]} - Tel: {telefono[i]}")
            i += 1

def buscar_por_dni(dni, nombre, apellidos, telefono, total):#FUNCION PARA BUSCAR A UN CLIENTE EN ESPECIFICO POR SU DNI
    dni_buscado = input("Escribe el DNI del cliente a quien quieres buscar: ")
    pos = buscar_cliente(dni, total, dni_buscado)
    if pos != -1:
        print("El cliente que buscas es este , denada ;) :")
        print(f"{dni[pos]} - {nombre[pos]} {apellidos[pos]} - Tel: {telefono[pos]}")
    else:
        print("Ese cliente no existe , sorry :(")

def modificar_telefono(dni, telefono, total):#FUNCION PARA CAMBIAR EL TELEFONO FEL CLIENTE
    dni_buscado = input("Escribe el DNI del cliente a quien quieres cambiarle el telefono: ")
    pos = buscar_cliente(dni, total, dni_buscado)
    if pos != -1:
        telefono[pos] = input("Escribe el nuevo telefono del cliente: ")
        print("Hemos cambiado su telefono , denada CRACK")
    else:
        print("Ese cliente no existe , sorry :(")

def eliminar_cliente(dni, nombre, apellidos, telefono, total):#FUNCION PARA ELIMINAR AL CLIENTE
    eliminar = input("Escribe el DNI del cliente a quien quieres eliminar del listado: ")
    pos = buscar_cliente(dni, total, eliminar)
    if pos != -1:
        i = pos
        while i < total - 1:
            dni[i] = dni[i + 1]
            nombre[i] = nombre[i + 1]
            apellidos[i] = apellidos[i + 1]
            telefono[i] = telefono[i + 1]
            i += 1
        total -= 1
        print("Hemos eliminado al cliente que querias , denada CRACK")
    else:
        print("Ese cliente no existe , sorry :(")
    return total

def guardar_fichero(dni, nombre, apellidos, telefono, total):#FUNCION PARA GUARDAR EL LISTADO DE LOS CLIENTES EN UN .TXT
    try:
        with open("clientes.txt", "w", encoding="utf-8") as f:
            i = 0
            while i < total:
                linea = f"{dni[i]};{nombre[i]};{apellidos[i]};{telefono[i]}\n"
                f.write(linea)
                i += 1
        print("Hemos guardado el listado de los clientes en un archivo llamado clientes.txt")
    except:
        print("No se a podido guardar el archivo , mira por que no se a podido , que yo no se :(")

def cargar_fichero(dni, nombre, apellidos, telefono):#FUNCION PARA CARGAR EL LISTADO DE LOS CLIENTES YA GURDADOS
    total = 0
    try:
        f = open("clientes.txt", "r", encoding="utf-8")
        lineas = f.readlines()
        f.close()
        i = 0
        while i < len(lineas):
            partes = lineas[i].strip().split(";")
            if len(partes) == 4:
                dni[total] = partes[0]
                nombre[total] = partes[1]
                apellidos[total] = partes[2]
                telefono[total] = partes[3]
                total += 1
            i += 1
        print("Hemos cargado el listado de clientes que tenias creado anteriormente en un archivo llamado clientes.txt")
    except:
        print("No tienes ningun archivo del listado de clientes , revisa si se te olvido haberlo guardado la anterior vez que iniciaste este codigo")
    return total
