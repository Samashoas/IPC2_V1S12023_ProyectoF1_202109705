from colorama import*
from ListaSE import*

users = load_users_from_xml('Usuarios.xml')

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

def register_user(users):
    print(Fore.WHITE +'ingrese los datos correspondientes del usuario')
    nombre = input(Fore.BLUE +'Nombre: ')
    apellido = input('Apellido: ')
    telefono = input('Numero de telefono: ')
    correo = input('Corrreo electronico: ')

    while True:
        contrasena = input('contraseña: ')
        passused = False
        for user in users:
            if user.contrasena == contrasena:
                passused = True
                print('contraseña en uso, ingrese otra')
                break
        if not passused:
            break

    users.register_user(nombre, apellido, telefono, correo, contrasena)
    print(Fore.GREEN +"Usuario registrado!!")

    # Update XML file
    xml_string = ET.tostring(users.to_xml(), encoding="unicode")
    dom = xml.dom.minidom.parseString(xml_string)
    formatted_xml = dom.toprettyxml(indent="  ")

    with open("Usuarios.xml", "w") as file:
        file.write(formatted_xml)

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
            inicio()
            break
        else:
            print('opción invalida')

def ListadoPelis():
    print('Trabajando en ello')

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
            print('Gestion de usuarios')
            break
        elif option == 2:
            print('Gestion de pelis')
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
            print('opcion invalida')
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
            print('Listado de Peliculas')
        elif option == 2:
            print('Peliculas favoritas')
        elif option == 3:
            print('Compra de Boletos')
        elif option == 4:
            print('Historial de compras')
        elif option == 5:
            inicio()
        else:
            print('ingrese una opción valida')
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
            register_user(users)
            break
        elif option == 3:
            ListadoPelis()
            break
        elif option == 4:
            exit()
        else:
            print('Opcion invalida')
            print()
inicio()