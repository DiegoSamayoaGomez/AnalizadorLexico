from tkinter import *
from turtle import right
from analizador import BasicLexer
from sly import Lexer

#Función para botones sin programar1
def btn_clicked():
    print("Botón sin uso")

#Envío de entrada de texto para ser analizado
def analizarBtn():
    text_box.config(state='normal')
    text_box.delete("1.0", END)
    lexer = BasicLexer()
    env = {}
    text = entry1.get("1.0",'end+1c')
    if text:
        lex = lexer.tokenize(text)
        for token in lex:
            if token.type == "ERROR":                
                text_box.insert(END, "CARACTER INVALIDO -> %s, Linea = %d:" % (token.value[0], token.lineno)+"\n")
                            
            else:
                text_box.insert(END, "Tipo = {0}, Valor = {1}, Linea = {2}, No. Caracter = {3}".format(token.type, token.value, token.lineno, token.index)+"\n")
    text_box.config(state='disabled')

#Limpiar TextBox  
def nuevoBtn():   
    text_box.config(state='normal')
    text_box.delete("1.0", END)
    entry1.delete("1.0",END)
    text_box.config(state='disabled')

#Función que abre ventana de Información
def informacionFrame():
    ventanaInformacion = Toplevel()
    ventanaInformacion.title("Información")
    ventanaInformacion.geometry("700x500")  
    c=Canvas(ventanaInformacion,
    bg="#ffffff",
    height=700,
    width=500)
    filename=PhotoImage(file = f"background_1.png")
    background_label=Label(ventanaInformacion,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    ventanaInformacion.resizable(False, False)    
    ventanaInformacion.mainloop()

    
#Inicio de interfaz 
window = Tk()
window.title("Analizador Léxico")

#Dimensiones de ventana
window.geometry("880x600")
window.configure(bg = "#272727")
canvas = Canvas(
    window,
    bg = "#272727",
    height = 600,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    440.0, 156.0,
    image=background_img)

#TextBox 1 - Ingreso de datos
entry1 = Text(
    window,
    bd = 0,
    bg = "#ffffff",    
    highlightthickness = 0)

entry1.pack()

entry1.place(
    x = 31, y = 106,
    width = 818,
    height = 116)

#Botón 1 - Botón analizar
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = analizarBtn,
    relief = "flat")

b0.place(
    x = 36, y = 241,
    width = 139,
    height = 35)

#Botón 2 - Botón nuevo
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = nuevoBtn,
    relief = "flat")

b1.place(
    x = 200, y = 241,
    width = 139,
    height = 35)

#Botón 3 - Botón Información
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = informacionFrame,
    relief = "flat")

b2.place(
    x = 835, y = 2,
    width = 45,
    height = 45)

text_box = Text(
    window,
    bg= "#37474f",
    font= "CORBELL 13",    
    fg= "#fafafa",
    
    height=12,
    width=40
)

#TextBox 2 - Salida de datos
text_box.pack(expand=True)
text_box.config(state='disabled')

text_box.place(
    x = 31, y = 324,
    width = 818,
    height = 243)
window.resizable(False, False)
window.mainloop()
