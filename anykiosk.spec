%define ver 0.0.2
%define reldate 20101210

Name: AnyKiosk
Version: %ver.%reldate
Release: alt1

%setup_python_module %modulename

Summary: Easy kiosk mode tuning for various programs 
License: GPL
Group: System/Configuration/Other

Url: http://unixforum.org/index.php?showtopic=117466
Packager: Denjs <denjs@users.berlios.de not-altlinux.org>
#

Source: anykiosk-0.0.2.20101210.tar.gz

BuildArch:      noarch
#BuildArch:      i586

#BuildRequires:  python-devel, python-module-setuptools
BuildPreReq: python-module-PyQt4 perl

#BuildPreReq: %py_dependencies setuptools
#BuildPreReq: %py_dependencies qt4

%description
AnyKiosk - a Point&Click tool for system administrators 
to enable KIOSK features for various software.
0.0.2beta release includes only FireFox 3.6 plugin.
%description_ru
AnyKiosk - утилита автоматической настройки различных программ в режим киоска -
режим с заблокированными от изменения настройками и ограниченной функциональностью.
Версия 0.0.2 поставляется с плагином для FireFix 3.6.

%prep
#%setup -q

%build
%python_build

%install
%python_install

%files

#%changelog
#* 2010.12.02 Denjs 
#    Initial build for Sisyphus
#    (firefox plugin and Qt4 interface)    

%changelog
* Sun Dec 12 2010 Denjs <denjs@users.berlios.de not-alilinux.org> 0.0.2.20101210-alt1
[ Denjs ]
- Initial build for Sisyphus
  + firefix 3.6  plugin 
