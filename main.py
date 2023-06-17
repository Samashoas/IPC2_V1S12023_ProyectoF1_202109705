from colorama import*
from ListaSE import*
from ListaDE import*

users = load_users_from_xml('Usuarios.xml')
filmes = Es_cine('Pelis.xml')

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
            menuAdmin()
            break
        elif option == 2:
            print(Fore.WHITE +'Esperando a que el usuario termine de ver los clientes registrados')
        else:
            print(Fore.WHITE +'opcion invalida')

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
            print('modificar cliente')
            break
        elif Option == 4:
            print('Eliminar cliente')
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
            print('Mostrar Pelicula')
            break
        elif Option == 2:
            print('Ingresar pelicula')
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