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
	self.widgets2 = gtk.glade.XML("AcercaDe.glade")
	
        signals = { "on_entry1_changed" : self.cuentas,
	            "on_combobox1_changed": self.cuentas,
		    "on_AcercaDe_activate" : self.on_AcercaDe_activate,
                    "gtk_main_quit" : gtk.main_quit }
        
        self.widgets.signal_autoconnect(signals)

	self.window = self.widgets.get_widget("window")
	self.window2 = self.widgets2.get_widget("window2")	
        self.entryPrecioInicial = self.widgets.get_widget("entryPrecioInicial")
        self.labelPrecioFinal = self.widgets.get_widget("labelPrecioFinal")
	self.labelDescontadoFinal = self.widgets.get_widget("labelDescontadoFinal")
        self.combobox1 = self.widgets.get_widget("combobox1")
       
        self.combobox1.set_active(0)

	self.window.set_default_size(200,200)

	self.widgets.signal_autoconnect(signals)
	
    def on_AcercaDe_activate(self, widget):
	self.widgets2.get_widget("window2").show()
      
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
