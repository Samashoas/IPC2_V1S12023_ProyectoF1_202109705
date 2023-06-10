import xml.etree.ElementTree as ET
import xml.dom.minidom

class User:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, user):
        if not self.head:
            self.head = user
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = user

    def find_user(self, username, password):
        current = self.head
        while current:
            if current.nombre == username and current.contrasena == password:
                return current
            current = current.next
        return None

    def to_xml(self):
        root = ET.Element("usuarios")
        current = self.head
        while current:
            usuario = ET.SubElement(root, "usuario")
            rol = ET.SubElement(usuario, "rol")
            rol.text = current.rol
            nombre = ET.SubElement(usuario, "nombre")
            nombre.text = current.nombre
            apellido = ET.SubElement(usuario, "apellido")
            apellido.text = current.apellido
            telefono = ET.SubElement(usuario, "telefono")
            telefono.text = current.telefono
            correo = ET.SubElement(usuario, "correo")
            correo.text = current.correo
            contrasena = ET.SubElement(usuario, "contrasena")
            contrasena.text = current.contrasena

            current = current.next

        return root
    
    def register_user(self, nombre, apellido, telefono, correo, contrasena):
        new_user = User('cliente', nombre, apellido, telefono, correo, contrasena)
        if not self.head:
            self.head = new_user
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_user

def load_users_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    user_list = LinkedList()

    for usuario in root.findall('usuario'):
        rol = usuario.find('rol').text
        nombre = usuario.find('nombre').text
        apellido = usuario.find('apellido').text
        telefono = usuario.find('telefono').text
        correo = usuario.find('correo').text
        contrasena = usuario.find('contrasena').text

        user = User(rol, nombre, apellido, telefono, correo, contrasena)
        user_list.append(user)

    return user_list

