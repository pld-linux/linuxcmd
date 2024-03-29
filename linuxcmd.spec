Summary:	Clone of Total Commander for Linux
Summary(pl.UTF-8):	Klon Total Commandera dla Linuksa
Name:		linuxcmd
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.algonet.se/~skeleton/linuxcmd/%{name}-%{version}.tar.gz
# Source0-md5:	f5ece078248e6f6898b2456f218fb5f4
Source1:	%{name}.desktop
URL:		http://www.algonet.se/~skeleton/linuxcmd/
BuildRequires:	glib-devel >= 1.2.10
BuildRequires:	gtk+-devel >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linuxcmd is a clone of Total Commander used to manage files under
Linux.

%description -l pl.UTF-8
linuxcmd jest klonem Total Commandera używanym do zarządzania plikami
pod Linuksem.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/%{name}.desktop
