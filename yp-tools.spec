Summary:	NIS (or YP) client programs
Summary(de):	NIS (YP)-Clients
Summary(es):	Clientes NIS (YP)
Summary(fr):	Clients NIS (YP)
Summary(ja):	NIS (�ޤ��� YP)���饤����ȥץ����
Summary(pl):	Klienci NIS (YP)
Summary(pt_BR):	Clientes NIS (YP)
Summary(ru):	���������� ��������� NIS (��� YP)
Summary(tr):	NIS (YP) istemcileri
Summary(uk):	�̦�����˦ �������� NIS (��� YP)
Summary(zh_CN):	NIS(���� YP)�ͻ��˳���.
Name:		yp-tools
Version:	2.6
Release:	5
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-passwd.patch
URL:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
BuildRequires:	autoconf
BuildRequires:	automake
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
Diese Implementierung von NIS f�r Linux basiert auf dem YP-Material
f�r FreeBSD.

Diese Implementierung stellt nur NIS-_Clients_ zur Verf�gung. Es mu�
irgendwo bereits ein NIS-Server laufen.

%description -l es
Esta implementaci�n de NIS para Linux est� basada en el YP para
FreeBSD. Es un porte especial para glibc 2.x y libc $>$=5.4.21. Esta
implementaci�n solamente provee clientes NIS. Debes tener un servidor
NIS ejecutando en alguna m�quina. Puedes encontrar uno para Linux en
http://www-vt.uni-paderborn.de/\~kukuk/Linux/nis.html. Por Favor, lee
tambi�n NIS-HOWTO.

%description -l fr
Implantation de NIS pour Linux bas�e sur l'YP de FreeBSD.

Cette implantation n'offre que les *clients* NIS. Vous devez avoir un
serveur NIS qui tourne.

%description -l pl
NIS (Network Information Service - sieciowy system informacji) jest
systemem dostarczaj�cym przez informacje sieciowe (loginy, has�a,
katalogi domowe, grupy u�ytkownik�w) do wszystkich maszyn w sieci. NIS
mo�e pozwala� u�ytkownikom logowa� si� na dowoln� maszyn� w sieci o
ile na tej maszynie dzia�aj� programy klienckie NIS i has�o
u�ytkownika jest zapisane w bazie NIS passwd. NIS by� wcze�niej znany
jako Sun Yellow Pages (YP).

Implementacja NIS z tego pakietu bazuje na YP z FreeBSD. Ten pakiet
zawiera tylko klient�w NIS. Aby u�ywa� klient�w, musisz mie� gdzie� w
sieci dzia�aj�cy serwer NIS - ten znajduje si� w pakiecie ypserv.

Zainstaluj pakiet yp-tools je�eli potrzebujesz program�w klienckich
NIS. B�dziesz potrzebowa� zainstalowa� te� pakiet ypbind na ka�dej
maszynie z klientami NIS. Je�eli potrzebujesz serwer NIS, zainstaluj
pakiet ypserv na jednej maszynie w sieci.

%description -l pt_BR
Esta implementa��o de NIS para Linux � baseada no YP para FreeBSD. Ele
� um porte especial para glibc 2.x e libc >=5.4.21.

Esta implementa��o somente prov� clientes NIS. Voc� deve ter um
servidor NIS rodando em alguma m�quina. Voc� pode encontrar um para o
Linux em http://www-vt.uni-paderborn.de/~kukuk/Linux/nis.html. Por
favor leia tamb�m o NIS-HOWTO.

%description -l ru
Network Information Service (NIS) - ��� �������, ���������������
������� ���������� (����� �������������, ������, �������� ��������,
���������� � �������) ���� ������� ����. NIS ��������� �������������
���������� �� ����� ������ � ���� ���� �� ���� ������ ��������
���������� ��������� NIS � ������ ������������ ������ � ���� ������
������� NIS. NIS ����� �������� ��� Sun Yellow Pages (YP).

������ ���������� NIS �������� �� YP �� FreeBSD � ����������
����������� ��� glibc 2.x � libc ������ 5.4.21 ��� �����. ��� �����
�������� ������ ���������� ��������� NIS. ��� ����, ����� ������������
��� �������, ���������� ����� ���-�� � ���� ������� ������ NIS. �����
������ ������� � ����� ypserv.

���������� ����� yp-tools �� ���� �������, ������� ���������
���������� ��������� NIS. ���� ��� ����� NIS-������, ��� �����
���������� ���������� ����� ypserv �� �����-�� �� ����� ����� ����.

%description -l tr
Bu paket Linux i�in bir NIS uyarlamas�n�n yaln�zca istemci k�s�mlar�n�
i�ermektedir. Bu hizmetten yararlanabilmek i�in �al��an bir NIS
sunucusuna gerek vard�r.

%description -l uk
Network Information Service (NIS) - �� �������, ��� ����� ��������
�������æ� (����� ���������ަ�, ����̦, �����Φ ��������, �������æ�
��� �����) �Ӧ� ������� ����֦. NIS ������Ѥ ������������ ��Ǧ������
�� ����-�˦� ����Φ ����֦ ���� �� æ� ����Φ ������Φ �̦�����˦
�������� NIS � ������ ����������� �������� �� ���� ����� ����̦� NIS.
NIS ����� צ����� �� Sun Yellow Pages (YP).

�� ���̦��æ� NIS �������� �� YP � FreeBSD � ���æ����� ��������� Ц�
glibc 2.x �� libc ���Ӧ� 5.4.21 �� ������. ��� ����� ͦ����� Ԧ����
�̦�����˦ �������� NIS. ��� ����, ��� ��������������� æ �̦����,
����Ȧ��� ��� ���� � ����֦ �������� ������ NIS. ����� ������
ͦ������� � ����Ԧ ypserv.

������צ�� ����� yp-tools �� �Ӧ� �������, �˦ ���������� �̦�����˦
�������� NIS. ���� ��� ���Ҧ��� NIS-������, ��� ����� ����Ȧ���
���������� ����� ypserv �� �˦��� � ����� ���ϧ ����֦.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure \
	--disable-domainname
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf AUTHORS README ChangeLog NEWS THANKS TODO etc/nsswitch.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f yp-tools.lang
%defattr(644,root,root,755)
%doc *.gz etc/*.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
%lang(fi) %{_mandir}/fi/man[158]/*
%lang(ja) %{_mandir}/ja/man[158]/*
%lang(pl) %{_mandir}/pl/man[158]/*
/var/yp/nicknames
