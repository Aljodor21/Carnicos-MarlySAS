from tkinter import *
from tkinter import ttk
from herramientas import *
from conexion import *
from PIL import Image, ImageTk
from tkinter import messagebox


class Cliente:

    # Creamos una instancia de la base de datos
    db = DataBase()

    def __init__(self, window):
        self.wind = window
        self.wind.title("Catalogo Cárnicos Marly S.A.S")
        self.wind.geometry("800x500+300+50")
        self.wind.resizable(width=False, height=False)
        self.wind.overrideredirect(True)
        self.entry = StringVar()
        self.entry2 = StringVar()
        self.entry3 = StringVar()
        self.entry4 = StringVar()
        self.entry5 = StringVar()
        self.entry6 = StringVar()

        # Con estas lineas podemos poner fondo a nuestra ventana
        def fondo(event):
            image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
            l.image = ImageTk.PhotoImage(image)
            l.config(image=l.image)

        bgimg = Image.open('fondo2.png')
        l = Label(self.wind)
        l.place(x=0, y=0, relwidth=1, relheight=1)
        l.bind('<Configure>', fondo)

        # Frame para nuestros antiguos valores 1
        Label(self.wind, text="Precio Unidad").place(x=120, y=360)
        Entry(self.wind, textvariable=self.entry,
              state='readonly').place(x=100, y=380)

        Label(self.wind, text="Cantidad disponible").place(x=105, y=400)
        Entry(self.wind, textvariable=self.entry2,
              state='readonly').place(x=100, y=420)

        self.spinbox = Spinbox(self.wind)
        self.spinbox.place(x=100, y=450)

        # Frame para nuestros antiguos valores 2
        Label(self.wind, text="Precio Unidad").place(x=370, y=360)
        Entry(self.wind, textvariable=self.entry3,
              state='readonly').place(x=350, y=380)

        Label(self.wind, text="Cantidad disponible").place(x=355, y=400)
        Entry(self.wind, textvariable=self.entry4,
              state='readonly').place(x=350, y=420)

        self.spinbox2 = Spinbox(self.wind)
        self.spinbox2.place(x=350, y=450)

        # Frame para nuestros antiguos valores 3
        Label(self.wind, text="Precio Unidad").place(x=600, y=360)
        Entry(self.wind, textvariable=self.entry5,
              state='readonly').place(x=580, y=380)

        Label(self.wind, text="Cantidad disponible").place(x=585, y=400)
        Entry(self.wind, textvariable=self.entry6,
              state='readonly').place(x=580, y=420)

        # Menu de numeros
        self.spinbox3 = Spinbox(self.wind)
        self.spinbox3.place(x=580, y=450)

        # Mensajes al usuario
        self.txtMens = Label(self.wind, text='Bienvenid@',fg=azul)
        self.txtMens.grid(row=0,column=1)

        # Boton salir y comprar
        Button(self.wind, text="Salir", relief="flat",
               width=8, command=self.salir).place(x=45, y=25)
        self.comprar=Button(self.wind, text="Comprar", relief="flat", width=8,bg=verde, command=self.comprar).place(x=680,y=25)
        

        self.get_products()

    # Función para salir
    def salir(self):
        self.wind.destroy()

    def comprar(self):
        self.p1 = self.spinbox.cget("state")
        self.p2 = self.spinbox2.cget("state")
        self.p3 = self.spinbox3.cget("state")

        self.p11 = self.spinbox.get()
        self.p22 = self.spinbox2.get()
        self.p33 = self.spinbox3.get()

        self.p111 = 0
        self.p222 = 0
        self.p333 = 0

        if (self.p1 == 'normal'):
            self.p11 = self.spinbox.get()
            self.p111 = int(self.p11)
        else:
            self.p111 = 0

        if (self.p2 == 'normal'):
            self.p22 = self.spinbox2.get()
            self.p222 = int(self.p22)
        else:
            self.p222 = 0

        if (self.p3 == 'normal'):
            self.p33 = self.spinbox3.get()
            self.p333 = int(self.p33)
        else:
            self.p333 = 0

        self.val1 = self.entry.get()
        self.val2 = self.entry3.get()
        self.val3 = self.entry5.get()

        if (self.val1 == 'NO DISPONIBLE'):
            self.val1 = 0
        else:
            self.val1 = float(self.val1)

        if (self.val2 == 'NO DISPONIBLE'):
            self.val2 = 0
        else:
            self.val2 = float(self.val2)

        if (self.val3 == 'NO DISPONIBLE'):
            self.val3 = 0
        else:
            self.val3 = float(self.val3)

        self.total = (self.p111*self.val1) + \
            (self.p222*self.val2)+(self.p333*self.val3)
        self.totaly = str(self.total)

        respuesta = messagebox.askquestion("Pregunta", 'Seguro que desea continuar? \n Chorizo de cerdo: ' +self.p11+"\n Butifarra ahumada: "+self.p22+"\n Carnes pulpas: "+self.p33+'\nTotal a pagar:$ '+self.totaly, parent=self.wind)

        print(respuesta)
        

        if (respuesta == 'yes'):
            vec=['1','2','3']
            i = 0
            count=0

            while (i < 3):
                if (i == 0 and (self.spinbox.cget('state') == 'normal')):
                    x1=int(self.spinbox.get())
                    x2=int(self.entry2.get())
                    xal=x2-x1
                    
                    
                    t2='SELECT * FROM productos WHERE code='+vec[0]

                    self.db.cursor.execute(t2)
                    db=self.db.cursor.fetchall()
                    self.db.connection.commit()
                    
                    h1=''

                    for row in db:
                        h1=row

                    calues=(h1[1],xal,h1[3])
                    k3='UPDATE productos SET nombre=%s,cantidad=%s,preciou=%s WHERE code='+vec[0]
                    self.db.cursor.execute(k3,calues)
                    self.db.connection.commit()
                    count+=1

                elif (i == 1 and (self.spinbox2.cget('state') == 'normal')):
                    v1=int(self.spinbox2.get())
                    v2=int(self.entry4.get())
                    val=v2-v1
                    
                    
                    q2='SELECT * FROM productos WHERE code='+vec[1]

                    self.db.cursor.execute(q2)
                    db2=self.db.cursor.fetchall()
                    self.db.connection.commit()
                    
                    b1=''

                    for row in db2:
                        b1=row

                    values=(b1[1],val,b1[3])
                    q3='UPDATE productos SET nombre=%s,cantidad=%s,preciou=%s WHERE code='+vec[1]
                    self.db.cursor.execute(q3,values)
                    self.db.connection.commit()

                    count+=1

                elif (i == 2 and (self.spinbox3.cget('state') == 'normal')):
                    z1=int(self.spinbox3.get())
                    z2=int(self.entry6.get())
                    pal=z2-z1
                    
                    
                    p2='SELECT * FROM productos WHERE code='+vec[2]

                    self.db.cursor.execute(p2)
                    db3=self.db.cursor.fetchall()
                    self.db.connection.commit()
                    
                    r1=''

                    for row in db3:
                        r1=row

                    qalues=(r1[1],pal,r1[3])
                    o3='UPDATE productos SET nombre=%s,cantidad=%s,preciou=%s WHERE code='+vec[2]
                    self.db.cursor.execute(o3,qalues)
                    self.db.connection.commit()
                    count+=1

                i+=1

            if(count!=0):
                self.get_products()
                self.txtMens.config(text='Compra exitosa',fg=verde)

            
            
            
            
    

    def get_products(self):
        # Consulta en la base de datos
        query = 'SELECT * FROM productos'
        self.db.cursor.execute(query)
        db_rows = self.db.cursor.fetchall()
        self.db.connection.commit()
        cc = len(db_rows)

        if cc == 1:
            for row in db_rows:
                ide = row[4]
                if (ide == 1):
                    self.entry.set(row[3])
                    self.entry2.set(row[2])
                    self.entry3.set('NO DISPONIBLE')
                    self.entry4.set('NO DISPONIBLE')
                    self.entry5.set('NO DISPONIBLE')
                    self.entry6.set('NO DISPONIBLE')
                    self.spinbox.config(from_=0, to=row[2])
                    self.spinbox2.config(state='disabled')
                    self.spinbox3.config(state='disabled')

                elif (ide == 2):
                    self.entry.set('NO DISPONIBLE')
                    self.entry2.set('NO DISPONIBLE')
                    self.entry3.set(row[3])
                    self.entry4.set(row[2])
                    self.entry5.set('NO DISPONIBLE')
                    self.entry6.set('NO DISPONIBLE')
                    self.spinbox.config(state='disabled')
                    self.spinbox2.config(from_=0, to=row[2])
                    self.spinbox3.config(state='disabled')
                else:
                    self.entry.set('NO DISPONIBLE')
                    self.entry2.set('NO DISPONIBLE')
                    self.entry3.set('NO DISPONIBLE')
                    self.entry4.set('NO DISPONIBLE')
                    self.entry5.set(row[3])
                    self.entry6.set(row[2])
                    self.spinbox.config(state='disabled')
                    self.spinbox2.config(state='disabled')
                    self.spinbox3.config(from_=0, to=row[2])
        elif cc == 2:
            i = 0
            e = 0
            o = 0

            for row in db_rows:
                ide = row[4]

                if (ide == 1):
                    self.entry.set(row[3])
                    self.entry2.set(row[2])
                    self.spinbox.config(from_=0, to=row[2])
                    i = 1
                elif (ide == 2):
                    self.entry3.set(row[3])
                    self.entry4.set(row[2])
                    self.spinbox2.config(from_=0, to=row[2])
                    e = 1
                elif (ide == 3):
                    self.entry5.set(row[3])
                    self.entry6.set(row[2])
                    self.spinbox3.config(from_=0, to=row[2])
                    o = 1

            if (i == 0):
                self.entry.set('NO DISPONIBLE')
                self.entry2.set('NO DISPONIBLE')
                self.spinbox.config(state='disabled')

            elif (e == 0):
                self.entry3.set('NO DISPONIBLE')
                self.entry4.set('NO DISPONIBLE')
                self.spinbox2.config(state='disabled')
            elif (o == 0):
                self.entry5.set('NO DISPONIBLE')
                self.entry6.set('NO DISPONIBLE')
                self.spinbox3.config(state='disabled')

        elif cc == 3:
            for row in db_rows:
                ide = row[4]

                if (ide == 1):
                    self.entry.set(row[3])
                    self.entry2.set(row[2])
                    self.spinbox.config(from_=0, to=row[2])
                elif (ide == 2):
                    self.entry3.set(row[3])
                    self.entry4.set(row[2])
                    self.spinbox2.config(from_=0, to=row[2])
                elif (ide == 3):
                    self.entry5.set(row[3])
                    self.entry6.set(row[2])
                    self.spinbox3.config(from_=0, to=row[2])

        else:
            self.entry.set('NO DISPONIBLE')
            self.entry2.set('NO DISPONIBLE')
            self.entry3.set('NO DISPONIBLE')
            self.entry4.set('NO DISPONIBLE')
            self.entry5.set('NO DISPONIBLE')
            self.entry6.set('NO DISPONIBLE')


def iniciarCliente(principal):
    ventana = Toplevel()
    Cliente(ventana)
    
