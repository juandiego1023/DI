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
        self.widgets = gtk.glade.XML("pytemp.glade")

        signals = { "on_entry1_changed" : self.cuentas,
	            "on_combobox1_changed": self.cuentas,
                    "gtk_main_quit" : gtk.main_quit }
        
        self.widgets.signal_autoconnect(signals)

	self.window1 = self.widgets.get_widget("window1")
        self.entryPrecioInicial = self.widgets.get_widget("entryPrecioInicial")
        self.labelPrecioFinal = self.widgets.get_widget("labelPrecioFinal")
	self.labelDescontadoFinal = self.widgets.get_widget("labelDescontadoFinal")
        self.combobox1 = self.widgets.get_widget("combobox1")
       
        self.combobox1.set_active(0)

	self.window1.set_default_size(200,200)

	self.widgets.signal_autoconnect(signals)
	
	
      
    def cuentas(self, widget):
	
	precioInicial=self.entryPrecioInicial.get_text()
	precioInicial=float(precioInicial)
	       
        selec1 = valor_combobox(self.combobox1)
                        
        if selec1 == "10":
		 descuento=(str(descuentoDiez(precioInicial)))
        elif selec1 == "20":
           	 descuento=(str(descuentoVeinte(precioInicial)))

	self.labelPrecioFinal.set_text(descuento)
	descuento=float(descuento)
       
	self.labelDescontadoFinal.set_text(precioInicial-descuento)   

if __name__== "__main__":
    MainGui()
    gtk.main()
