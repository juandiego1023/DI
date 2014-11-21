#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0') 
import gtk
import gtk.glade
import gtk.gdk

def descuentoDiez(precio):
    descuento = (precio ) * 10 / 100
    return descuento

def descuentoVeinte(precio):
    descuento = (precio ) * 20 / 100
    return descuento

def valor_combobox(combobox):
    model = combobox.get_model()
    activo = combobox.get_active()
    if activo <0:
        return None
    return model[activo][0]



class MainGui:
    def __init__(self):
        self.widgets = gtk.glade.XML("Descuentos.glade")
	
        signals = { "on_entry1_changed" : self.cuentas,
	            "on_combobox1_changed": self.cuentas,
		    "on_AcercaDe_activate" : self.on_AcercaDe_activate,
                    "gtk_main_quit" : gtk.main_quit }
        
 

	self.window = self.widgets.get_widget("window")
	
	
        self.entryPrecioInicial = self.widgets.get_widget("entryPrecioInicial")
        self.labelPrecioFinal = self.widgets.get_widget("labelPrecioFinal")
	self.labelDescontadoFinal = self.widgets.get_widget("labelDescontadoFinal")
        self.combobox1 = self.widgets.get_widget("combobox1")
       
        self.combobox1.set_active(0)

	self.window.set_default_size(200,200)

	self.widgets.signal_autoconnect(signals)
	
    def on_AcercaDe_activate(self, widget):
    	ventana = gtk.Dialog()
	ventana.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#A9F5F2"))
	ventana.set_default_size(450,170)
	ventana.set_opacity(0.90)
	cancelar_button = ventana.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
	ventana.set_title("Acerca de...")
	label = gtk.Label("<b>Calculadora de descuentos 1.0</b>\n")
	label2 = gtk.Label("10%,20% sobre el precio a introducir\n\n                Juan Diego Arias Martin")
	label3=gtk.Label("")	
	label3.set_markup("<a href=\"http://www.google.es\" " "title=\"Google\">Google</a>")
	label.set_property("use-markup", True)
	ventana.vbox.pack_start(label, True, True, 0)
	ventana.vbox.pack_start(label2, True, True, 0)
	ventana.vbox.pack_start(label3, True, True, 0)
	
	ventana.show_all()

	ventana.run()
	ventana.destroy()

    def cuentas(self, widget):
		
	precioInicial=self.entryPrecioInicial.get_text()
	precioInicialFloat=float(precioInicial)
	       
        selCombo = valor_combobox(self.combobox1)
                        
        if selCombo == "10":
		 descuento=(str(descuentoDiez(precioInicialFloat)))
        elif selCombo == "20":
           	 descuento=(str(descuentoVeinte(precioInicialFloat)))
	else:
		 error("Error")

	self.labelDescontadoFinal.set_text(descuento)
	descuento=float(descuento)     
	self.labelPrecioFinal.set_text(str(precioInicialFloat-descuento))   


if __name__== "__main__":
    MainGui()
    gtk.main()
