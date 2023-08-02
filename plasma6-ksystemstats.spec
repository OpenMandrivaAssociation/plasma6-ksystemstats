%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230802

Name: plasma6-ksystemstats
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/ksystemstats/-/archive/master/ksystemstats-master.tar.bz2#/ksystemstats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: KDE Frameworks 6 system monitoring framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libnm) >= 1.4.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libcap)
BuildRequires: lm_sensors-devel
# Prevent pulling in plasma5
BuildRequires: plasma6-xdg-desktop-portal-kde

%description
KDE Frameworks 6 system monitoring framework.

%prep
%autosetup -p1 -n ksystemstats-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksystemstats --all-name --with-html

%files -f ksystemstats.lang
%{_prefix}/lib/systemd/user/plasma-ksystemstats.service
%{_bindir}/ksystemstats
%{_bindir}/kstatsviewer
%{_qtdir}/plugins/ksystemstats
%{_datadir}/dbus-1/services/org.kde.ksystemstats.service
