%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: ksystemstats
Version: 5.22.3
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Collect statistics about the running Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
# (tpg) https://bugs.kde.org/show_bug.cgi?id=439615
Patch100: https://invent.kde.org/plasma/ksystemstats/-/merge_requests/8.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KSysGuard)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: lm_sensors-devel

%description
KSystemStats is a daemon that collects
statistics about the running system.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/kstatsviewer
%dir %{_qt5_plugindir}/%{name}
%{_qt5_plugindir}/%{name}/*.so
%{_userunitdir}/plasma-%{name}.service
%{_datadir}/dbus-1/services/*.%{name}.service
