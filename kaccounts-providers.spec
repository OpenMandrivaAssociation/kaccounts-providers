Summary:        Additional service providers for KAccounts framework
Name:           kaccounts-providers
Version: 15.12.0
Release:        2
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

BuildArch:      noarch

URL:            https://www.kde.org/

BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  libaccounts-glib-devel
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Package)

%description
Additional service providers for KAccounts framework

%files
%_sysconfdir/signon-ui/webkit-options.d/*
%_kde5_datadir/accounts/providers/google.provider

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
