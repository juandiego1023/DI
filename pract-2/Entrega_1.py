#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade
import gtk.gdk

# Creamos la clase de la ventana principal del programa
class MainWin:

	def __init__(self):
		# Le decimos a nuestro programa que archivo de glade usar (puede tener
		# un nombre distinto del script). Si no esta en el mismo directorio del
		# script habría que indicarle la ruta completa en donde se encuentra
		self.widgets  = gtk.glade.XML("Entrega_1.glade")

		window1 = self.widgets.get_widget("window1")

		#Color de fondo
		window1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#F8E0F7'))

		class combo:
			def __init__(self):
				builder = gtk.Builder()
				builder.add_from_file("Entrega_1.glade")
				self.ventanaprincipal = builder.get_object("ventanaprincipal")
				self.combo = builder.get_object("combo")
				self.boton = builder.get_object("boton")

			builder.connect_signals(self)
			self.ventanaprincipal.show()

			def popularcombo(self):
				listaelementos=gtk.ListStore(str)
				listaelementos.append(["Manzanas"])
				listaelementos.append(["Peras"])
				listaelementos.append(["Naranjas"])

			self.combo.set_model(listaelementos)
			render = gtk.CellRendererText()
			self.combo.pack_start(render, True)
			self.combo.add_attribute(render, 'text', 0)

			def on_ventanaprincipal_destroy(self, widget, data=None):
				gtk.main_quit()
		

	# Se definen los métodos, en este caso señales como "destroy" ya fueron
	# definidas en el .glade, así solo se necesita definir "on_button1_clicked"
	def on_combobox1_clicked(self, widget):
		entry1 = gtk.Label("Precio: "+self.widgets.get_widget("entry1").get_text())
		
		#Obtenemos datos del textview
		textview1 = self.widgets.get_widget("textview1")
		buffer = textview1.get_buffer()
		textview = gtk.Label("Direccion: "+buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter())+"\n\n")


# Para terminar iniciamos el programa
if __name__ == "__main__":
	MainWin()
	gtk.main()
