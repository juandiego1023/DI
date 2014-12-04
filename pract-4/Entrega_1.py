#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
import sqlite3
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk

#conexion con la base de datos
bbdd = 'tEjercicio'
conex = sqlite3.connect(bbdd)
c = conex.cursor()

# Creamos la clase de la ventana principal del programa
class MainWin:

	def __init__(self):
		# Le decimos a nuestro programa que archivo de glade usar (puede tener
		# un nombre distinto del script). Si no esta en el mismo directorio del
		# script habría que indicarle la ruta completa en donde se encuentra
		self.widgets  = gtk.glade.XML("Entrega_1.glade")

		window1 = self.widgets.get_widget("window1")
		self.treeView=self.widgets.get_widget("treeView")
		self.entry1=self.widgets.get_widget("entry1")
		self.entry2=self.widgets.get_widget("entry2")
		self.entry3=self.widgets.get_widget("entry3")
		self.entry4=self.widgets.get_widget("entry4")
		self.entry5=self.widgets.get_widget("entry5")

#*********************************************************************************************************
		
		#Color de fondo
		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#F8E0F7'))

		# Creamos un pequeño diccionario que contiene las señales definidas en
		# glade y su respectivo método (o llamada)
		signals = {"on_button1_clicked" : self.on_button1_clicked,
			"on_button2_clicked": self.on_button2_clicked,
			"on_button3_clicked": self.on_button3_clicked,
			
			"gtk_main_quit" : gtk.main_quit
			 }

		# Luego se auto-conectan las señales.
		self.widgets.signal_autoconnect(signals)

	# Se definen los métodos, en este caso señales como "destroy" ya fueron
	# definidas en el .glade, así solo se necesita definir "on_button1_clicked"
	def on_button1_clicked(self, widget):
		"Muestra la ventana con los datos"
		ventana = gtk.Dialog()
		ok_button = ventana.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
		cancelar_button = ventana.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		ok_button.grab_default()
		ventana.set_title("Confirma")
		label = gtk.Label("<b>¿Guardar Datos?</b>\n")
		label.set_property("use-markup", True)
		entry1 = gtk.Label("Usuario: "+self.widgets.get_widget("entry1").get_text())
		entry2 = gtk.Label("Contraseña: "+self.widgets.get_widget("entry2").get_text())
		entry3 = gtk.Label("E-mail: "+self.widgets.get_widget("entry3").get_text())
		entry4 = gtk.Label("Nombres: "+self.widgets.get_widget("entry4").get_text())
		entry5 = gtk.Label("Apellidos: "+self.widgets.get_widget("entry5").get_text())

		#Obtenemos datos del textview
		textview1 = self.widgets.get_widget("textview1")
		buffer = textview1.get_buffer()
		textview = gtk.Label("Direccion: "+buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())+"\n\n")
		
		ventana.vbox.pack_start(label, True, True, 0)
		ventana.vbox.pack_start(entry1, True, True, 0)
		ventana.vbox.pack_start(entry2, True, True, 0)
		ventana.vbox.pack_start(entry3, True, True, 0)
		ventana.vbox.pack_start(entry4, True, True, 0)
		ventana.vbox.pack_start(entry5, True, True, 0)
		ventana.vbox.pack_start(textview, True, True, 0)

		# Con show_all() mostramos el contenido del cuadro de dialogo (en este
		# caso solo tiene la etiqueta) si no se hace el dialogo aparece vacio
		ventana.show_all()
		# El run y destroy hace que la ventana se cierre al apretar el boton
		ventana.run()
		ventana.destroy()

#**************************************************************************************
#Boton Listar.
	def on_button3_clicked(self, bbdd):
		ventana = gtk.Dialog()

		ok_button = ventana.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
		cancelar_button = ventana.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		self.borrar_button=ventana.add_button(gtk.STOCK_DELETE, gtk.RESPONSE_CLOSE)		
		self.borrar_button.connect("clicked",self.on_button_delete_clicked)
		ok_button.grab_default()
		
		ventana.set_title("Listar")
		
		listStore = gtk.ListStore(str, str, str, str, str)
		self.treeView=gtk.TreeView(listStore)
		self.selection=self.treeView.get_selection()
		self.selection.connect("changed",self.on_changed)
	
		c.execute('SELECT * FROM tusuario;')

		for x in c.fetchall():
			listStore.append([x[0],x[1],x[2],x[3],x[4]])
		
		renderer = gtk.CellRendererText()
		
		column = gtk.TreeViewColumn("usuario", renderer, text=0)
		column1 = gtk.TreeViewColumn("contraseña", renderer, text=1)
		column2 = gtk.TreeViewColumn("email", renderer, text=2)
		column3 = gtk.TreeViewColumn("nombre", renderer, text=3)
		column4 = gtk.TreeViewColumn("apellidos", renderer, text=4)
		
		
		self.treeView.set_model(listStore)
		self.treeView.append_column(column)
		self.treeView.append_column(column1)
		self.treeView.append_column(column2)
		self.treeView.append_column(column3)
		self.treeView.append_column(column4)

		ventana.vbox.pack_start(self.treeView, True, True, 0)
		

		# Con show_all() mostramos el contenido del cuadro de dialogo (en este
		# caso solo tiene la etiqueta) si no se hace el dialogo aparece vacio
		ventana.show_all()
		# El run y destroy hace que la ventana se cierre al apretar el boton
		ventana.run()
		ventana.destroy()
#Boton grabar.

	def on_button2_clicked(self, bbdd):

		usuario = self.widgets.get_widget("entry1").get_text()
		contrasena = self.widgets.get_widget("entry2").get_text()
		email = self.widgets.get_widget("entry3").get_text()
		nombre = self.widgets.get_widget("entry4").get_text()		
		apellidos = self.widgets.get_widget("entry5").get_text()	
		
		textview1=self.widgets.get_widget("textview1")
		buffer=textview1.get_buffer()
		direccion=buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())


		c.execute('insert into tusuario(usuario,contrasena,email,nombre,apelidos,direccion) values ("'+str(usuario)+'","'+str(contrasena)+'","'+str(email)+'","'+str(nombre)+'","'+str(apellidos)+'","'+str(direccion)+'")')
		conex.commit()

	def on_changed(self, selection):
		self.modelo, self.treeiter=selection.get_selected()
#Boton Borrar

	def on_button_delete_clicked(self,bbdd):
		c.execute("DELETE FROM tusuario WHERE email='"+self.modelo[self.treeiter][2]+"';")
		conex.commit()



# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
	
