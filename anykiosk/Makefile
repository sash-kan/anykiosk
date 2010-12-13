DESTDIR =

DATADIR = $(DESTDIR)/usr/share/anykiosk

all: 

install: all
	mkdir -p $(DATADIR)
	cp -r . $(DATADIR)/

	cp anykiosk $(DESTDIR)/usr/bin/

	## The following changes should also be performed in a post-install script
	#-chgrp games $(DESTDIR)/usr/lib/pathological/bin/write-highscores
	#-chmod 2755 $(DESTDIR)/usr/lib/pathological/bin/write-highscores

	#mkdir -p $(DESTDIR)/var/anykiosk

	#mkdir -p $(DESTDIR)/usr/share/man/man6
	#cp anykiosk.6.gz $(DESTDIR)/usr/share/man/man6

	#mkdir -p $(DESTDIR)/usr/share/doc/anykiosk
	#cp -r html $(DESTDIR)/usr/share/doc/anykiosk

uninstall:
	rm -rf $(DATADIR)
	rm -f $(DESTDIR)/usr/bin/anykiosk
	#rm -rf $(DESTDIR)/var/anykiosk
	#rm -f $(DESTDIR)/usr/share/man/man6/anykiosk.6.gz

#purge: uninstall
#	rm -f $(DESTDIR)/var/games/pathological_scores

empty: 
#distclean

#distclean:
#	rm -f write-highscores
#	rm -f html/*.png
