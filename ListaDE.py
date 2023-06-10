import xml.etree.ElementTree as ET

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev

            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while True:
                print(current.data)
                current = current.next
                if current == self.head:
                    break
            print()

# Parse the XML file and populate the doubly circular linked list
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    peli = DoublyCircularLinkedList()

    for categoria in root.findall('categoria'):
        nombre = categoria.find('nombre').text
        peli.insert(nombre)

        peliculas = categoria.find('peliculas')
        for pelicula in peliculas.findall('pelicula'):
            titulo = pelicula.find('titulo').text
            director = pelicula.find('director').text
            pelicula_data = f"Titulo: {titulo}\nDirector: {director}"
            peli.insert(pelicula_data)

    return peli
