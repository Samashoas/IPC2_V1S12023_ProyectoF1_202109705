from colorama import*
from ListaSE import*
from ListaDE import*

users = load_users_from_xml('Usuarios.xml')
filmes = Es_cine('Pelis.xml')
#inicio de sesion
def sesion():

    while True:
        user = input(Fore.BLUE +'Ingrese el Usuario: ')
        pasw = input(Fore.BLUE +'Ingrese su contraseña: ')

        found_user = users.find_user(user, pasw)
        if found_user:
            if found_user.rol == 'admin':
                menuAdmin()
            else:
                menuCliente()
            break
        else:
            print(Fore.WHITE +'Datos incorrectos')

#funciones de cliente
def register_user(users, role):
    print(Fore.WHITE +'ingrese los datos correspondientes del usuario')
    nombre = input(Fore.BLUE +'Nombre: ')
    apellido = input('Apellido: ')
    telefono = input('Numero de telefono: ')
    correo = input('Corrreo electronico: ')

    while True:
        contrasena = input(Fore.BLUE +'contraseña: ')
        passused = False
        for user in users:
            if user.contrasena == contrasena:
                passused = True
                print(Fore.WHITE +'contraseña en uso, ingrese otra')
                break
        if not passused:
            break

    users.register_user(nombre, apellido, telefono, correo, contrasena)
    print(Fore.WHITE +"Usuario registrado!!")

    xml_string = ET.tostring(users.to_xml(), encoding="unicode")
    dom = xml.dom.minidom.parseString(xml_string)
    formatted_xml = dom.toprettyxml(indent="  ")

    with open("Usuarios.xml", "w") as file:
        file.write(formatted_xml)

    if role == 'Admin':
        print(Fore.RED +'Ingresar un nuevo usuario: ')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('|                   1. Si                          *')
        print('|                   2. No                          *')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        while True:
            option = int(input(Fore.GREEN +'Ingrese una opcion: '))
            if option == 1:
                register_user(users)
                break
            elif option == 2:
                gestCliente()
                break
            else:
                print(Fore.WHITE +'opción invalida')
        pass
    else:
        print(Fore.WHITE +'Ya puedes iniciar sesión')
        inicio()
        pass

def modificar_usuario():
    print(Fore.WHITE +'usuarios registrados')
    for user in users:
        if user.rol == 'cliente':
            print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
            print(Fore.WHITE +"---------------------")

    index = int(input(Fore.GREEN +'Ingresa el index del usuario a modificar: '))
    user = users.find_user_by_index(index)
    print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
    print()
    new_data = {}

    new_nombre = input(Fore.BLUE +'Enter the new name (leave empty to keep current): ')
    if new_nombre:
        new_data['nombre'] = new_nombre

    new_apellido = input('Enter the new last name (leave empty to keep current): ')
    if new_apellido:
        new_data['apellido'] = new_apellido

    new_telefono = input('Enter the new phone number (leave empty to keep current): ')
    if new_telefono:
        new_data['telefono'] = new_telefono

    new_correo = input('Enter the new email (leave empty to keep current): ')
    if new_correo:
        new_data['correo'] = new_correo
    
    while True:
        new_contrasena = input('Enter the new password (leave empty to keep current): ')
        if not new_contrasena:
            break
        elif users.is_password_in_use(new_contrasena):
            print(Fore.WHITE +'Password already in use, please enter a different one')
        else:
            new_data['contrasena'] = new_contrasena
            break

    if users.update_user_by_index(index, new_data):
        print(Fore.WHITE +'Cliente modificado exitosamente')
        user = users.find_user_by_index(index)
        print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
        print()
    else:
        print(Fore.WHITE +'Client not found')

    print(Fore.RED +'Modificar otro usuario: ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                   1. Si                          *')
    print('|                   2. No                          *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    while True:
        option = int(input(Fore.GREEN +'Ingrese una opcion: '))
        if option == 1:
            modificar_usuario()
            break
        elif option == 2:
            gestCliente()
            break
        else:
            print(Fore.WHITE +'opción invalida')

def elminar_usuario():
    print(Fore.WHITE +'usuarios registrados')
    for user in users:
        if user.rol == 'cliente':
            print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
            print(Fore.WHITE +"---------------------")
    index = int(input('Ingresa el index del cliente a eliminar: '))

    print('está seguro de eliminar este cliente')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                   1. Si                          *')
    print('|                   2. No                          *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    while True: 
        option = int(input(Fore.GREEN +'ingrese su opción: '))
        if option == 1:
            if users.delete_user_by_index(index):
                print('El cliente fue eliminado exitosamente')
                print(Fore.WHITE +'usuarios registrados')
                for user in users:
                    if user.rol == 'cliente':
                        print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
                        print(Fore.WHITE +"---------------------")
            print(Fore.RED +'Eliminar otro usuario: ')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print('|                   1. Si                          *')
            print('|                   2. No                          *')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            while True:
                option = int(input(Fore.GREEN +'Ingrese una opcion: '))
                if option == 1:
                    elminar_usuario()
                    break
                elif option == 2:
                    gestCliente()
                    break
                else:
                    print(Fore.WHITE +'opción invalida')
            else:
                print('Client not found')
            break
        elif option == 2:
            gestCliente()
            break

def register_peli():
    file_path = 'Pelis.xml'
    nombre = input("Ingrese el nombre de la categoria: ")
    titulo = input("Ingrese el titulo de la pelicula: ")
    director = input("Ingrese el director de la pelicula: ")
    anio = input("ingrese el año de estreno: ")
    fecha = input("Ingrese la fecha de emisison (YYYY-MM-DD): ")
    hora = input("ingrese la hora de funcion: ")

    register_new_movie(file_path, nombre, titulo, director, anio, fecha, hora)

    print(Fore.RED +'Ingresar una nueva pelicula: ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                   1. Si                          *')
    print('|                   2. No                          *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    while True:
        option = int(input(Fore.GREEN +'Ingrese una opcion: '))
        if option == 1:
            register_peli()
            break
        elif option == 2:
            gestPelis()
            break
        else:
            print(Fore.WHITE +'opción invalida')

#Mostrar xml
def ListadoPelis(filmes, role):
    print(Fore.WHITE +'listado de peliculas')
    for row in filmes:
        print(Fore.CYAN + row)
    
    if role == 'Cliente':
        print(Fore.RED +'¿desea regresar al menu principal?')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('|                  Cliente                         *')
        print('|                   1. Si                          *')
        print('|                   2. No                          *')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        while True:
            option = int(input(Fore.GREEN +'seleccione una opción: '))
            if option == 1:
                menuCliente()
                break
            elif option == 2:
                print(Fore.WHITE +'Esperando a que el usuario termine de ver las peliculas')
            else:
                print(Fore.WHITE +'opcion invalida')
        pass
    elif role == 'Admin':
        print(Fore.RED +'¿desea regresar al menu principal?')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('|                   Admin                          *')
        print('|                   1. Si                          *')
        print('|                   2. No                          *')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        while True:
            option = int(input(Fore.GREEN +'seleccione una opción: '))
            if option == 1:
                gestPelis()
                break
            elif option == 2:
                print(Fore.WHITE +'Esperando a que el usuario termine de ver las peliculas')
            else:
                print(Fore.WHITE +'opcion invalida')
        pass
    else:
        print(Fore.WHITE +'Aun no has iniciado sesión')
        inicio()
        pass

def listadoClientes(users):
    print(Fore.WHITE +'usuarios registrados')
    for user in users:
        if user.rol == 'cliente':
            print(Fore.CYAN+ f"[{user.index}].Nombre: {user.nombre}, Apellido: {user.apellido}, Teléfono: {user.telefono}, Correo: {user.correo}")
            print(Fore.WHITE +"---------------------")
    
    print(Fore.RED +'¿desea regresar al menu principal?')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                Administrador                     *')
    print('|                   1. Si                          *')
    print('|                   2. No                          *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    while True:
        option = int(input(Fore.GREEN +'Seleccione una opción: '))
        if option == 1:
            gestCliente()
            break
        elif option == 2:
            print(Fore.WHITE +'Esperando a que el usuario termine de ver los clientes registrados')
        else:
            print(Fore.WHITE +'opcion invalida')

#menus
def gestCliente():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                  Gestion de clientes             *')
    print('|              1. Mostrar clientes                 *')
    print('|              2. Registrar nuevo cliente          *')
    print('|              3. Modificar cliente                *')
    print('|              4. Eliminar cliente                 *')
    print('|              5. Regresar a menu principal        *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    
    while True:
        Option = int(input(Fore.GREEN +'Seleccione una opción: '))
        if Option == 1:
            listadoClientes(users)
            break
        elif Option == 2:
            register_user(users, 'Admin')
            break
        elif Option == 3:
            modificar_usuario()
            break
        elif Option == 4:
            elminar_usuario()
            break
        elif Option == 5:
            menuAdmin()
        else:
            print(Fore.WHITE +'opcion invalida')
            print()

def gestPelis():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                Gestion de Peliculas              *')
    print('|              1. Mostrar Pelicula                 *')
    print('|              2. Registrar nueva Pelicula         *')
    print('|              3. Modificar Pelicula               *')
    print('|              4. Eliminar Pelicula                *')
    print('|              5. Regresar a menu principal        *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    
    while True:
        Option = int(input(Fore.GREEN +'Seleccione una opción: '))
        if Option == 1:
            ListadoPelis(filmes, 'Admin')
            break
        elif Option == 2:
            register_peli()
            break
        elif Option == 3:
            print('modificar pelicula')
            break
        elif Option == 4:
            print('Eliminar pelicula')
        elif Option == 5:
            menuAdmin()
        else:
            print(Fore.WHITE +'opcion invalida')
            print()

def menuAdmin():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                    Gestiones                     *')
    print('|              1. Usuarios                         *')
    print('|              2. Categorias y peliculas           *')
    print('|              3. Salas                            *')
    print('|              4. Compra de Boletos                *')
    print('|              5. Regresar a menu principal        *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

    while True:
        option = int(input(Fore.GREEN +'Seleccione una opción: '))
        if option == 1:
            gestCliente()
            break
        elif option == 2:
            gestPelis()
            break
        elif option == 3:
            print('Gestion de Salas')
            break
        elif option == 4:
            print('Gestion de Boletos')
            break
        elif option == 5:
            inicio()
            break
        else:
            print(Fore.WHITE +'opcion invalida')
            print()

def menuCliente():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                    Bienvenido                    *')
    print('|              1. Listado de Peliculas             *')
    print('|              2. Peliculas favoritas              *')
    print('|              3. Comprar Boletos                  *')
    print('|              4. Historial de compras             *')
    print('|              5. Regresar a menu principal        *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

    while True:
        option = int(input(Fore.GREEN +'Seleccione una opción: '))
        if option == 1:
            ListadoPelis(filmes, 'Cliente')
            break
        elif option == 2:
            print('Peliculas favoritas')
        elif option == 3:
            print('Compra de Boletos')
        elif option == 4:
            print('Historial de compras')
        elif option == 5:
            inicio()
        else:
            print(Fore.WHITE +'ingrese una opción valida')
            print()

def inicio():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                    Binvenido                     *')
    print('|                1. Iniciar Sesión                 *')
    print('|                2. Registrarse                    *')
    print('|                3. Listado de peliculas           *')
    print('|                4. Salir                          *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    while True:
        option = int(input(Fore.GREEN +'Ingrese una opción: ' ))
        if option == 1:
            sesion()
            break
        elif option == 2:
            register_user(users, 'Nuevo usuario')
            break
        elif option == 3:
            ListadoPelis(filmes, 'invitado')
            break
        elif option == 4:
            exit()
        else:
            print(Fore.WHITE +'Opcion invalida')
            print()
inicio()