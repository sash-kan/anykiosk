%define ver 0.0.2
%define reldate 20101210

Name: anykiosk
Version: %ver.%reldate
Release: alt1

Summary: Easy kiosk mode tuning for various programs
License: GPL
Group: System/Configuration/Other

Url: http://unixforum.org/index.php?showtopic=117466
Packager: Denjs <denjs@users.berlios.de>

Source: anykiosk-0.0.2.20101210.tar.gz

BuildArch: noarch
BuildPreReq: python python-module-PyQt4 python-module-setuptools perl

%description
AnyKiosk - a Point-and-Click tool for system administrators 
to enable KIOSK features for various software.
0.0.2beta release includes only FireFox 3.6 plugin.

# description_ru
# AnyKiosk - утилита автоматической настройки различных программ в режим киоска -
# режим с заблокированными от изменения настройками и ограниченной функциональностью.
# Версия 0.0.2 поставляется с плагином для FireFix 3.6.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files

%changelog
* Sun Dec 12 2010 Denjs <denjs@users.berlios.de> 0.0.2.20101210-alt1
[ Denjs ]
- Initial build for Sisyphus
  + firefox 3.6  plugin
