import xml.etree.ElementTree as ET

class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salas = LinkedList()

class Sala:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, sala):
        if self.head is None:
            self.head = sala
            self.tail = sala
        else:
            sala.prev = self.tail
            self.tail.next = sala
            self.tail = sala

def print_cine_data(cine):
    current_sala = cine.salas.head
    while current_sala is not None:
        print("Número de sala:", current_sala.numero)
        print("Número de asientos:", current_sala.asientos)
        print()
        current_sala = current_sala.next

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    cine_element = root.find('cine')
    cine_nombre = cine_element.find('nombre').text
    cine = Cine(cine_nombre)

    salas_element = cine_element.find('salas')
    for sala_element in salas_element.findall('sala'):
        sala_numero = sala_element.find('numero').text
        sala_asientos = int(sala_element.find('asientos').text)
        sala = Sala(sala_numero, sala_asientos)
        cine.salas.append(sala)

    return cine
