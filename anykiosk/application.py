# -*- coding: UTF-8 -*-
from PyQt4 import QtGui,QtCore
class Application:
	name = "default"
	
# это список значений опций'. Используется в рантайме. 
	options = {} 
	
	
#*******************************************************************************
# !CHANGEIT IN CHULD! : это описания опций (имя и описание). Его надо менять в наследуемых плагинах:
	optionsArray = {
	'имя фичи, опции или сама опция':"""
описание фичи
или опции
"""} 
#тут ключи - это строки QString - для поиска по ним.
	optionsArray_qt = {
	'имя фичи, опции или сама опция':"""
описание фичи
или опции
"""}

	def get_option(self, opt):
		return self.options[QtCore.QString(opt)]
	
	def get_options(self):
		return self.options
	
	def set_option(self, opt, value):
		self.options[QtCore.QString(opt)] = value
	
	def set_options(self, options):
		if not(isinstance(options, dict)):
			raise TypeError("dict expected")
		self.options = options
	
		
	def get_descr(self, opt):
		retv="<no description>";
		#мы не знаем что нам передали. потому попробуем плучить QString явно...
		if QtCore.QString(opt) in self.optionsArray_qt:
			retv=self.optionsArray_qt[QtCore.QString(opt)] #
		return retv
#	def get_descr(self, opt):
#		return "no description"
	
	def checks(self):
		pass
	
	def load(self):
		pass
	
	def save(self):
		pass

#*******************************************************************************
# !CHANGEIT IN CHULD!: название плагина, для регистрации
def name():
	return "DUMMY koisk mode (probe)"
	
#*******************************************************************************
# !CHANGEIT IN CHULD!: краткое описание плагина, для регистрации
def descr():
	return """==================================
  Проба настройки киоск-мода 
  """
	
#*******************************************************************************
# !CHANGEIT IN CHULD!: подробное описание плагина, для регистрации
def help():
	return """
  Плагин настраивает одну из программ для работы 
  в Koisk-mode или предлагает расширенные фичи для настройки.
  """
	
#*******************************************************************************
# !CHANGEIT IN CHULD!: отдаем собственный объект 
def object():
	return Application()
