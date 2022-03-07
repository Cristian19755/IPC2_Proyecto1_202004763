from re import X
from tkinter import W, Button, Pack, Tk, filedialog
from typing import List
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
        contador= 0
        while nodeAux != None:
            contador = contador+1
            nodeAux = nodeAux.siguiente
        return contador

    
class Listas2:
    def remplazar_dato(y, x, dato):
        auxtemp = y
        temp = y.root
        ini= y.cantidad_de_datos()
        
        print(auxtemp)
        for i in range(0,x):
            temp = temp.siguiente
            
        temp.data = dato
        y.root = temp
        fin = y.cantidad_de_datos()
    
        print(auxtemp)
        contador = 0
        while ini != fin:
            z = auxtemp.extraer_dato(contador)
            y.insertar_inicio(z)
            print(List)
            contador = contador+1   
            fin = List.cantidad_de_datos()        

class main:
    def menu(self):
        print("****Seleccione una opcion****\n   1.Cargar Archivo\n   2.Salir")
        op = input()
        if op == '1':
            raiz = Tk()
            myArchivo = filedialog.askopenfilename(title="Abrir Archivo")
            Button(raiz, text= "Abrir Archivo" ).pack
            if myArchivo != None:
                self.archivo = minidom.parse(myArchivo)
                M.leerArchivo()
                print('Archivo Cargado')
                M.menu2()
                raiz.mainloop()
            else: 
                print('Archivo no encontrado')
        if op == '2':
            exit()

    def menu2(self):
        print('****Seleccione un piso****\n  0. Salir')
        for i in range(0,pisosLN.cantidad_de_datos()):
            nombre = pisosLN.extraer_dato(i)
            opcion = '  '+str(i+1)+'. '+nombre
            print(opcion)
        x=int(input())
        if x == 0:
            exit()
        x= x-1
        print('****Seleccione un patron inicial****\n  0. Salir')
        for i in range(0,pisosLPC.extraer_dato(x).cantidad_de_datos()):
            codigo = pisosLPC.extraer_dato(x).extraer_dato(i)
            patron= pisosLP.extraer_dato(x).extraer_dato(i)
            opcion = '  '+str(i+1)+'. '+codigo+': '+patron
            print(opcion)
        y = int (input()) 
        if y == 0:
            exit()
        y = y-1
        codigoin= pisosLPC.extraer_dato(x).extraer_dato(y)
        patronin= pisosLP.extraer_dato(x).extraer_dato(y)
        M.graficar_piso(x,y)
        print('\n----------Grafica generada exitosamente----------\n')
        print('****Seleccione un piso final****\n  0. Salir')
        for i in range(0,pisosLPC.extraer_dato(x).cantidad_de_datos()):
            codigo = pisosLPC.extraer_dato(x).extraer_dato(i)
            patron= pisosLP.extraer_dato(x).extraer_dato(i)
            opcion = '  '+str(i+1)+'. '+codigo+': '+patron
            if i == y:
                print(opcion+'  (patron Inicial)')
            else:
                print(opcion)
        z = int (input()) 
        if z == 0:
            exit()
        z = z-1
        codigofin= pisosLPC.extraer_dato(x).extraer_dato(z)
        patronfin = pisosLP.extraer_dato(x).extraer_dato(z)
        f = FL.extraer_dato(x)
        s = SL.extraer_dato(x)

        
        M.optimizacion(codigoin, codigofin, patronin,patronfin,f,s)
        M.graficar_piso(x,z)
        print('\n----------Grafica generada exitosamente----------\n')
        print('**** Seleccione una opcion ****\n   1.Regresar al menu principal\n   2.Seleccionar otro piso\n   3.Salir')
        opc = int(input())
        if opc == 1 :
            M.menu()
        if opc == 2:
            M.menu2()
        if opc == 3:
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
    def voltear(self, x):
        if x == 'W' or x == 'w':
            return 'B'
        if x == 'B' or x == 'b':
            return 'W'
    
    def optimizacion(self, COD1, COD2, PAT1, PAT2, f, s):
        print('\n:::::::: PASOS '+COD1+' ---> '+COD2+' ::::::::\n')
        contador = 0
        for letra in PAT1:
            PATRON1.insertar_fin(letra)
        for letra in PAT2:
            PATRON2.insertar_fin(letra)
        contador = 0
        PATRONAUX = Lista()

        while contador < PATRON1.cantidad_de_datos():
            if f == s:
                if PATRON1.extraer_dato(contador) != PATRON2.extraer_dato(contador):
                    x = PATRON1.extraer_dato(contador)
                    PATRONAUX.insertar_fin(M.voltear(x))
                    print('se volteo el piso #'+str(contador+1)+':')
                    print(PATRONAUX)
                else: 
                    x = PATRON1.extraer_dato(contador)
                    PATRONAUX.insertar_fin(x)
                    print('se mantuvo el piso #'+str(contador+1)+':')
                    print(PATRONAUX)
            contador = contador +1

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
        
PATRON1 = Lista()
PATRON2 = Lista()      
RL = Lista()
CL = Lista()
SL = Lista()
FL = Lista()
pisosLPC= Lista()
pisosLP = Lista()
pisosLN = Lista()
M = main()
M.menu()