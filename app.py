import utiles

MAX = 100
dni = [""] * MAX
nombre = [""] * MAX
apellidos = [""] * MAX
telefono = [""] * MAX
total = 0
opcion = 0

#Creacion de la tabla
while opcion != 8:
    print("\n--- Gestor de clientes ---")
    print("1. Alta de cliente")
    print("2. Listar todos los clientes")
    print("3. Buscar cliente por DNI")
    print("4. Modificar teléfono de un cliente")
    print("5. Eliminar cliente")
    print("6. Guardar clientes en fichero")
    print("7. Cargar clientes desde fichero")
    print("8. Salir")
    opcion = int(input("Escribe el numero de la opcion que quieras eleguir: "))
    if opcion == 1:
        total = utiles.alta_cliente(dni, nombre, apellidos, telefono, total, MAX)
    if opcion == 2:
        utiles.listar_clientes(dni, nombre, apellidos, telefono, total)
    if opcion == 3:
        utiles.buscar_por_dni(dni, nombre, apellidos, telefono, total)
    if opcion == 4:
        utiles.modificar_telefono(dni, telefono, total)
    if opcion == 5:
        total = utiles.eliminar_cliente(dni, nombre, apellidos, telefono, total)
    if opcion == 6:
        utiles.guardar_fichero(dni, nombre, apellidos, telefono, total)
    if opcion == 7:
        total = utiles.cargar_fichero(dni, nombre, apellidos, telefono)
print("Bye Bye : D")
