import tkinter as tk
from tkinter import ttk
from herramientas import *
from conexion import *
from PIL import Image, ImageTk


#Creamos nuestra ventana principal
def crearV(ventana,principal):

    #Funciones de los botones
    def salir():
     principal.destroy()

    def limpiar():
        login.set("")
        password.set("")
        nombre.set("")
        direccion.set("")
        email.set("")
        tipe.set("") 
        code.set("")

    def iniciar():
        usuario=login.get()
        contrasena=password.get()
        name=nombre.get()
        address=direccion.get()
        correo=email.get()
        tip=tipe.get()
        codigo=code.get()

        if tip =='A':
            tip=1
        else:
            tip=0

        if (usuario== "" or contrasena == "" or name==""or address==""or correo==""or codigo=="" or tip==""):
            txtMensaje.config(text="No pueden existir \n CAMPOS VACIOS",fg=rojo)
            limpiar()
        else:
            if(codigo=="kiri"):
                val=(usuario,contrasena,name,address,correo,tip)
                sql="INSERT INTO USUARIOS (LOGIN,PASSWORD,NOMBRE,DIRECCION,EMAIL,TIPO) VALUES (%s,%s,%s,%s,%s,%s)"
                db.cursor.execute(sql,val)
                db.connection.commit()
                txtMensaje.config(text="Creado satisfactoriamente!!!",fg="green")
                limpiar()
                ventana.after(30000,ventana.destroy())

            else:
                txtMensaje.config(text="El codigo es \n INCORRECTO",fg=azul)
                limpiar()

    ventana.title("Registro")
    ventana.geometry("800x500+300+50")
    ventana.resizable(width=False,height=False)
    ventana.overrideredirect(True)
    #Con estas lineas podemos poner fondo a nuestra ventana
    
    def fondo(event):
        image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
        l.image = ImageTk.PhotoImage(image)
        l.config(image=l.image)

    bgimg = Image.open('registro.png')
    l = tk.Label(ventana)
    l.place(x=0, y=0, relwidth=1, relheight=1)
    l.bind('<Configure>', fondo)


    #Label para mostrar mensajes al usuario
    txtMensaje=tk.Label(ventana,text="Bienvenid@",fg=verde,bg=None)
    txtMensaje.place(x=400,y=20)

    #Creamos una instacia de la base de datos
    db=DataBase()
    login=tk.StringVar()
    password=tk.StringVar()
    nombre=tk.StringVar()
    direccion=tk.StringVar()
    email=tk.StringVar()
    tipe=tk.StringVar()
    code=tk.StringVar()
    

    #Entradas de la ventana Registro
    entrada =tk.Entry(ventana, textvariable=login, width=22,relief="flat", bg=gris)
    entrada.place(x=620,y=114)

    entrada2 =tk.Entry(ventana, textvariable=password, width=22,  relief="flat", bg=gris, show="*")
    entrada2.place(x=620,y=180)

    entrada3 =tk.Entry(ventana, textvariable=nombre, width=22,  relief="flat", bg=gris)
    entrada3.place(x=620,y=245)

    entrada4 =tk.Entry(ventana, textvariable=direccion, width=22,  relief="flat", bg=gris)
    entrada4.place(x=620,y=310)

    entrada5 =tk.Entry(ventana, textvariable=email, width=22,  relief="flat", bg=gris)
    entrada5.place(x=620,y=375)

    entrada6 =tk.Entry(ventana, textvariable=code, width=8,  relief="flat", bg=gris,show="*")
    entrada6.place(x=690,y=34)

    rel="A","U"
    combo = ttk.Combobox(ventana,values=rel,textvariable=tipe)
    combo.place(x=400,y=420)

    #Botones de nuestra ventana Registro
    boton = tk.Button(ventana, text="Registrar",cursor="hand2", bg=verde,width=12,relief="flat",font=("Comic Sans MS",12,"bold"),command=lambda:iniciar())
    boton.place(x=620,y=435)

    boton2 = tk.Button(ventana, text="Salir",cursor="hand2", bg=grisb,width=12,relief="flat",font=("Comic Sans MS",12,"bold"),command=salir)
    boton2.place(x=20,y=440)


def iniciarRegistro(principal):
    ven=tk.Toplevel()
    crearV(ven,principal)

    def volver(event=None):
        ven.destroy
        principal.update()
        principal.deiconify()

    



    

    