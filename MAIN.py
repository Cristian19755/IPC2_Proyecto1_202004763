from tkinter import W, Button, Tk, filedialog
from xml.dom import minidom
import GrafPiso

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
            return
        if op == '3':
            x = int(input('ingrese el piso a graficar'))
            y = int(input('ingrese el patron a graficar'))
            M.graficar_piso(x, y)
            M.menu
        if op == '5':
            exit()
    
    def leerArchivo(self):
        a = self.archivo
        pisos = a.getElementsByTagName('piso')
        patrones = a.getElementsByTagName('patrones')
        R = a.getElementsByTagName('R')
        C = a.getElementsByTagName('C')
        F = a.getElementsByTagName('F')
        S = a.getElementsByTagName('S')
        for elem in pisos:
            nombrePisos = elem.getAttribute('nombre')
            pisosLN.insertar_fin(nombrePisos)
        for elem in R:
            RData= elem.firstChild.data
            RL.insertar_fin(int(RData))
        for elem in C:
            CData= elem.firstChild.data
            CL.insertar_fin(int(CData))
        for elem in F:
            FData= elem.firstChild.data
            FL.insertar_fin(int(FData))
        for elem in S:
            SData= elem.firstChild.data
            SL.insertar_fin(int(SData))
        for elem in patrones:
            patron = elem.getElementsByTagName('patron')
            k = Lista()
            j = Lista()
            for data in patron:
                patronC = data.getAttribute('codigo')
                patronData = data.firstChild.data
                patronData = patronData.replace("\n", "")
                patronData = patronData.replace(" ", "")
                k.insertar_fin(patronC)
                j.insertar_fin(patronData)
            pisosLP.insertar_fin(j)
            pisosLPC.insertar_fin(k)
        print(pisosLN, pisosLPC, pisosLP)

    def optimizacion(self):
        x = patronesL.extraer_dato(1)
        print(x)
    
    def graficar_piso(self, x, y):
        cells = ''
        rows = ''
        contador = 0
        celdaB='''<TD BGCOLOR="WHITE">       </TD>'''
        celdaN='''<TD BGCOLOR="BLACK">       </TD>'''
        nombre = pisosLPC.extraer_dato(x).extraer_dato(y)
        for letra in pisosLP.extraer_dato(x).extraer_dato(y):
            if letra =='w' or letra=='W':
                cells = cells + celdaB
                contador= contador + 1
            elif letra =='b' or letra=='B':
                cells = cells + celdaN
                contador = contador + 1
            if contador == CL.extraer_dato(x):
                rows = rows + '''<TR>''' + cells +'''</TR>'''
                cells = ''
                contador = 0
        GrafPiso.graficar.grafica(rows, nombre)
        M.menu()
        
RL = Lista()
CL = Lista()
SL = Lista()
FL = Lista()
pisosLPC= Lista()
pisosLP = Lista()
pisosLN = Lista()
patronesLC = Lista()
patronesL = Lista()
M = main()
M.menu()
