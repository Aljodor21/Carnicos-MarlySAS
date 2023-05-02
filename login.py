import tkinter as tk
from herramientas import *
from conexion import *
from registro import *
from cliente import *
from administrador import *


# Funciones de los botones
def inicio():
    user = usuario.get()
    pas = password.get()

    if (user and pas):

        cur = db.connection.cursor()
        val = (user, pas)
        sql = "SELECT * FROM USUARIOS WHERE LOGIN = %s AND PASSWORD =%s"
        cur.execute(sql, val)
        usersx = cur.fetchone()
        db.connection.commit()

        if usersx:
            txtMensaje.config(text="Bienvenid@", fg=azul)
            curi = db.connection.cursor()
            val = (user, pas, 1)
            sql = 'SELECT * FROM USUARIOS WHERE login = %s AND password = %s AND tipo = %s'
            curi.execute(sql, val)
            usery = curi.fetchone()
            db.connection.commit()

            if usery:

                limpiar()
                iniciarInicio(ventana)
            else:
                limpiar()
                iniciarCliente(ventana)

        else:
            txtMensaje.config(
                text="Usuario o contraseña\n INCORRECTA", fg=rojo)
            limpiar()

    else:
        txtMensaje.config(text="No pueden existir \n CAMPOS VACIOS", fg=rojo)
        limpiar()


def limpiar():
    usuario.set("")
    password.set("")


def salirP():
    ventana.destroy()


# Creamos nuestra ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("800x500+300+50")
ventana.resizable(width=False, height=False)
ventana.overrideredirect(True)

# Con estas lineas podemos poner fondo a nuestra ventana
fondo = tk.PhotoImage(file="login.png")
fondo1 = tk.Label(ventana, image=fondo).place(
    x=0, y=0, relwidth=1, relheight=1)

# Creamos una instacia de la base de datos
db = DataBase()

# Creamos variables para no modificar los entry directamente
usuario = tk.StringVar()
password = tk.StringVar()

# Label para mostrar mensajes al usuario
txtMensaje = tk.Label(ventana, text="Bienvenid@", fg=verde, bg=None)
txtMensaje.place(x=400, y=20)

# Entradas del login
entrada = tk.Entry(ventana, textvariable=usuario,
                   width=22, relief="flat", bg=gris)
entrada.focus()
entrada.place(x=620, y=170)

entrada2 = tk.Entry(ventana, textvariable=password,
                    width=22,  relief="flat", bg=gris, show="*")
entrada2.place(x=620, y=250)

# Botones de nuestra ventana login
boton = tk.Button(ventana, text="Entrar", cursor="hand2", bg=verde, width=12,
                  relief="flat", font=("Comic Sans MS", 12, "bold"), command=lambda: inicio())
boton.place(x=620, y=320)

boton2 = tk.Button(ventana, text="Salir", cursor="hand2", bg=grisb, width=12,
                   relief="flat", font=("Comic Sans MS", 12, "bold"), command=salirP)
boton2.place(x=620, y=20)

boton3 = tk.Button(ventana, text="Registrar", cursor="hand2", bg=grisb, width=12, relief="flat", font=(
    "Comic Sans MS", 12, "bold"), command=lambda: iniciarRegistro(ventana))
boton3.place(x=620, y=400)


ventana.mainloop()
