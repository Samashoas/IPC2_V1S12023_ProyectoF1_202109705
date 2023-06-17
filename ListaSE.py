import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class User:
    def __init__(self, index, rol, nombre, apellido, telefono, correo, contrasena):
        self.index = index
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

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def find_user(self, username, password):
        current = self.head
        while current:
            if current.nombre == username and current.contrasena == password:
                return current
            current = current.next
        return None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

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
        new_user = User(self.get_next_index(),'cliente', nombre, apellido, telefono, correo, contrasena)
        if not self.head:
            self.head = new_user
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_user
    
    def update_user_by_index(self, index, new_data):
        current = self.head

        while current:
            if current.index == index:
                current.nombre = new_data.get('nombre', current.nombre)
                current.apellido = new_data.get('apellido', current.apellido)
                current.telefono = new_data.get('telefono', current.telefono)
                current.correo = new_data.get('correo', current.correo)
                current.contrasena = new_data.get('contrasena', current.contrasena)

                self.update_xml_file()
                return True

            current = current.next

        return False

    def delete_user_by_index(self, index):
        if index < 0 or index >= self.length():
            return False

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            count = 0

            while count < index:
                previous = current
                current = current.next
                count += 1

            previous.next = current.next
            current = None

        self.update_xml_file()  # Update the XML file after deletion
        return True

    def update_xml_file(self):
        root = ET.Element("usuarios")

        current = self.head
        while current:
            user = ET.SubElement(root, "usuario")
            ET.SubElement(user, "rol").text = current.rol
            ET.SubElement(user, "nombre").text = current.nombre
            ET.SubElement(user, "apellido").text = current.apellido
            ET.SubElement(user, "telefono").text = current.telefono
            ET.SubElement(user, "correo").text = current.correo
            ET.SubElement(user, "contrasena").text = current.contrasena

            current = current.next

        tree = ET.ElementTree(root)

        xml_str = ET.tostring(root, encoding="utf-8")

        xml_parsed = minidom.parseString(xml_str)

        pretty_xml = xml_parsed.toprettyxml(indent="  ")

        with open("Usuarios.xml", "w") as file:
            file.write(pretty_xml)

    def is_password_in_use(self, password):
        current = self.head
        while current:
            if current.contrasena == password:
                return True
            current = current.next
        return False
    
    def find_user_by_index(self, index):
        current = self.head
        while current:
            if current.index == index:
                return current
            current = current.next
        return None

    def get_next_index(self):
        current = self.head
        index = 1
        while current:
            current = current.next
            index += 1
        return index

def load_users_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    user_list = LinkedList()

    for index, usuario in enumerate(root.findall('usuario')):
        rol = usuario.find('rol').text
        nombre = usuario.find('nombre').text
        apellido = usuario.find('apellido').text
        telefono = usuario.find('telefono').text
        correo = usuario.find('correo').text
        contrasena = usuario.find('contrasena').text

        user = User(index +1, rol, nombre, apellido, telefono, correo, contrasena)
        user_list.append(user)

    return user_list

