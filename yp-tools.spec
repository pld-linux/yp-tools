Summary:	NIS (or YP) client programs
Summary(de):	NIS (YP)-Clients
Summary(fr):	Clients NIS (YP)
Summary(tr):	NIS (YP) istemcileri
Name:		yp-tools
Version:	2.4
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.gz
Url:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yppasswd, yp-clients
Requires:	ypbind

%description
The Network Information Service (NIS) is a system which provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network. NIS can enable users
to login on any machine on the network, as long as the machine has the
NIS client programs running and the user's password is recorded in the
NIS passwd database. NIS was formerly known as Sun Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later. This
package only provides the NIS client programs. In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for
machines on your network. You will also need to install the ypbind
package on every machine running NIS client programs. If you need an
NIS server, you'll need to install the ypserv package on one machine
on the network.

%description -l de
Diese Implementierung von NIS für Linux basiert auf dem YP-Material
für FreeBSD.

Diese Implementierung stellt nur NIS-_Clients_ zur Verfügung. Es muß
irgendwo bereits ein NIS-Server laufen.

%description -l fr
Implantation de NIS pour Linux basée sur l'YP de FreeBSD.

Cette implantation n'offre que les *clients* NIS. Vous devez avoir un
serveur NIS qui tourne.

%description -l tr
Bu paket Linux için bir NIS uyarlamasýnýn yalnýzca istemci kýsýmlarýný
içermektedir. Bu hizmetten yararlanabilmek için çalýþan bir NIS
sunucusuna gerek vardýr.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-domainname
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf {AUTHORS,README,ChangeLog,NEWS,etc/nsswitch.conf} \
	{THANKS,TODO} $RPM_BUILD_ROOT/%{_mandir}/*/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f yp-tools.lang
%defattr(644,root,root,755)
%doc *.gz etc/*.gz 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
/var/yp/nicknames
