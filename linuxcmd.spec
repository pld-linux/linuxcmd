Summary:	linuxcmd - clone of Total Commander for linux
Summary(pl):	linuxcmd - klon Total Commandera dla linuxa
Name:		linuxcmd
Version:	0.5.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.algonet.se/~skeleton/linuxcmd/%{name}-%{version}.tar.gz
URL:		http://www.algonet.se/~skeleton/linuxcmd/
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	glib-devel >= 1.2.10
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
