#spec for building rpm for alt-linux with gear

%define ver 0.0.2
%define reldate 20101210

Name: anykiosk
Version: %ver.%reldate
Release: alt1

Summary: Easy kiosk mode tuning for various programs
License: GPL
Group: System/Configuration/Other

Vendor: UnixForum.org (Denjs & Minoru-kun)
Url: http://anykiosk.belios.de
Packager: Denjs <denjs@users.berlios.de>

Source: anykiosk-0.0.2.20101210.tar.gz

BuildArch: noarch

BuildPreReq: python >= 2.5
BuildPreReq: python-module-PyQt4 >= 4.5
BuildPreReq: perl 
BuildPreReq: perl-Encode >= 2.37 
BuildPreReq: perl-PerlIO >= 1:5.8

#Requires: python >= 2.5
#Requires: python-module-PyQt4 >= 4.5
#Requires: perl 
#Requires: perl-Encode >= 2.37 
#Requires: perl-PerlIO >= 1:5.8

#Requires:
#python-module-setuptools

%description
AnyKiosk - a Point-and-Click tool for system administrators 
to enable KIOSK features for various software.
0.0.2beta release includes only FireFox 3.6 plugin.

%description -l ru_RU.UTF-8
AnyKiosk - утилита настройки различных программ в режим киоска -
режим с заблокированными от изменения настройками и ограниченной 
функциональностью. Просто отметье галочками нужные программы и
нажмите "применить".
Версия 0.0.2 поставляется с плагином для FireFix 3.6.

%prep
%setup -q

%build
#python_build

%install
#python_install
%make_install DESTDIR=%buildroot install


%files
/usr/share/anykiosk/tmp
/usr/share/anykiosk/*.py
/usr/share/anykiosk/moz-byteshift.pl
/usr/bin/anykiosk



%changelog
* Sun Dec 12 2010 Denjs <denjs@users.berlios.de> 0.0.2.20101210-alt1
[ Denjs ]
- Initial build for Sisyphus
  + firefox 3.6  plugin
