from tkinter import W, Button, Tk, filedialog
from xml.dom import minidom
from graphviz import Digraph

class node:
    def __init__(self, data = None, siguiente = None):
        self.data = data 
        self.siguiente = siguiente

class Lista: 
    def __init__(self):
        self.root = None

    def insertar_inicio(self, data):
        self.root = node(data=data, siguiente=self.root) 

    def insertar_fin(self, midato): 

        if self.root is None: 
            self.root = node(data=midato) 
            return 
        auxRoot = self.root
        while auxRoot.siguiente: 
            auxRoot = auxRoot.siguiente
        auxRoot.siguiente = node(data=midato)
    
    def imprimir_lista( self ):
        nodeAux = self.root 
        while nodeAux != None:
            print(nodeAux.data)
            nodeAux = nodeAux.siguiente

    def extraer_dato(self, x):
        auxRoot = self.root
        for i in range(0,x):
            auxRoot = auxRoot.siguiente
        return auxRoot.data

    def __str__(self):
        Cadena = "["
        auxRoot = self.root
        for i in range(self.cantidad_de_datos()):
            Cadena += str(auxRoot.data)
            if i != self.cantidad_de_datos()-1:
                    Cadena += str(", ")
            auxRoot = auxRoot.siguiente
        Cadena +="]"
        return Cadena

    def cantidad_de_datos(self):
        nodeAux = self.root 
        contador=0
        while nodeAux != None:
            contador = contador+1
            nodeAux = nodeAux.siguiente
        return contador
        
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
            patronesL.imprimir_listaD()
            patronesLC.imprimir_listaD()
            exit()

        if op == '3':
            M.graficar()
            M.menu
        if op == '5':
            exit()
    
    def leerArchivo(self):
        a = self.archivo
        pisos = a.getElementsByTagName('piso')
        patrones = a.getElementsByTagName('patrones')
        self.R = a.getElementsByTagName('R')
        self.C = a.getElementsByTagName('C')
        self.F = a.getElementsByTagName('F')
        self.S = a.getElementsByTagName('S')

        for elem in pisos:
            nombrePisos = elem.getAttribute('nombre')
            pisosLN.insertar_final(nombrePisos)
        for elem in pisos:
            for elem in patrones:
                codigoPatrones = elem.getAttribute('codigo')
                patronesLC.insertar_final(codigoPatrones)
            for elem in patrones:
                patron = elem.firstChild.data
                patronesL.insertar_final(patron)
                print()
            pisosLP.insertar_final(patronesL.root.elemento)
            pisosLPC.insertar_final(patronesLC.root.elemento)
        pisosLP.imprimir_listaD()

    def optimizacion(self):
        x = patronesL.extraer_dato(1)
        print(x)
    
    def graficar(self):
        cells = ''
        rows = ''
        contador = 0
        for i in range(0,int(self.R)):

            while contador < int(self.C):
                if pisosLP.root.elemento()=='w' or pisosLP.root.elemento()=='W':
                    cells = cells + '<TD BGCOLOR="WHITE">       </TD>'
                    pisosLP.eliminar_inicio()
                    contador = contador+1
                elif pisosLP.root.elemento()=='b' or pisosLP.root.elemento()=='B':
                    cells = cells + '<TD BGCOLOR="WHITE">       </TD>'
                    contador = contador+1
                    pisosLP.eliminar_inicio()
                else:
                    contador = contador 
                    pisosLP.eliminar_inicio()
            rows = rows + '<TR>' + cells +'</TR>'
            i = i
            print(rows)

        h = Digraph('g', filename='btree.gv',
                     node_attr={'shape': 'record', 'height': '.1'})
        

        
pisosLPC= Lista()
pisosLP = Lista()
pisosLN = Lista()
patronesLC = Lista()
patronesL = Lista()
M = main()
M.menu()
