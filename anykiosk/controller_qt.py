# -*- coding: UTF-8 -*-
#import pygtk
#pygtk.require('2.0')
from PyQt4 import QtGui,QtCore
import sys

class Controller:
	apps = {}
	descrs = {}
	qapp = QtGui.QApplication(sys.argv)
	
	def __init__(self):
		#Хочу русские буквы.))))
		codec=QtCore.QTextCodec.codecForName('UTF-8')
		QtCore.QTextCodec.setCodecForTr(codec)
		QtCore.QTextCodec.setCodecForCStrings(codec)
		QtCore.QTextCodec.setCodecForLocale(codec)
		#self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		boxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom);
		
		self.window = QtGui.QWidget()
		self.window.resize(600,400)
		self.window.setWindowTitle("AnyKiosk:SafeRunIt!") 
		self.window.setLayout(boxLayout)
		
		
		#self.window.connect("destroy", self.destroy)
		#QtCore.QObject.connect( self.window, QtCore.SIGNAL("anySig1"), self, QtCore.SLOT("destroy") )
		self.qapp.connect(self.qapp, QtCore.SIGNAL("lastWindowClosed()"),self.qapp, QtCore.SLOT("quit()"))
		
		#self.treestore = gtk.TreeStore(str, str, bool)
		#trend = gtk.CellRendererText()
		#chrend = gtk.CellRendererToggle()
		#chrend.set_property("mode", gtk.CELL_RENDERER_MODE_ACTIVATABLE)
		#chrend.set_property("activatable", True)
		#chrend.connect("toggled", self.cell_toggled_cb, self.treestore)
		#
		#self.treeview = gtk.TreeView(self.treestore)
		self.treestore=QtGui.QTreeWidget()
		self.treestore.setColumnCount(3)
		self.treestore.setColumnWidth(0,150)
		self.treestore.setColumnWidth(1,350)
		self.treestore.setColumnWidth(2,50)
		self.treestore.setAlternatingRowColors(True)
		self.treeview=self.treestore


		#for i in zip(["Option", "Description", "Value"], [trend, trend, chrend], range(0,3)):
		#	column = gtk.TreeViewColumn(i[0], i[1], text=i[2])
		#	column.set_resizable(True)
		#	if i[2] == 1: column.set_expand(True)
		#	if i[2] == 2: column.add_attribute(chrend, "active", 2)
		#	self.treeview.append_column(column)
		
		apply_btn = QtGui.QPushButton("Apply")
		#restore_btn = QtGui.QPushButton("Restore")
		close_btn = QtGui.QPushButton("Close")
		
		#apply_btn.connect("clicked", self.apply_cb)
		#close_btn.connect("clicked", self.close_cb)
		#QtCore.QObject.connect( apply_btn, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("apply_cb()") )
		QtCore.QObject.connect( apply_btn, QtCore.SIGNAL("clicked()"), self.apply_cb )
		QtCore.QObject.connect( close_btn, QtCore.SIGNAL("clicked()"), self.close_cb )
		
		#hbox = gtk.HBox()
		#for w in [apply_btn, restore_btn, close_btn]: hbox.pack_start(w)
		#btn_bar = gtk.Alignment(1.0, 0.0, 0.0, 0.0)
		#btn_bar.add(hbox)
		button_hboxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight);
		button_window = QtGui.QWidget()
		button_window.setLayout(button_hboxLayout)
		button_hboxLayout.addStretch(80)
		button_hboxLayout.addWidget(apply_btn)
		button_hboxLayout.addWidget(apply_btn)
		#button_hboxLayout.addWidget(restore_btn)
		button_hboxLayout.addWidget(close_btn)
		boxLayout.addWidget(button_window)

		#vbox = gtk.VBox()
		#vbox.pack_start(self.treeview)
		#vbox.pack_start(btn_bar, False, False, 0)
		#self.window.add(vbox)
		##пока лениво делать нормально:
		boxLayout.addWidget(self.treeview)


		#for w in [apply_btn, restore_btn, close_btn, hbox, btn_bar, self.treeview]: w.show()
		#vbox.show()
		#self.window.show()
		self.window.show()
	
	def main(self):
		#gtk.main()
		sys.exit(self.qapp.exec_())
		
	def destroy(self, widget, data=None):
		#gtk.main_quit()
		self.qapp.quit();
	
	#def cell_toggled_cb(self, cell, path, treestore):
		#treestore[path][2] = not treestore[path][2]
		#children = treestore[path].iterchildren()
		#while True:
		#	try:
		#		x = children.next()
		#		x[2] = treestore[path][2]
		#	except StopIteration:
		#		break
		##не нужно - потому что в QTreeWidget галочки сами так работают
		
	
	def register_app(self, module): #name, app, descr):
		self.apps[QtCore.QString(module.name())] = module.object() #app
		self.descrs[QtCore.QString(module.name())] = module.descr()
	
	def proceed(self):
		for app_name in self.apps.keys():
			app = self.apps[app_name]
			app.checks()
			app.load()
			descr = self.descrs[app_name]
			#master_iter = self.treestore.append(None, [app_name, descr, None])
			treeWidgetEl=QtGui.QTreeWidgetItem()
			treeWidgetEl.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsUserCheckable)
			treeWidgetEl.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsTristate) #need to be added for child checks update ok
			treeWidgetEl.setText(0,app_name)
			treeWidgetEl.setText(1,descr)
			treeWidgetEl.setData(2,QtCore.Qt.CheckStateRole,QtCore.Qt.Checked)
			self.treestore.addTopLevelItem(treeWidgetEl)
			master_iter = treeWidgetEl
			
			for opt in app.get_options().keys():
				#self.treestore.append(master_iter, [opt, app.get_descr(opt), app.get_option(opt)])
				treeWidgetEl2=QtGui.QTreeWidgetItem(treeWidgetEl)
				treeWidgetEl2.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsUserCheckable)
				treeWidgetEl2.setText(0,opt)
				treeWidgetEl2.setText(1,app.get_descr(opt))
				treeWidgetEl2.setData(2,QtCore.Qt.CheckStateRole,app.get_option(opt))
				
	#def apply_cb(self, button):
	def apply_cb(self):
		i = 0
		while i<self.treestore.topLevelItemCount():
			try:
				#master_row = self.treestore[str(i)]
				master_row = self.treestore.topLevelItem(i)
				i=i+1
				#if (master_row==0):
				#  break
				
				i = i + 1
				#app_name = master_row[0]
				app_name = master_row.text(0)
				
				#children = master_row.iterchildren()
				childrencount=master_row.childCount()
				childrencount_i=0;
				
				app = self.apps[app_name]
				#while True:
				while childrencount_i<childrencount :
					try:
						#x = children.next()
						x=master_row.child(childrencount_i)
						childrencount_i=childrencount_i+1;
						
						#app.set_option(x[0], x[2])
						#print "cp[00166]",x.text(0),"=", x.text(2)
						app.set_option(QtCore.QString(x.text(0)), (x.checkState(2)==QtCore.Qt.Checked) )
						
					except StopIteration:
						break
				app.save()
			except IndexError:
				break
	
	#def close_cb(self, button):
	def close_cb(self):
		#quit()
		self.qapp.quit();