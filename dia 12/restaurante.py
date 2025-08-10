from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [200, 300, 400, 500,600]
precios_bebida = [100, 150, 200,250, 300]
precios_postres = [500, 600, 650, 500, 400]


def clic_boton(numero):
    global operador
    operador = operador +  numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x= 0
    for i in cuadros_comidas:
        if variables_comidas[x].get()==1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get()=='0':
                cuadros_comidas[x].delete(0,END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x += 1

    x = 0
    for i in cuadros_bebidas:
        if variables_bebidas[x].get()==1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for i in cuadros_postres:
        if variables_postres[x].get()==1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comidas:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1


    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1


    sub_total_postre = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1


    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto = sub_total * 0.19
    total = sub_total + impuesto

    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postre.set(f'${round(sub_total_postre,2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuesto.set(f'${round(impuesto, 2)}')
    var_total.set(f'${round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N#-{random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END,f'Factura:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*'*63+'\n')
    texto_recibo.insert(END,f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END,f'-'*75+'\n')

    x=0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get())*precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get())*precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END,f'{lista_postres[x]}\t\t{postre.get()}\t${int(postre.get())*precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END,f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los Postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END, f'Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IVA: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'TOTAL: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, f'Te esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(1.0,END)

    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)

    var_costo_comida.set('0')
    var_costo_bebida.set('0')
    var_costo_postre.set('0')
    var_subtotal.set('0')
    var_impuesto.set('0')
    var_total.set('0')



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
                         variable=variables_comidas[contador],
                         command=revisar_check) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco

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
                         variable=variables_bebidas[contador],
                         command=revisar_check) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco
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
                                      textvariable=texto_bebidas[contador])  # Crea un cuadro de entrada (Entry) para cada comida en la lista de comidas, con un ancho de 5 caracteres, tipo de letra 'Dosis' de tamaño 19 y negrita, borde de 1 píxel, estado deshabilitado y vinculado a la variable de texto correspondiente
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
                         variable=variables_postres[contador],
                         command=revisar_check) # Crea un botón de opción (Checkbutton) para cada comida en la lista de comidas, con el texto de la comida, tipo de letra 'Dosis' de tamaño 19 y negrita, valor activado 1, valor desactivado 0, color de fondo 'CadetBlue4' y color de texto blanco
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
                                      textvariable=texto_postres[contador])  # Crea un cuadro de entrada (Entry) para cada comida en la lista de comidas, con un ancho de 5 caracteres, tipo de letra 'Dosis' de tamaño 19 y negrita, borde de 1 píxel, estado deshabilitado y vinculado a la variable de texto correspondiente
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
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',11,'bold'),
                   fg = 'black',
                   bg = 'cornsilk3',
                   bd=1, width=10)
    botones_creados.append(boton)
    boton.grid(row=1,column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

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


botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','=','C','0','/']
botones_guardados = []

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
    botones_guardados.append(boton)
    boton.grid(row=fila,column=columna)
    if columna==3:
        fila +=1

    columna +=1
    if columna == 4:
        columna = 0


botones_guardados[0].config(command=lambda : clic_boton('7'))
botones_guardados[1].config(command=lambda : clic_boton('8'))
botones_guardados[2].config(command=lambda : clic_boton('9'))
botones_guardados[3].config(command=lambda : clic_boton('+'))
botones_guardados[4].config(command=lambda : clic_boton('4'))
botones_guardados[5].config(command=lambda : clic_boton('5'))
botones_guardados[6].config(command=lambda : clic_boton('6'))
botones_guardados[7].config(command=lambda : clic_boton('-'))
botones_guardados[8].config(command=lambda : clic_boton('1'))
botones_guardados[9].config(command=lambda : clic_boton('2'))
botones_guardados[10].config(command=lambda : clic_boton('3'))
botones_guardados[11].config(command=lambda : clic_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : clic_boton('0'))
botones_guardados[15].config(command=lambda : clic_boton('/'))








#evitar que se cierre la ventana
aplicacion.mainloop()