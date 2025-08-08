from tkinter import *


#iniciar tkinter
aplicacion = Tk() # Crea una instancia de la clase Tk, que es la ventana principal de la aplicación

# tama de la ventana
aplicacion.geometry("1070x600+500+200") # Establece el tamaño de la ventana a 600 píxeles de ancho y 400 píxeles de alto

# evitar maximizar la ventana
aplicacion.resizable(0, 0) # Evita que la ventana sea redimensionable, es decir, que no se pueda cambiar su tamaño por el usuario

# titulo de la ventana
aplicacion.title("BluBerry Labs - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg="CadetBlue4") # Establece el color de fondo de la ventana a "CadetBlue4", un tono de azul


#panel superior
panel_superior = Frame(aplicacion, bd=1, relief = FLAT) # Crea un marco (Frame) para el panel superior de la aplicación, con un color de fondo y sin relieve
panel_superior.pack(side = TOP) # Empaqueta el panel superior en la parte superior de la ventana principal

#etiqueta titulo
#etiqueta_titulo = Label(panel_superior, text = "BluBerry Labs", font = ("Arial", 58), bg = "CadetBlue4", fg = "white") # Crea una etiqueta (Label) para mostrar el título de la aplicación, con un tipo de letra Arial de tamaño 30, color de fondo "CadetBlue4" y color de texto blanco
etiqueta_titulo = Label(panel_superior, text = "BluBerry Labs", fg ='cornsilk3',
                        font = ('Dosis',58),bg = "CadetBlue4", width = 27) # Crea una etiqueta (Label) para mostrar el título de la aplicación, con un tipo de letra Arial de tamaño 30, color de fondo "CadetBlue4" y color de texto blanco

#etiqueta_titulo.grid(row = 0, column = 0) # Coloca la etiqueta del título en el panel superior, en la fila 0 y columna 0, con un espacio de 10 píxeles a la izquierda y a la derecha
etiqueta_titulo.pack(pady=5)  # Centrado automático y separación vertical

#*****************************************
#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief = FLAT, bg = 'cornsilk3', padx = 5) # Crea un marco (Frame) para el panel izquierdo de la aplicación, con un color de fondo y sin relieve
panel_izquierdo.pack(side = LEFT, fill = BOTH) # Empaqueta el panel izquierdo en el lado izquierdo de la ventana principal y lo hace expandible para llenar todo el espacio


# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief = FLAT, bg = 'cornsilk3', padx = 5) # Crea un marco (Frame) para el panel de costos, con un color de fondo y sin relieve
panel_costos.pack(side = BOTTOM,pady=40) # Empaqueta el panel de costos en la parte inferior del panel izquierdo
#panel_costos.pack()

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text = 'COMIDA', font=('Dosis',19,'bold'), bd=1, relief = FLAT, fg='CadetBlue4') # Crea un marco (Frame) para el panel de comidas, con un título "Comida", tipo de letra 'Dosis' de tamaño 19 y negrita, sin relieve y color de texto 'cornsilk3'
panel_comidas.pack(side = LEFT) # Empaqueta el panel de comidas en la parte superior del panel izquierdo y lo hace expandible para llenar todo el espacio


# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text = 'BEBIDAS', font=('Dosis',19,'bold'), bd=1, relief = FLAT, fg='CadetBlue4') # Crea un marco (Frame) para el panel de comidas, con un título "Comida", tipo de letra 'Dosis' de tamaño 19 y negrita, sin relieve y color de texto 'cornsilk3'
panel_bebidas.pack(side = LEFT) # Empaqueta el panel de comidas en la parte superior del panel izquierdo y lo hace expandible para llenar todo el espacio


# panel postres
panel_postres = LabelFrame(panel_izquierdo, text = 'POSTRES', font=('Dosis',19,'bold'), bd=1, relief = FLAT, fg='CadetBlue4') # Crea un marco (Frame) para el panel de comidas, con un título "Comida", tipo de letra 'Dosis' de tamaño 19 y negrita, sin relieve y color de texto 'cornsilk3'
panel_postres.pack(side = LEFT) # Empaqueta el panel de comidas en la parte superior del panel izquierdo y lo hace expandible para llenar todo el espacio


#*****************************************
#panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief = FLAT) # Crea un marco (Frame) para el panel derecho de la aplicación, con un color de fondo y sin relieve
panel_derecho.pack(side = RIGHT ) # Empaqueta el panel derecho en el lado derecho de la ventana principal y lo hace expandible para llenar todo el espacio

#panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief = FLAT, bg='CadetBlue4') # Crea un marco (Frame) para el panel de la calculadora, con un color de fondo y sin relieve
panel_calculadora.pack() # Empaqueta el panel de la calculadora en la parte superior del panel derecho y lo hace expandible para llenar todo el espacio

#panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief = FLAT, bg='CadetBlue4') # Crea un marco (Frame) para el panel de la calculadora, con un color de fondo y sin relieve
panel_recibo.pack() # Empaqueta el panel de la calculadora en la parte superior del panel derecho y lo hace expandible para llenar todo el espacio

#panel botones
panel_botones = Frame(panel_derecho, bd=1, relief = FLAT, bg='CadetBlue4') # Crea un marco (Frame) para el panel de la calculadora, con un color de fondo y sin relieve
panel_botones.pack() # Empaqueta el panel de la calculadora en la parte superior del panel derecho y lo hace expandible para llenar todo el espacio


#*****************************************
#lista de productos
lista_comidas = ['Hamburguesa', 'Perro Caliente', 'Pizza', 'Ensalada', 'Tacos'] # Lista de comidas disponibles
lista_bebidas = ['Coca Cola', 'Jugo de Naranja', 'Agua', 'Cerveza', 'Vino'] # Lista de bebidas disponibles
lista_postres = ['Helado', 'Pastel', 'Fruta Fresca', 'Galletas', 'Tarta de Queso'] # Lista de postres disponibles

#generar items de comida---------------------------------------
variables_comidas = [] # Lista para almacenar las variables de las comidas seleccionadas
cuadros_comidas = [] # Lista para almacenar los cuadros de texto de las comidas seleccionadas
texto_comidas = [] # Lista para almacenar los textos de las comidas seleccionadas
contador = 0
for comida in lista_comidas:

    #crear checkbutton
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()  # Crea una variable entera para cada comida en la lista de comidas, que se utilizará para almacenar el estado del botón de opción (Checkbutton)
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',12,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comidas[contador]) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco
    comida.grid(row=contador,
                column=0,
                sticky=W) # Coloca el botón de opción en el panel de comidas, en la fila correspondiente al contador y en la columna 0, alineado a la izquierda
    #crear cuadro de entrada
    cuadros_comidas.append('')
    texto_comidas.append('')  # Agrega un elemento vacío a la lista de cuadros de texto y textos para cada comida
    texto_comidas[contador]=StringVar()
    texto_comidas[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      width=5,
                                      font=('Dosis',12,'bold'),
                                      bd=1,
                                      state=DISABLED,
                                      textvariable=texto_comidas[contador])  # Crea un cuadro de entrada (Entry) para cada comida en la lista de comidas, con un ancho de 5 caracteres, tipo de letra 'Dosis' de tamaño 19 y negrita, borde de 1 píxel, estado deshabilitado y vinculado a la variable de texto correspondiente
    cuadros_comidas[contador].grid(row=contador, column=1)  # Coloca el cuadro de entrada en el panel de comidas, en la fila correspondiente al contador y en la

    contador += 1


#generar items de bebidas----------------------------------
variables_bebidas = [] # Lista para almacenar las variables de las bebidas seleccionadas
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:

    # crear checkbutton
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()  # Crea una variable entera para cada comida en la lista de comidas, que se utilizará para almacenar el estado del botón de opción (Checkbutton)
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',12,'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_bebidas[contador]) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco
    bebida.grid(row=contador, column=0, sticky=W) # Coloca el botón de opción en el panel de bebidas, en la fila correspondiente al contador y en la columna 0, alineado a la izquierda

    # crear cuadro de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')  # Agrega un elemento vacío a la lista de cuadros de texto y textos para cada comida
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      width=5,
                                      font=('Dosis', 12, 'bold'),
                                      bd=1,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[
                                          contador])  # Crea un cuadro de entrada (Entry) para cada comida en la lista de comidas, con un ancho de 5 caracteres, tipo de letra 'Dosis' de tamaño 19 y negrita, borde de 1 píxel, estado deshabilitado y vinculado a la variable de texto correspondiente
    cuadros_bebidas[contador].grid(row=contador,column=1)  # Coloca el cuadro de entrada en el panel de comidas, en la fila correspondiente al contador y en la
    contador += 1


#generar items de postres---------------------------------------
variables_postres = [] # Lista para almacenar las variables de las bebidas seleccionadas
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    #crear chekbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()  # Crea una variable entera para cada comida en la lista de comidas, que se utilizará para almacenar el estado del botón de opción (Checkbutton)
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',12,'bold'),
                         onvalue=1, offvalue=0,
                         variable=variables_postres[contador]) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco
    postre.grid(row=contador, column=0, sticky=W) # Coloca el botón de opción en el panel de postres, en la fila correspondiente al contador y en la columna 0, alineado a la izquierda

    # crear cuadro de entrada
    cuadros_postres.append('')
    texto_postres.append('')  # Agrega un elemento vacío a la lista de cuadros de texto y textos para cada comida
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      width=5,
                                      font=('Dosis', 12, 'bold'),
                                      bd=1,
                                      state=DISABLED,
                                      textvariable=texto_postres[
                                          contador])  # Crea un cuadro de entrada (Entry) para cada comida en la lista de comidas, con un ancho de 5 caracteres, tipo de letra 'Dosis' de tamaño 19 y negrita, borde de 1 píxel, estado deshabilitado y vinculado a la variable de texto correspondiente
    cuadros_postres[contador].grid(row=contador,column=1)  # Coloca el cuadro de entrada en el panel de comidas, en la fila correspondiente al contador y en la
    contador += 1


#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada Comida
etiqueta_costo_comida = Label(panel_costos,
                              text ='Costo Comida:',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx=30)


# etiquetas de costo y campos de entrada BEBIDA
etiqueta_costo_bebida = Label(panel_costos,
                              text ='Costo Bebida:',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx=30)


# etiquetas de costo y campos de entrada Postre
etiqueta_costo_postre = Label(panel_costos,
                              text ='Costo Postre:',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1, padx=30)


# subtotal
etiqueta_subtotal = Label(panel_costos,
                              text ='Subtotal:',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=30)


# impuestos
etiqueta_impuestos = Label(panel_costos,
                              text ='IVA',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_impuestos.grid(row=1,column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuestos.grid(row=1,column=3, padx=30)


# total
etiqueta_total = Label(panel_costos,
                              text ='TOTAL:',
                              font=('Dosis',12,'bold'),
                              bg='cornsilk3',
                              fg='black')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3, padx=30)



# Botones
botones = ['total','recibo','guardar','resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',11,'bold'),
                   fg = 'black',
                   bg = 'cornsilk3',
                   bd=1, width=10)
    boton.grid(row=1,column=columnas)
    columnas += 1

# area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10,
                    padx = 10)
texto_recibo.grid(row=0,column=0)


#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',12,'bold'),
                          width=42,
                          bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)


botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','=','BORRAR','0','/']

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg = 'black',
                   bg='cornsilk3',
                   bd=1,
                   width=10)
    boton.grid(row=fila,column=columna)
    if columna==3:
        fila +=1

    columna +=1
    if columna == 4:
        columna = 0









#evitar que se cierre la ventana
aplicacion.mainloop()