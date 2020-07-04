from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os.path as path
import json
Nombre = ""
Ansiedad = {}
Depresion= {}
TOC = {}
Bipolar = {}
Esquizofrenia = {}
Significado = {}
listaAnsiedad = []
ProbAnsiedad = 0.0
listaDepresion = []
ProbDepresion = 0.0
listaTOC = []
ProbTOC = 0.0
listaBipolar = []
ProbBipolar = 0.0
listaEsq = []
ProbEsq = 0.0
with open("Ansiedad.json", 'r') as jsonTrastorno:
    Ansiedad = json.load(jsonTrastorno)
with open("Depresion.json", 'r') as jsonTrastorno:
    Depresion = json.load(jsonTrastorno)
with open("TOC.json", 'r') as jsonTrastorno:
    TOC = json.load(jsonTrastorno)
with open("Bipolar.json", 'r') as jsonTrastorno:
    Bipolar = json.load(jsonTrastorno)
with open("Esquizofrenia.json", 'r') as jsonTrastorno:
    Esquizofrenia = json.load(jsonTrastorno)
with open("Significado.json", 'r') as jsonSignificado:
    Significado = json.load(jsonSignificado)

#Ventana consulta
def vConsulta():
    vConsulta = Toplevel()
    txtbBusqueda = Entry(vConsulta)
    txtbBusqueda.grid(row=0, column=0)
    btnBusqueda = ttk.Button(vConsulta, text='Buscar', command=lambda:Buscar(txtbBusqueda.get()))
    btnBusqueda.grid(row=0, column=1)
    btnLista = ttk.Button(vConsulta, text='Lista', command=ListaP)
    btnLista.grid(row=1, column=1)
#Buscar
def Buscar (Name):
    if path.exists(Name.replace(" ","_")+'.txt'):
        path.os.system(Name.replace(" ","_")+'.txt')
    else:
        messagebox.showerror(message='No se encontró al paciente')
#Lista
def ListaP():
    def CurSelect(event):
#        value = str((lstPacientes.curselection()))
        value = lstPacientes.get(ANCHOR)
        path.os.system(value.replace(" ","_")+".txt")
        Lista.destroy()
    Contenido = path.os.listdir(path.os.getcwd())
    Pacientes = []
    for fichero in Contenido:
        if path.os.path.isfile(path.os.path.join(path.os.getcwd(),fichero)) and fichero.endswith('.txt'):
            f = fichero.rstrip('.txt')
            f=f.replace("_"," ")
            Pacientes.append(f)
    Lista = Toplevel()
    Lista.title('Pacientes')
    lstPacientes = Listbox(Lista, width=40)
    lstPacientes.see(30)
    lstPacientes.bind('<<ListboxSelect>>',CurSelect)

    lstPacientes.pack()
    lstPacientes.insert(0, *Pacientes)

#Ventana paciente
def newvPaciente():
    def GuardarPaciente():
        global Nombre
        Nombre = txtbPaciente.get()
        Nombre = Nombre.replace(" ","_")
        Paciente = open(Nombre + '.txt','w')
        Paciente.write("Nombre: " + txtbPaciente.get()  + path.os.linesep)
        Paciente.write("Edad: " + txtbEdad.get()  + path.os.linesep)
        Paciente.write("Datos generales:" + path.os.linesep + txtbGeneral.get("1.0", END) + path.os.linesep)
        Paciente.close()
        btnCriterios.config(state=NORMAL)
    global vPaciente
    vPaciente = Toplevel()
    vPaciente.resizable(False,False)
    vPaciente.title('ADTM')

    lblPaciente = Label(vPaciente, text = "Nombre")
    lblPaciente.grid(row = 0, column = 0, sticky = W, pady = 2)
    txtbPaciente = Entry(vPaciente)
    txtbPaciente.grid(row = 0, column = 1, sticky = W, pady = 2, ipadx=50)

    lblEdad = Label(vPaciente, text = "Edad")
    lblEdad.grid(row = 1, column = 0, sticky = W, pady = 2)
    txtbEdad = Entry(vPaciente)
    txtbEdad.grid(row = 1, column = 1, sticky = W)

    lblGeneral = Label(vPaciente, text= "Datos generales\ndel paciente")
    lblGeneral.grid(row = 2, column = 0, sticky = W, pady = 2)
    txtbGeneral = Text(vPaciente)
    txtbGeneral.grid(row = 2, column = 1, ipadx=2)

    btnSalir = ttk.Button(vPaciente, text="Salir", command = vPaciente.destroy)
    btnSalir.grid(row=3, column=0)

    btnGuardar = ttk.Button(vPaciente, text="Guardar", command = GuardarPaciente)
    btnGuardar.grid(row=3, column=1, sticky = W)

    btnCriterios = ttk.Button(vPaciente, text="Siguiente", command = newvCriterios)
    btnCriterios.grid(row = 3, column = 2, sticky = W, pady = 2)
    btnCriterios['state'] = DISABLED

#Ventana de seleccion de criterios
def newvCriterios ():

    global vCriterios
    vCriterios = Toplevel()
    vCriterios.title("Criterios")
    vCriterios.resizable(False,False)
    vPaciente.withdraw()
    try:
        vCriterios2.destroy()
    except:
        pass
    
    global boolFatiga
    boolFatiga = BooleanVar()
    chkFatiga = Checkbutton(vCriterios, text="Fatiga", variable=boolFatiga)
    chkFatiga.grid(row=0, column=0, sticky="w")

    global boolSueno
    boolSueno = BooleanVar()
    chkSueno = Checkbutton(vCriterios, text="Insomnio o hipersomnia", variable=boolSueno)
    chkSueno.grid(row=1, column=0, sticky="w")

    global boolConcentracion
    boolConcentracion = BooleanVar()
    chkConcentracion = Checkbutton(vCriterios, text="Falta de concentración", variable=boolConcentracion)
    chkConcentracion.grid(row=2, column=0, sticky="w")

    global boolDetSocial
    boolDetSocial = BooleanVar()
    chkDetSocial = Checkbutton(vCriterios, text="Deterioro social", variable=boolDetSocial)
    chkDetSocial.grid(row=3, column=0, sticky="w")

    global boolPlacer
    boolPlacer = BooleanVar()
    chkPlacer = Checkbutton(vCriterios, text="Falta de iniciativa o placer", variable=boolPlacer)
    chkPlacer.grid(row=4, column=0, sticky="w")

    def Volver():
        vCriterios.destroy()
        vPaciente.destroy()
    
    btnRegresar = ttk.Button(vCriterios, text="Regresar", command=Volver)
    btnRegresar.grid(row=7, column=0)
    
    btnCriterios2 = ttk.Button(vCriterios, text="Siguiente", command=newvCriterios2)
    btnCriterios2.grid(row=7, column=1, sticky=W)


#Segunda pagina ventana criterios
def newvCriterios2():
    vCriterios.destroy()
    global listaCriterios
    listaCriterios = []
    if boolFatiga.get():
        listaCriterios.append("Fatiga")
    if boolSueno.get():
        listaCriterios.append("Insomnio")
    if boolConcentracion.get():
        listaCriterios.append("NoConcentracion")
    if boolDetSocial.get():
        listaCriterios.append("DeterioroSocial")
    if boolPlacer.get():
        listaCriterios.append("NoPlacer")
    
    global vCriterios2
    vCriterios2 = Toplevel()
    vCriterios2.title("Criterios - 2")
    vCriterios2.resizable(False,False)

    global Preocupacion
    Preocupacion = BooleanVar()
    chkPreocupacion = Checkbutton(vCriterios2, text='Preocupación excesiva', variable=Preocupacion)
    chkPreocupacion.grid(row=0, column=0, sticky=W)

    global Peso
    Peso = BooleanVar()
    chkPeso = Checkbutton(vCriterios2, text='Perdida o aumento significativo de peso', variable=Peso)
    chkPeso.grid(row=1, column=0, sticky=W)

    global Ob
    Ob = BooleanVar()
    chkObsesiones = Checkbutton(vCriterios2, text='Presencia de obsesiones', variable=Ob)
    chkObsesiones.grid(row=2, column=0, sticky=W)

    global Compul
    Compul = BooleanVar()
    chkCompulsiones = Checkbutton(vCriterios2, text='Presencia de compulsiones', variable=Compul)
    chkCompulsiones.grid(row=3, column=0, sticky=W)

    global Man
    Man = BooleanVar()
    chkM = Checkbutton(vCriterios2, text='Se ha presentado un episodio maníaco', variable=Man)
    chkM.grid(row=4, column=0, sticky=W)

    global Delirio
    Delirio = BooleanVar()
    chkDelirio = Checkbutton(vCriterios2, text='Presencia de delirio', variable=Delirio)
    chkDelirio.grid(row=5, column=0, sticky=W)

    btnCriterios3 = ttk.Button(vCriterios2, text='Siguiente', command=newvCriterios3)
    btnCriterios3.grid(row=6, column=1)

    btnAtras = ttk.Button(vCriterios2, text='Atrás', command=newvCriterios)
    btnAtras.grid(row=6, column=0)

#Criterios pagina 3
def newvCriterios3():
    if Preocupacion.get():
        listaCriterios.append('Preocupacion')
    if Peso.get():
        listaCriterios.append('Peso')
    if Ob.get():#acuerdate de multiplicar la proporcion
        listaCriterios.append('Ob')
    if Compul.get():
        listaCriterios.append('Compul')
    if Ob.get() and Compul.get():
        listaCriterios.append('ObComp')
    if not Man.get():
        listaCriterios.append('NoM')
    if Delirio.get():
        listaCriterios.append('Delirios')
######################################################
    for Comp in listaCriterios:
        if Comp in Ansiedad.keys():
            listaAnsiedad.append(Ansiedad['ProbInd']*Ansiedad[Comp]['ProbCond']/Ansiedad[Comp]['ProbInd'])
#            listaProbAnsiedad.append(listaAnsiedad)
        if Comp in Depresion.keys():
            listaDepresion.append(Depresion['ProbInd']*Depresion[Comp]['ProbCond']/Depresion[Comp]['ProbInd'])
#            listaProbDepresion.append(listaDepresion)
        if Comp in TOC.keys():
            listaTOC.append(TOC['ProbInd']*TOC[Comp]['ProbCond']/TOC[Comp]['ProbInd'])
#            listaProbTOC.append(listaTOC)
        if Comp in Bipolar.keys():
            listaBipolar.append(Bipolar['ProbInd']*Bipolar[Comp]['ProbCond']/Bipolar[Comp]['ProbInd'])
#            listaProbBipolar.append(listaBipolar)
        if Comp in Esquizofrenia.keys():
            listaEsq.append(Esquizofrenia['ProbInd']*Esquizofrenia[Comp]['ProbCond']/Esquizofrenia[Comp]['ProbInd'])
#            listaProbEsq.append(listaEsq)
    print(listaAnsiedad)
    print(listaDepresion)
    print(listaTOC)
    print(listaBipolar)
    print(listaEsq)
    print("\n")
    ProbAnsiedad = 0
    ProbDepresion = 0
    ProbTOC = 0
    ProbBipolar = 0
    ProbEsq = 0
    for Elemento in listaAnsiedad:
        ProbAnsiedad = ProbAnsiedad + Elemento
    for Elemento in listaDepresion:
        ProbDepresion = ProbDepresion + Elemento
    for Elemento in listaTOC:
        ProbTOC = ProbTOC + Elemento
    for Elemento in listaBipolar:
        ProbBipolar = ProbBipolar + Elemento
    for Elemento in listaEsq:
        ProbEsq = ProbEsq + Elemento
######################################################
    global vCriterios3
    vCriterios3 = Toplevel()
    vCriterios3.title('Criterios - 3')
    vCriterios3.resizable(False,False)
    vCriterios2.withdraw()
    global OCTiempo
    OCTiempo = BooleanVar()
    global Tics
    Tics = BooleanVar()
    global Introspeccion
    Introspeccion = BooleanVar()

    global H
    H = BooleanVar()
    global Dep
    Dep = BooleanVar()
    global Anos
    Anos = BooleanVar()

    global Aluc
    Aluc = BooleanVar()
    global DD
    DD = BooleanVar()
    global CD
    CD = BooleanVar()
    global AB
    AB = BooleanVar()
    global DL
    DL = BooleanVar()
    global Autismo
    Autismo = BooleanVar()

    #depresion
    global RetMot
    RetMot = BooleanVar()
    global Culpa
    Culpa = BooleanVar()
    global Muerte
    Muerte = BooleanVar()
    
    #Ansiedad
    global ControlP
    ControlP = BooleanVar()
    global Inquietud
    Inquietud = BooleanVar()
    global Irritabilidad
    Irritabilidad = BooleanVar()
    global TMuscular
    TMuscular = BooleanVar()
######################################################
    if ProbTOC > ProbAnsiedad and ProbBipolar > ProbAnsiedad:
        #descarta ansiedad y depresion
        if ProbTOC > ProbDepresion and ProbBipolar > ProbDepresion and ProbEsq > ProbAnsiedad and ProbEsq > ProbDepresion:
            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=0, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=1, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=2, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')
            
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=3, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
                chkDep.grid(row=11, column=0, sticky=W)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=4, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')
            
            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=5, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=6, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=7, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=8, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=9, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=10,column=0, sticky=W)
        #descarta ansiedad y esquizofrenia
        if ProbDepresion > ProbAnsiedad and ProbDepresion > ProbEsq and ProbTOC > ProbEsq and ProbBipolar > ProbEsq:
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=1, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=2, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=3, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=4, column=0, sticky=W)  

            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=5, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=6, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=7, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=8, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')
            
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=9, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=10, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')

    if ProbTOC > ProbBipolar and ProbEsq > ProbBipolar:
        #descarta ansiedad y bipolar
        if ProbDepresion > ProbAnsiedad and ProbDepresion > ProbBipolar and ProbTOC > ProbAnsiedad and ProbEsq > ProbAnsiedad:
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=0, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=1, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=2, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=3, column=0, sticky=W)  

            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=4, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            
            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=5, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=6, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=7, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')

            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=8, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=9, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=10, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=11, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=12, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=13,column=0, sticky=W)

        #descarta depresion y bipolar
        if ProbAnsiedad > ProbDepresion and ProbAnsiedad > ProbBipolar and ProbTOC > ProbDepresion and ProbEsq > ProbDepresion:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)

            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')

            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=4, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=5, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=6, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')
            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=7, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=8, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=9, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=10, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=11, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=12,column=0, sticky=W)
    if ProbDepresion > ProbTOC and ProbEsq > ProbTOC:
        #descarta ansiedad y toc
        if ProbDepresion > ProbAnsiedad and ProbBipolar > ProbAnsiedad and ProbBipolar > ProbTOC and ProbEsq > ProbAnsiedad:
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=0, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=1, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=2, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=3, column=0, sticky=W)  

            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=4, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=5, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=6, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')
            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=7, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=8, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=9, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=10, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=11, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=12,column=0, sticky=W)
        #descarta toc y bipolar
        if ProbAnsiedad > ProbTOC and ProbAnsiedad > ProbBipolar and ProbDepresion > ProbBipolar and ProbEsq > ProbBipolar:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)

            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=4, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=5, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=6, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=7, column=0, sticky=W)  

            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=8, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=9, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=10, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=11, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=12, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=13, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=13, column=0, sticky=W)
    if ProbAnsiedad > ProbDepresion and ProbBipolar > ProbDepresion:
        #descarta depresion y toc
        if ProbAnsiedad > ProbTOC and ProbBipolar > ProbTOC and ProbEsq > ProbDepresion and ProbEsq > ProbTOC:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)

            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=4, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
                chkDep.grid(row=5, column=0, sticky=W)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=6, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')
            #Esquizofrenia
            chkAluc = Checkbutton(vCriterios3, text='Presencia de alucionaciones', variable=Aluc)
            chkAluc.grid(row=7, column=0, sticky=W)

            chkDD = Checkbutton(vCriterios3, text='Discurso desorganizado', variable=DD)
            chkDD.grid(row=8, column=0, sticky=W)

            chkCD = Checkbutton(vCriterios3, text='Comportamiento desorganizado', variable=CD)
            chkCD.grid(row=9, column=0, sticky=W)

            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=10, column=0, sticky=W)

            chkDL = Checkbutton(vCriterios3, text='Deterioro laboral', variable=DL)
            chkDL.grid(row=11, column=0, sticky=W)

            chkAutismo = Checkbutton(vCriterios3, text='Sospecha de autismo', variable=Autismo)
            chkAutismo.grid(row=12, column=0, sticky=W)
        #descarta depresión y esquizofrenia
        if ProbAnsiedad > ProbEsq and ProbTOC > ProbDepresion and ProbTOC > ProbEsq and ProbBipolar > ProbEsq:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)
            
            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=4, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
                chkDep.grid(row=5, column=0, sticky=W)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=6, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')
            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=7, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=8, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=9, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')
    if ProbAnsiedad > ProbEsq and ProbDepresion > ProbEsq:
        #descarta toc y esquizofrenia
        if ProbAnsiedad > ProbTOC and ProbDepresion > ProbTOC and ProbBipolar > ProbTOC and ProbBipolar > ProbEsq:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)

            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=4, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=5, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=6, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=7, column=0, sticky=W)  

#            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
#            chkH.grid(row=8, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            #Bipolar
            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=9, column=0, sticky=W)

            if ProbDepresion > 0.1:
                listaTOC.append(0.3)
                chkDep = Checkbutton(vCriterios3, text='Episodios depresivos presentes la mitad del tiempo del malestar', variable=Dep)
            
            chk2anos = Checkbutton(vCriterios3, text='Los malestares han estado presentes durante al menos dos años', variable=Anos)
            chk2anos.grid(row=10, column=0, sticky=W)

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por esquizofrenia')
        #descarta bipolar y esquizofrenia
        if ProbAnsiedad > ProbBipolar and ProbDepresion > ProbBipolar and ProbTOC > ProbBipolar and ProbTOC  > ProbEsq:
            #Ansiedad
            chkControlP = Checkbutton(vCriterios3, text='Resulta difícil controlar la preocupación', variable=ControlP)
            chkControlP.grid(row=0, column=0, sticky=W)

            chkInquietud = Checkbutton(vCriterios3, text='Inquietud', variable=Inquietud)
            chkInquietud.grid(row=1, column=0, sticky=W)

            chkIrritabilidad = Checkbutton(vCriterios3, text='Irritabilidad', variable=Irritabilidad)
            chkIrritabilidad.grid(row=2, column=0, sticky=W)

            chkTMuscular = Checkbutton(vCriterios3, text='Tensión muscular', variable=TMuscular)
            chkTMuscular.grid(row=3, column=0, sticky=W)

            if ProbTOC > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por TOC')
            #Depresion
            chkAB = Checkbutton(vCriterios3, text='Expresión emotiva disminuida', variable=AB)
            chkAB.grid(row=4, column=0, sticky=W) 

            chkRetMot = Checkbutton(vCriterios3, text='Retraso motor', variable=RetMot)  
            chkRetMot.grid(row=5, column=0, sticky=W)

            chkCulpa = Checkbutton(vCriterios3, text='Sentimiento de culpabilidad excesiva', variable=Culpa)
            chkCulpa.grid(row=6, column=0, sticky=W)

            chkMuerte = Checkbutton(vCriterios3, text='Pensamiento de muerte', variable=Muerte) 
            chkMuerte.grid(row=7, column=0, sticky=W)  

            chkH = Checkbutton(vCriterios3,text='Se ha presentado un episodio hipomaniaco', variable=H)
            chkH.grid(row=8, column=0, sticky=W)   

            if ProbEsq > 0.2:
                messagebox.showinfo(message='Tal vez se explica mejor por esquizofrenia')
            #TOC
            if Ob.get() or Compul.get():
                chkOCTiempo = Checkbutton(vCriterios3, text='Las obsesiones o compulsiones requiere mucho tiempo', variable=OCTiempo)
                chkOCTiempo.grid(row=9, column=0, sticky=W)
            
            chkTics = Checkbutton(vCriterios3,text='Existe un diagnóstico previo de tics', variable=Tics)
            chkTics.grid(row=10, column=0,sticky=W)

            chkIntrospeccion = Checkbutton(vCriterios3,text='Está consciente de las obsesiones y/o compulsiones',variable=Introspeccion)
            chkIntrospeccion.grid(row=11, column=0, sticky=W)

            if ProbAnsiedad > 0.2:
                messagebox.showinfo(message='Tal vez se explique mejor por ansiedad')
            
    btnDiagnostico = ttk.Button(vCriterios3,text='Diagnostico', command=newvDiagnostico)
    btnDiagnostico.grid(row=15, column=2, sticky=E)
######################################################

#Ventana de diagnostico
def newvDiagnostico():
#    Diagnostico = Toplevel()
    vCriterios.destroy()
    vCriterios2.destroy()
    vCriterios3.destroy()
#    Diagnostico.title('Diagnóstico')
    if ControlP.get():
        listaCriterios.append('NoControlP')
    if Inquietud.get():
        listaCriterios.append('Inquietud')
    if Irritabilidad.get():
        listaCriterios.append('Irritabilidad')
    if TMuscular.get():
        listaCriterios.append('TensionM')
    if RetMot.get():
        listaCriterios.append('Motor')
    if Culpa.get():
        listaCriterios.append('Culpabilidad')
    if Muerte.get():
        listaCriterios.append('PMuerte')
    if Aluc.get():
        listaCriterios.append('Alucionaciones')
    if DD.get():
        listaCriterios.append('DiscursoDesorg')
    if CD.get():
        listaCriterios.append('ComportamientoDesorg')
    if AB.get():
        listaCriterios.append('AnimoBajo')
    if DL.get():
        listaCriterios.append('DeterioroLaboral')
    if Autismo.get():
        listaCriterios.append('Autismo')
    if H.get():
        listaCriterios.append('H')
    if Dep.get():
        listaCriterios.append('SiDepresion')
    if Anos.get():
        listaCriterios.append('2Anos')
    if OCTiempo.get():
        listaCriterios.append('OCTiempo')
    if Tics.get():
        listaCriterios.append('Tics')
    if Introspeccion.get():
        listaCriterios.append('Introspeccion')

    listaAnsiedad = []
    listaDepresion = []
    listaTOC = []
    listaBipolar = []
    listaEsq = []
    for Comp in listaCriterios:
        if Comp in Ansiedad.keys():
            listaAnsiedad.append(Ansiedad['ProbInd']*Ansiedad[Comp]['ProbCond']/Ansiedad[Comp]['ProbInd'])
#            listaProbAnsiedad.append(listaAnsiedad)
        if Comp in Depresion.keys():
            listaDepresion.append(Depresion['ProbInd']*Depresion[Comp]['ProbCond']/Depresion[Comp]['ProbInd'])
#            listaProbDepresion.append(listaDepresion)
        if Comp in TOC.keys():
            listaTOC.append(TOC['ProbInd']*TOC[Comp]['ProbCond']/TOC[Comp]['ProbInd'])
#            listaProbTOC.append(listaTOC)
        if Comp in Bipolar.keys():
            listaBipolar.append(Bipolar['ProbInd']*Bipolar[Comp]['ProbCond']/Bipolar[Comp]['ProbInd'])
#            listaProbBipolar.append(listaBipolar)
        if Comp in Esquizofrenia.keys():
            listaEsq.append(Esquizofrenia['ProbInd']*Esquizofrenia[Comp]['ProbCond']/Esquizofrenia[Comp]['ProbInd'])
    ProbAnsiedad = 0
    ProbDepresion = 0
    ProbTOC = 0
    ProbBipolar = 0
    ProbEsq = 0
    for Elemento in listaAnsiedad:
        ProbAnsiedad = ProbAnsiedad + Elemento
    for Elemento in listaDepresion:
        ProbDepresion = ProbDepresion + Elemento
    for Elemento in listaTOC:
        ProbTOC = ProbTOC + Elemento
    for Elemento in listaBipolar:
        ProbBipolar = ProbBipolar + Elemento
    for Elemento in listaEsq:
        ProbEsq = ProbEsq + Elemento
    Paciente = open(Nombre + '.txt','a')
    Paciente.write('Dado que el paciente ' + Nombre.replace("_"," ") + ' presenta ')
    if ProbAnsiedad > ProbDepresion and ProbAnsiedad > ProbTOC and ProbAnsiedad > ProbBipolar and ProbAnsiedad > ProbEsq:
        for Comp in listaCriterios:
            if Comp in Significado.keys():
                Paciente.write(Significado[Comp] + ', ')
        Paciente.write('se determina que existe un ' + str(ProbAnsiedad*100) + '%' + ' de probabilidad de que se trate de ansiedad')
    if ProbDepresion > ProbAnsiedad and ProbDepresion > ProbTOC and ProbDepresion > ProbBipolar and ProbDepresion > ProbEsq:
        for Comp in listaCriterios:
            if Comp in Significado.keys():
                Paciente.write(Significado[Comp] + ', ')
        Paciente.write('se determina que existe un ' + str(ProbDepresion*100) + '%' + ' de probabilidad de que se trate de depresion')
    if ProbTOC > ProbAnsiedad and ProbTOC > ProbDepresion and ProbTOC > ProbBipolar and ProbTOC > ProbEsq:
        for Comp in listaCriterios:
            if Comp in Significado.keys():
                Paciente.write(Significado[Comp] + ', ')
        Paciente.write('se determina que existe un ' + str(ProbTOC*100) + '%' + ' de probabilidad de que se trate de trastorno obsesivo compulsivo')
    if ProbBipolar > ProbAnsiedad and ProbBipolar > ProbDepresion and ProbBipolar > ProbTOC and ProbBipolar > ProbEsq:
        for Comp in listaCriterios:
            if Comp in Significado.keys():
                Paciente.write(Significado[Comp] + ', ')
        Paciente.write('se determina que existe un ' + str(ProbBipolar*100) + '%' + ' de probabilidad de que se trate de trastorno bipolar')
    if ProbEsq > ProbAnsiedad and ProbEsq > ProbDepresion and ProbEsq > ProbTOC and ProbEsq > ProbBipolar:
        for Comp in listaCriterios:
            if Comp in Significado.keys():
                Paciente.write(Significado[Comp] + ', ')
        Paciente.write('se determina que existe un ' + str(ProbEsq*100) + '%' + ' de probabilidad de que se trate de esquizofreni')
    Paciente.close()
    path.os.system(Nombre+".txt")

#Ventana inicial
Home = Tk()
Home.title("ADTM")
Home.resizable(False,False)
lblHome = Label(Home, text='Asistente de Diagnóstico\nde Trastornos Mentales')
lblHome.config(font=("Verdana",20))
lblHome.grid(row=0, column=0)
Imagen1 = PhotoImage(file="ADTM.gif")
#La imagen fue obtenida de https://pixabay.com/es/photos/cerebro-anatom%C3%ADa-resumen-arte-2146817/
#Uso libre y gratuito, no requiere acreditación
#Imagen1 = Imagen1.subsample(3,3)
lblImagen1 = Label(Home, image=Imagen1, width=200, height=200)
lblImagen1.grid(row=1, column=0)
btnRegistrar = ttk.Button(Home, text="Registrar", command=newvPaciente, width=20)
btnRegistrar.grid(row=2, column=0)
btnConsultar = ttk.Button(Home, text="Consultar", command=vConsulta, width=20)
btnConsultar.grid(row=3, column=0)
btnSalir = ttk.Button(Home, text="Salir", command = quit)
btnSalir.grid(row=4, column=0)
Home.mainloop()