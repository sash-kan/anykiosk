# -*- coding: UTF-8 -*-
import application

from PyQt4 import QtGui,QtCore

#2010.11.07
#2010.11.08
import os


# по описаниям http://tvxlc.livejournal.com/6943.html 
#+ http://habrahabr.ru/blogs/firefox/40098/
#+ http://habrahabr.ru/blogs/firefox/21631/
#+ https://developer.mozilla.org/en/Automatic_Mozilla_Configurator/Locked_config_settings
#+ http://users.telenet.be/mydotcom/howto/linuxkiosk/webterm02.htm
class DummyFF(application.Application):
	
#*******************************************************************************
	optionsArray = {
	'lockPref("browser.startup.homepage", "about:blank");':u"""
Устанавливаем стартовую 
страницу about:blank
""",
	
	'lockPref("browser.startup.page", 0);':u"""
Та же настройка, что и browser.startup.homepage, 
делаем стартовой страницей - пустую.
Просто на всякий случай.
""",
	
	'lockPref("browser.tabs.autoHide", false);':"""
Запрещаем пропадать панельке с tab'ами, 
когда ни один tab не открыт.
Просто мне так больше нравится :) 
""",
	
	'lockPref("network.proxy.type",0);':"""
Никаких прокси-серверов.
Прямой доступ к интернету.
""",
	
	'lockPref("privacy.sanitize.sanitizeOnShutdown", true);':"""
Чистим личные данные пользователей 
после закрытия программы.
""",
	
	'lockPref("privacy.sanitize.promptOnSanitize", false);':"""
к "Чистим личные данные пользователей":,
причем , не консультируясь по этому поводу с ними.
""",
	
	'lockPref("privacy.item.sessions", true);':"""
Чистим все SSL сессии.
""",
	
	'lockPref("privacy.item.passwords", true);':"""
чиcтим все пароли, если они 
каким-то образом сохранились.
""",
	
	'lockPref("privacy.item.history", true);':"""
Удаляем всю history, чтобы никто не знал, 
что школьники лазят по порно-сайтам
""",
	
	'lockPref("privacy.item.downloads", true);':"""
Удаляем список скаченных программ. 
(а то скачать скачают, а вот список скаченных 
программ, не всегда чистят за собой).
""",
	
	'lockPref("privacy.item.formdata", true);':"""
Чистим данные введенные в формы.
""",
	
	'lockPref("privacy.item.cookies", true);':"""
Чистим печенюшки :)
""",
	
	'lockPref("privacy.item.cache", true);':"""
никакого кеширования (?).
""",
	
	'lockPref("browser.formfill.enable", false);':"""
Не сохраняем данные, введенные в формы.
""",
	
	'lockPref("browser.search.update", false);':"""
Не ищем обновления плагинов для поиска.
""",
	
	'lockPref("privacy.popups.showBrowserMessage", true);':"""
Показываем информационную линейку, которая предупреждает пользователя 
что тот или иной pop-up был заблокрован программой. 
Чтобы не было лишних вопросов почему они не открываются.
""",
	
	'lockPref("browser.shell.checkDefaultBrowser", false);':"""
Не проверяем, является ли Mozilla Firefox просмотрщиком по умолчанию, 
ибо пользователи пугаются при сообщении, что программа 
не является просмотрщиком по умолчанию.
""",
	
	'lockPref("security.enable_java", true);':"""
Включаем Java.
""",
	
	'lockPref("javascript.enabled", true);':"""
Включаем JavaScript.
""",
	
	'lockPref("security.warn_entering_secure", false);':"""
Не предупреждаем пользователей, 
что зашли на сайт через SSL. 
Все равно не читают этого сообщения.
""",
	
	'lockPref("security.warn_leaving_secure", false);':"""
Не предупреждаем пользователей, 
что вышли с сайта, на котором лазили через SSL. 
Все равно не читают этого сообщения.
""",
	
	'lockPref("security.warn_submit_insecure", false);':"""
Не пугаем пользователей тем, что их данные, 
отосланные Plain Text'ом, могут перехватить. 
(А то будут боятся работать в интернете).
""",
	
	'lockPref("browser.tabs.loadInBackground", true);':"""
Пусть все табы открытые открываются в фоне. 
(Мне так больше нравится :) )
""",
	
	'lockPref("browser.tabs.opentabfor.middleclick", true);':"""
Открываем новые табы щелчком на мышиное колесико.
""",
	
	'lockPref("browser.tabs.warnOnClose", true);':"""
Предупреждаем юЗверя, что у него отрыты несколько табов,
а он собрался закрывать Firefox. 
""",
	
	'lockPref("extensions.update.enabled", false);':"""
Мы не пользуемся extension'ами, п
оэтому искать их обновления не будем.
""",
	
	'lockPref("signon.rememberSignons", false);':"""
Отказываемся от услуг Password Manager'а. 
Он дома (и то под вопросом), а не в публичных местах.
""",
	
	'lockPref("browser.download.manager.closeWhenDone", true);':"""
Закрываем download manager, когда все что нужно скачали
""",
	
	'lockPref("security.enable_ssl2", true);':"""
Используем SSL 2.0. На всякий случай.
""",
	
	'lockPref("security.enable_ssl3", true);':"""
Используем SSL 3.0. Без него никак :)
""",
	
	'lockPref("security.enable_tls", true);':"""
Не знаю что за протокол. Потом почитаю. 
Тем не менее, раз он по умолчанию включен, поступим так же :)
""",
	
	'lockPref("signon.prefillForms", false);':"""
Не заполняем формы паролями автоматически, 
потому что мы их не сохраняем.
""",
	
	'lockPref("signon.expireMasterPassword", true);':"""
Если кто-то и поставил Master Password в Password Manager'е,
 пусть он пропадет. Не нужно конфигурировать чужой компьютер под себя :)
""",
	
	'lockPref("browser.download.manager.openDelay", 0);':"""
Всегда показываем download manager, даже если скачивание заняло 1 секунду.
""",
	
	'lockPref("browser.download.manager.focusWhenStarting", true);':"""
Фокусируем download manager, когда начинаем скачивать. :)
""",
	
	'lockPref("browser.download.useDownloadDir", false);':"""
Пусть пользователь сам выбирает куда ему нужно сохранять файлы. 
А то бывает кто-то поставить download directory, а другой не понимает, 
куда скачивается его программка.
""",
	
	'lockPref("browser.link.open_external", 3);':"""
Все линки открываются в новом табе.
( Я так привык :) )
""",
	
	'lockPref("browser.download.manager.showWhenStarting", true);':"""
Показываем download manager каждый раз 
как начинается скачивание файла.
""",
	
	'lockPref("browser.history_expire_days", 0);':"""
Не ведем history :)
""",
	
	'lockPref("xpinstall.enabled", false);':"""
Не позволяем инсталлировать разного рода extensions.
"""  }

	
#*******************************************************************************
	def load(self):
		print " loading options from application config files "
		
		for opt in self.optionsArray:
			self.optionsArray_qt[QtCore.QString(opt)]=self.optionsArray[opt]
			self.set_option(QtCore.QString(opt), False) # <------------ тут надо бы научиться читать конфиг файла и подставлять сюда то что нашли
#		self.set_option('Опция 2', True)

		
	def save(self):
		
		#---------------------------------------------------------------------------
		# Пути проверены только для ПСПО5  
		#---------------------------------------------------------------------------
		pathToPutLocaSettingsJS="/usr/lib/firefox/defaults/preferences/"
		locaSettingsJSFilename="local-settings.kioskmode.js"
		#---------------------------------------------------------------------------
		pathToPutMozillaCFG="/usr/lib/firefox/"
		mozillaCFGFilename="mozilla.kioskmode.cfg"
		#---------------------------------------------------------------------------
		tmpWorkingPath="./tmp/"
		
		print " saving options to application config files "
		
		rezF="//\n"
		for opt in self.options.keys():
			print "dummy: saveopt", QtCore.QString(opt), "=", self.options[QtCore.QString(opt)]
			if self.options[QtCore.QString(opt)] == True :
				rezF=rezF+str(opt)
				rezF=rezF+str("\n")
		
		f = file(tmpWorkingPath+"mozilla.cfg.txt","w")
		f.write(str(rezF))
		f.close()
		
		print " :::: perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename
		os.system("perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename)
		# теперь у нас есть файл с настройками пригодный для подсовывания фоксу.
		# его покладем скорее всего в /usr/lib/firefox/ 
		
		#вот тут и нужны права рута.
		print " :::: (writing 'locaSettings.js file')  -=>",(pathToPutLocaSettingsJS+locaSettingsJSFilename),")"
		f = file(pathToPutLocaSettingsJS+locaSettingsJSFilename,"w")
		f.write('pref("general.config.filename", "'+mozillaCFGFilename+'");')
		f.close()
		
		print " :::: cp "+tmpWorkingPath+mozillaCFGFilename+" "+pathToPutMozillaCFG+mozillaCFGFilename
		os.system("cp "+tmpWorkingPath+mozillaCFGFilename+" "+pathToPutMozillaCFG+mozillaCFGFilename)
		
		#Все. теперь можно перезапустить фокс и должно быть счастье)))).


#	def checks(self):
#		pass
	
#*******************************************************************************
def name():
	return "DUMMY: Firefox 3.5 koisk (probe)"
	
#*******************************************************************************
def descr():
	return """==================================
  Проба настройки киоск-мода для FireFox 3.5
  (см http://tvxlc.livejournal.com/6943.html )"""
	
#*******************************************************************************
def object():
	return DummyFF()
	
#*******************************************************************************
	#--------------------------------------------------------------------
	# TODO: 2010.10.24 from Denjs: 
	#--------------------------------------------------------------------
	# Нужен скроллинг внутри окна прилодения. опций много, все уезжает вниз 
	#--------------------------------------------------------------------
	# TODO: 2010.10.24 from Denjs: 
	#--------------------------------------------------------------------
	# 2010.10.24_1440: (надо доработать в следубщей части:
	# опции и конфиги могут быть 2-х видов:
  #  опции приложения, которые нам и надо менять.
	#  опции настройки плагина - такие например как путь до конфигов прилодения
	# сейчас есть меню опций только для опции target-прилодения.
	# надо как-то читать опции плагина из ini-файла что ли? инишник на первых порах подойдет.
	#--------------------------------------------------------------------
	# на текущий момент - принимаем направление движения: 
	# 
	# (1) нет "рекомендуемых опций"
	# коорые могут быть загружены по умолчанию. 
	# Все галочки грузятся из конфига программы.
	# (было бы хорошо иметь возможность сохранить набранный конфиг галочек 
  #   и загрузить его потом на другой машине)
	# 
	# (2) программа не позволяет менять опции.
	# например - сказано что "включаем Java"
	# - нет возможности ставить опцию - отключаем джава, ероме как добавлением её 
	# как ещё один пункт в меню.