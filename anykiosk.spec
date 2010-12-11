%define ver 0.0.2
%define reldate 20101210

%define modulename foo

Name: AnyKiosk
Version: %ver.%reldate
Release: alt1.%reldate

%setup_python_module %modulename

Summary: Easy kiosk mode tuning for various programs 
License: GPL
Group: System/Configuration/Other

Url: http://unixforum.org/index.php?showtopic=117466
Packager: Denjs <denjs@users.berlios.de>

Source: anykiosk-%ver.%reldate.tar.gz

BuildArch:      noarch

#BuildRequires:  python-devel, python-module-setuptools
BuildPreReq:  python-devel

BuildPreReq: %py_dependencies setuptools
BuildPreReq: %py_dependencies qt4

%description
AnyKiosk - утилита автоматической настройки различных программ в режим киоска -
режим с заблокированными от изменения настройками и ограниченной функциональностью.
Версия 0.0.2 поставляется с плагином для FireFix 3.6.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files

%changelog
2010.12.02 Denjs 
    * Initial build for Sisyphus
    (firefox plugin and Qt4 interface)    