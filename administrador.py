from tkinter import *
from tkinter import ttk
from herramientas import *
from conexion import *
from PIL import Image, ImageTk

class Product:

    db=DataBase()

    #Creamos nuestra ventana
    def __init__(self,window):
        self.wind=window
        self.wind.title("Cárnicos Marly S.A.S")
        self.wind.geometry("800x500+300+50")
        self.wind.resizable(width=False,height=False)
        self.wind.overrideredirect(True)

        #Con estas lineas podemos poner fondo a nuestra ventana
        def fondo(event):
            image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
            l.image = ImageTk.PhotoImage(image)
            l.config(image=l.image)

        bgimg = Image.open('fondo.png')
        l = Label(self.wind)
        l.place(x=0, y=0, relwidth=1, relheight=1)
        l.bind('<Configure>', fondo)


        #Frame para nuestro crud
        frame=LabelFrame(self.wind, text="Registro de productos nuevos")
        frame.grid(row=0,column=0,padx=110,pady=40)

        #Name input
        Label(frame,text='Nombre: ').grid(row=0,column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=0,column=1)

        #cantidad input
        Label(frame,text='Cantidad: ').grid(row=1,column=0)
        self.cantidad = Entry(frame)
        self.cantidad.grid(row=1,column=1)

        #precio input
        Label(frame,text='Precio Unidad: ').grid(row=0,column=3)
        self.preciou = Entry(frame)
        self.preciou.grid(row=0,column=4)

        #code input
        Label(frame,text='Codigo: ').grid(row=1,column=3)
        self.codi = Entry(frame)
        self.codi.grid(row=1,column=4)

        #Boton agregar, eliminar y modificar
        ttk.Button(frame,text="Guardar Producto",command=self.add_product).grid(row=5,columnspan=6,sticky=W+E)

        ttk.Button(frame,text="Eliminar",command=self.eliminar_product).grid(row=6,column=0,columnspan=3,sticky=W+E,)

        ttk.Button(frame,text="Modificar",command=self.modificar_producto).grid(row=6,column=3,columnspan=3,sticky=W+E)

        #Boton salir
        ttk.Button(self.wind,text="Salir",command=self.salir).place(x=650,y=35)

        #Mensajes al usuario
        self.txtMensaje=Label(self.wind,text="Bienvenid@",fg=verde,bg=None)
        self.txtMensaje.grid(row=5,column=0,columnspan=4)
        

        #Tabla

        columnas=('Nombre','Cantidad','PrecioU','Codigo')

        self.tree=ttk.Treeview(self.wind,height=10,columns=columnas,show='headings')

        self.tree.heading('#0',text='')
        self.tree.heading('Nombre',text='Nombre')
        self.tree.heading('Cantidad',text='Cantidad')
        self.tree.heading('PrecioU',text='Precio Unidad')
        self.tree.heading('Codigo',text='Codigo')

        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('Nombre',width=120,anchor=CENTER)
        self.tree.column('Cantidad',width=120,anchor=CENTER)
        self.tree.column('PrecioU',width=120,anchor=CENTER)
        self.tree.column('Codigo',width=120,anchor=CENTER)


        self.tree.grid(row=6,column=0,padx=10)
        
        self.get_products()


    #Metodos del crud

    #Listar
    def get_products(self):
        #Limpiando la tabla
        records= self.tree.get_children()
        for elementos in records:
            self.tree.delete(elementos)

        #Consulta en la base de datos
        query='SELECT * FROM productos'
        self.db.cursor.execute(query)
        db_rows=self.db.cursor.fetchall()
        self.db.connection.commit()

        #Llenando los datos
        for row in db_rows:
            id=row[0]
            self.tree.insert('',END,id,text=id,values=(row[1],row[2],row[3],row[4]))

    #Crear
    def add_product(self):
        if self.validar():
            nombre=self.name.get()
            cantid=self.cantidad.get()
            precio=self.preciou.get()
            cod=self.codi.get()

            que='SELECT * FROM productos WHERE code='+cod
            self.db.cursor.execute(que)
            compro=self.db.cursor.fetchall()
            self.db.connection.commit()

            if compro:
                self.txtMensaje.config(text='Producto existente \n Debes modificar el producto',fg=rojo)
            else:
            
                val=(nombre,cantid,precio,cod)
                #Consulta en la base de datos
                query='INSERT INTO productos (NOMBRE,CANTIDAD,PRECIOU,CODE) VALUES (%s,%s,%s,%s)'
                self.db.cursor.execute(query,val)
                self.db.connection.commit()

                self.txtMensaje.config(text='Agregado correctamente',fg=azul)
            

        else:
            self.txtMensaje.config(text='No deben existir campos vacios',fg=azul)
            
        self.limpiar()
        self.get_products()

    def eliminar_product(self):
        self.txtMensaje.config(text='')

        if self.tree.selection():

            self.txtMensaje.config(text='')
            id=self.tree.selection()[0]
            sql='DELETE FROM productos where id='+id
            self.db.cursor.execute(sql)
            self.db.connection.commit()
            self.tree.delete(id)
            self.txtMensaje.config(text='Eliminado correctamente',fg=verde)
        else:
            self.txtMensaje.config(text='Debes elegir un producto',fg=azul)
        
    def modificar_producto(self):

        self.txtMensaje.config(text='')

        if self.tree.selection():
            id=self.tree.selection()[0]
            nom=self.tree.item(id,"values")[0]
            can=self.tree.item(id,"values")[1]
            pre=self.tree.item(id,"values")[2]
            cod=self.tree.item(id,"values")[3]

            self.edit_wind=Toplevel()
            self.edit_wind.title('Editar producto')
            self.edit_wind.geometry("440x120+380+90")
            self.edit_wind.resizable(width=False,height=False)
            self.edit_wind.overrideredirect(True)

            #Frame para nuestros antiguos valores
            Label(self.edit_wind, text="Antiguo nombre").grid(row=0,column=1,padx=2)
            Entry(self.edit_wind,textvariable=StringVar(self.edit_wind,value=nom),state='readonly').grid(row=0,column=2)

            Label(self.edit_wind, text="Antigua cantidad").grid(row=1,column=1,padx=2)
            Entry(self.edit_wind,textvariable=StringVar(self.edit_wind,value=can),state='readonly').grid(row=1,column=2)

            Label(self.edit_wind, text="Antiguo precioU").grid(row=2,column=1,padx=2)
            Entry(self.edit_wind,textvariable=StringVar(self.edit_wind,value=pre),state='readonly').grid(row=2,column=2)

            Label(self.edit_wind, text="Antiguo codigo").grid(row=3,column=1,padx=2)
            Entry(self.edit_wind,textvariable=StringVar(self.edit_wind,value=cod),state='readonly').grid(row=3,column=2)

            #Name input 
            Label(self.edit_wind,text='Nombre: ').grid(row=0,column=3)
            new_name= Entry(self.edit_wind)
            new_name.focus()
            new_name.grid(row=0,column=4)


            #cantidad input
            Label(self.edit_wind,text='Cantidad: ').grid(row=1,column=3)
            new_cantidad = Entry(self.edit_wind)
            new_cantidad.grid(row=1,column=4)

            #precio input
            Label(self.edit_wind,text='Precio Unidad: ').grid(row=2,column=3)
            new_preciou = Entry(self.edit_wind)
            new_preciou.grid(row=2,column=4)

            #code input
            Label(self.edit_wind,text='Codigo: ').grid(row=3,column=3)
            new_codi = Entry(self.edit_wind)
            new_codi.grid(row=3,column=4)

            #Botones subventana
            Button(self.edit_wind,text='Modificar',command=lambda:self.edit_records(id,new_name.get(),new_cantidad.get(),new_preciou.get(),new_codi.get())).grid(row=4,column=0,columnspan=3,sticky=W+E,padx=3)
            Button(self.edit_wind,text='Salir',command=self.edit_wind.destroy).grid(row=4,column=3,columnspan=3,sticky=W+E)
            


        else:
            self.txtMensaje.config(text='Debes elegir un producto',fg=verde)

            

    def edit_records(self,id,new_name,new_cantidad,new_preciou,new_codi):
        
        values=(new_name,new_cantidad,new_preciou,new_codi)
        query='UPDATE productos SET nombre=%s,cantidad=%s,preciou=%s,code=%s WHERE id='+id

        if(len(new_name) and len(new_cantidad) and len(new_preciou) and len(new_codi)):
            self.db.cursor.execute(query,values)
            self.db.connection.commit()
            self.edit_wind.destroy()
            self.txtMensaje.config(text='Producto modificado satisfactoriamente',fg=verde)
            self.get_products()
        else:
            self.txtMensaje.config(text='No pueden existir campos vacios',fg=rojo)

    def validar(self):

        return len(self.name.get()) != 0 and len(self.cantidad.get()) != 0 and len(self.preciou.get()) != 0 and len(self.codi.get()) != 0
    
    def limpiar(self):
        self.name.delete(0,END)
        self.cantidad.delete(0,END)
        self.preciou.delete(0,END)
        self.codi.delete(0,END)

    def salir(self):
        self.wind.destroy()
            
      
def iniciarInicio(principal):
    ventana=Toplevel()
    Product(ventana)

