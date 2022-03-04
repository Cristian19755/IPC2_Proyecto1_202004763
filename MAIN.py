from tkinter import Button, Tk, filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET
from Nodo import Nodo
import graphviz
class Lista:
    def __init__(self):
        self.root = None

    def insertar_lista_vacia(self, dato):
        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
        else:
            print("La lista no esta vacia")
    
    def insertar_inicio(self, dato):

        if self.root is None:
            self.insertar_lista_vacia(dato)
        else:
            nuevoNodo = Nodo(dato)
            nuevoNodo.siguiente = self.root
            self.root.anterior = nuevoNodo
            self.root = nuevoNodo
    
    def insertar_final(self, dato):

        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
            return
        
        apuntador = self.root

        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente

        nuevoNodo = Nodo(dato)
        apuntador.siguiente = nuevoNodo
        nuevoNodo.anterior = apuntador
    
    def insertar_despues_elemento(self, x, dato):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:

                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo(dato)
                nuevoNodo.anterior = apuntador
                nuevoNodo.siguiente = apuntador.siguiente
                if apuntador.siguiente is not None:
                    apuntador.siguiente.anterior = nuevoNodo
                apuntador.siguiente = nuevoNodo
    
    def insertar_antes_elemento(self, x, dato):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("Elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo(dato)
                nuevoNodo.siguiente = apuntador
                nuevoNodo.anterior = apuntador.anterior

                if apuntador.anterior is not None:
                    apuntador.anterior.siguiente = nuevoNodo
                apuntador.anterior = nuevoNodo

    def imprimir_listaD(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento, " ")
                apuntador = apuntador.siguiente

    def lista_vacia(self):
        if self.root is None:
            return True
        else:
            return False
    
    def contar_elementos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta
    
    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None

        self.root = self.root.siguiente
        self.root.anterior = None
    
    def eliminar_final(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None
            return

        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        apuntador.anterior.siguiente = None
    
    def eliminar_elemento(self, x):
        if self.root is None:
            print("La lista esta vacia")
            return
        
        if self.root.siguiente is None:
            if self.root.elemento == x:
                self.root = None
            else:
                print("Elemento no encontrado")
        
        if self.root.elemento == x:
            self.eliminar_inicio()
            return
        
        apuntador = self.root
        while apuntador.siguiente is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        
        if apuntador.siguiente is not None:
            apuntador.anterior.siguiente = apuntador.siguiente
            apuntador.siguiente.anterior = apuntador.anterior
        else:
            if apuntador.elemento == x:
                self.eliminar_final()
            else:
                return print("Elemento no encontrado")
                
class main:
    def menu(self):
        print("****Seleccione una opcion****\n1.Cargar Archivo\n2.Mostrar Patron\n3.Cambiar Patron\n4.Mostrar pisos cargados\n5.Salir")
        op = input()
        if op == '1':
            raiz = Tk()
            myArchivo = filedialog.askopenfilename(title="Abrir Archivo")
            Button(raiz, text= "Abrir Archivo" ).pack
            if myArchivo != None:
                self.archivo = minidom.parse(myArchivo)
                M.leerArchivo()
                print('Archivo Cargado')
                M.menu()
                raiz.mainloop()
            else: 
                print('Archivo no encontrado')
        if op == '2':
            print(self.archivo)
        if op == '3':
            M.optimizacion()
            M.menu
        if op == '5':
            exit()
    
    def leerArchivo(self):
        a = self.archivo
        pisos = a.getElementsByTagName('piso')
        patrones = a.getElementsByTagName('patron')
        self.R = a.getElementsByTagName('R')
        self.C = a.getElementsByTagName('C')
        self.F = a.getElementsByTagName('F')
        self.S = a.getElementsByTagName('S')
        
        for elem in pisos:
            nombrePisos = elem.getAttribute('nombre')
            pisosL.insertar_final(nombrePisos)

        for elem in patrones:
            codigoPatrones = elem.getAttribute('codigo')
            patronesLC.insertar_final(codigoPatrones)
        for elem in patrones:
            patron = elem.firstChild.data
            patronesL.insertar_final(patron)

    def optimizacion(self):
        x = patronesL.extraer_dato(1)
        print(x)
    
    def graficar():
        g = graphviz.Graph('G', filename='g_c_n.gv')
        g.attr(bgcolor='purple:pink', label='Piso01', fontcolor='white')

        with g.subgraph(name='cluster1') as c:
            c.attr(fillcolor='blue:cyan', label='', fontcolor='white',
                style='filled', gradientangle='270')
            c.attr('node', shape='box', fillcolor='Black',
                style='filled')
            c.node('1')
            c.attr('node', shape='box', fillcolor='white',
                style='filled')
            c.node('2')
            c.node('5t')
            c.node('22')
            c.node('9')
            c.node('8')
            c.node('7')
            c.node('6')

        with g.subgraph(name='cluster2') as d:
            d.attr(fillcolor='blue:cyan', label='', fontcolor='white',
                style='filled', gradientangle='270')
            d.attr('node', shape='box', fillcolor='Black',
                style='filled')
            d.node('3')
            d.attr('node', shape='box', fillcolor='white',
                style='filled')
            d.node('4')
        g.view()

pisosL = Lista()
patronesLC = Lista()
patronesL = Lista()
M = main()
M.menu()
