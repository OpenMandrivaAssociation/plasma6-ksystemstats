%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230520

Name: plasma6-ksystemstats
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/ksystemstats/-/archive/master/ksystemstats-master.tar.bz2#/ksystemstats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: Collect statistics about the running Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: lm_sensors-devel

%description
KSystemStats is a daemon that collects
statistics about the running system.

%prep
%autosetup -p1 -n ksystemstats-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/ksystemstats
%{_bindir}/kstatsviewer
%dir %{_qtdir}/plugins/ksystemstats
%{_qtdir}/plugins/ksystemstats/*.so
%{_userunitdir}/plasma-ksystemstats.service
%{_datadir}/dbus-1/services/*.ksystemstats.service
