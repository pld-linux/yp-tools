Summary:	NIS (or YP) client programs.
Name:		yp-tools
Version:	2.3
Release:	1
Copyright:	GNU
Group:		System Environment/Base
Source:		ftp://ftp.kernel.org/pub/linux/utils/net/NIS/yp-tools-%{version}.tar.gz
Url:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
Buildroot:	/tmp/yp-tools-root
Obsoletes:	yppasswd, yp-clients
Requires:	ypbind

%description
The Network Information Service (NIS) is a system which provides network
information (login names, passwords, home directories, group information)
to all of the machines on a network.  NIS can enable users to login on
any machine on the network, as long as the machine has the NIS client
programs running and the user's password is recorded in the NIS passwd
database.  NIS was formerly known as Sun Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later.  This
package only provides the NIS client programs.  In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for machines
on your network.  You will also need to install the ypbind package on
every machine running NIS client programs.  If you need an NIS server,
you'll need to install the ypserv package on one machine on the network.

%prep
%setup -q

%build
%configure \
	--disable-domainname
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

gzip -9nf {AUTHORS,COPYING,README,ChangeLog,NEWS,etc/nsswitch.conf} \
	{THANKS,TODO}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,README,ChangeLog,NEWS,etc/nsswitch.conf}.gz
%doc {THANKS,TODO}.gz
%attr(755, root, root) %{_bindir}/*
%attr(755, root, root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
/var/yp/nicknames

%changelog
* Wed Jun 23 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [2.3-1]
- FHS 2.0
- macros

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- version 2.2
- make it obsolete older yp-clients package

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2/1
- version 2.1
- require ypbind

* Fri Jun 12 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 2.0

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.4.1

* Thu Dec 04 1997 Cristian Gafton <gafton@redhat.com>
- put yppasswd again in the package, 'cause it is the right thing to do
  (sorry djb!)
- obsoletes old, unmaintained yppasswd package

* Sat Nov 01 1997 Donnie Barnes <djb@redhat.com>
- removed yppasswd from this package.

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- pulled from contrib into distribution (got fresh sources).  Thanks
  to Thorsten Kukuk <kukuk@vt.uni-paderborn.de> for the original.
- used fresh sources
