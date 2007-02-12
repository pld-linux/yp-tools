Summary:	NIS (or YP) client programs
Summary(de.UTF-8):	NIS (YP)-Clients
Summary(es.UTF-8):	Clientes NIS (YP)
Summary(fr.UTF-8):	Clients NIS (YP)
Summary(ja.UTF-8):	NIS (または YP)クライアントプログラム
Summary(pl.UTF-8):	Klienci NIS (YP)
Summary(pt_BR.UTF-8):	Clientes NIS (YP)
Summary(ru.UTF-8):	Клиентские программы NIS (или YP)
Summary(tr.UTF-8):	NIS (YP) istemcileri
Summary(uk.UTF-8):	Клієнтські програми NIS (або YP)
Summary(zh_CN.UTF-8):	NIS(或者 YP)客户端程序
Name:		yp-tools
Version:	2.9
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
# Source0-md5:	19de06a04129ec26773f9198e086fcd4
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	44a8ee872fa7a8df95ce311356a3cb95
Patch0:		%{name}-2.7-md5.patch
URL:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
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

%description -l de.UTF-8
Diese Implementierung von NIS für Linux basiert auf dem YP-Material
für FreeBSD.

Diese Implementierung stellt nur NIS-_Clients_ zur Verfügung. Es muß
irgendwo bereits ein NIS-Server laufen.

%description -l es.UTF-8
Esta implementación de NIS para Linux está basada en el YP para
FreeBSD. Es un porte especial para glibc 2.x y libc $>$=5.4.21. Esta
implementación solamente provee clientes NIS. Debes tener un servidor
NIS ejecutando en alguna máquina. Puedes encontrar uno para Linux en
http://www-vt.uni-paderborn.de/\~kukuk/Linux/nis.html. Por Favor, lee
también NIS-HOWTO.

%description -l fr.UTF-8
Implantation de NIS pour Linux basée sur l'YP de FreeBSD.

Cette implantation n'offre que les *clients* NIS. Vous devez avoir un
serveur NIS qui tourne.

%description -l pl.UTF-8
NIS (Network Information Service - sieciowy system informacji) jest
systemem dostarczającym przez informacje sieciowe (loginy, hasła,
katalogi domowe, grupy użytkowników) do wszystkich maszyn w sieci. NIS
może pozwalać użytkownikom logować się na dowolną maszynę w sieci o
ile na tej maszynie działają programy klienckie NIS i hasło
użytkownika jest zapisane w bazie NIS passwd. NIS był wcześniej znany
jako Sun Yellow Pages (YP).

Implementacja NIS z tego pakietu bazuje na YP z FreeBSD. Ten pakiet
zawiera tylko klientów NIS. Aby używać klientów, musisz mieć gdzieś w
sieci działający serwer NIS - ten znajduje się w pakiecie ypserv.

Zainstaluj pakiet yp-tools jeżeli potrzebujesz programów klienckich
NIS. Będziesz potrzebował zainstalować też pakiet ypbind na każdej
maszynie z klientami NIS. Jeżeli potrzebujesz serwer NIS, zainstaluj
pakiet ypserv na jednej maszynie w sieci.

%description -l pt_BR.UTF-8
Esta implementação de NIS para Linux é baseada no YP para FreeBSD. Ele
é um porte especial para glibc 2.x e libc >=5.4.21.

Esta implementação somente provê clientes NIS. Você deve ter um
servidor NIS rodando em alguma máquina. Você pode encontrar um para o
Linux em http://www-vt.uni-paderborn.de/~kukuk/Linux/nis.html. Por
favor leia também o NIS-HOWTO.

%description -l ru.UTF-8
Network Information Service (NIS) - это система, предоставляющая
сетевую информацию (имена пользователей, пароли, домашние каталоги,
информацию о группах) всем машинам сети. NIS позволяет пользователям
логиниться на любой машине в сети если на этой машине запущены
клиентские программы NIS и пароль пользователя внесен в базу данных
паролей NIS. NIS также известен как Sun Yellow Pages (YP).

Данная реализация NIS основана на YP из FreeBSD и специально
портирована под glibc 2.x и libc версий 5.4.21 или позже. Это пакет
содержит только клиентские программы NIS. Для того, чтобы использовать
эти клиенты, необходимо чтобы где-то в сети работал сервер NIS. Такой
сервер включен в пакет ypserv.

Установите пакет yp-tools на всех машинах, которые запускают
клиентские программы NIS. Если вам нужен NIS-сервер, вам также
необходимо установить пакет ypserv на какой-то из машин вашей сети.

%description -l tr.UTF-8
Bu paket Linux için bir NIS uyarlamasının yalnızca istemci kısımlarını
içermektedir. Bu hizmetten yararlanabilmek için çalışan bir NIS
sunucusuna gerek vardır.

%description -l uk.UTF-8
Network Information Service (NIS) - це система, яка надає мережеву
інформацію (імена користувачів, паролі, домашні каталоги, інформацію
про групи) всім машинам мережі. NIS дозволяє користувачам логінитися
на будь-якій машині мережі якщо на цій машині запущені клієнтські
програми NIS і пароль користувача внесений до бази даних паролів NIS.
NIS також відомий як Sun Yellow Pages (YP).

Ця реалізація NIS базована на YP з FreeBSD і спеціально портована під
glibc 2.x та libc версій 5.4.21 та старше. Цей пакет містить тільки
клієнтські програми NIS. Для того, щоб використовувати ці клієнти,
необхідно щоб десь у мережі працював сервер NIS. Такий сервер
міститься у пакеті ypserv.

Встановіть пакет yp-tools на усіх машинах, які запускають клієнтські
програми NIS. Якщо вам потрібен NIS-сервер, вам також необхідно
встановити пакет ypserv на якійсь з машин вашої мережі.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-domainname
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f yp-tools.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS THANKS TODO etc/nsswitch.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
%lang(fi) %{_mandir}/fi/man[158]/*
%lang(ja) %{_mandir}/ja/man[158]/*
%lang(pl) %{_mandir}/pl/man[158]/*
/var/yp/nicknames
