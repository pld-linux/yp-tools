Summary:	NIS (or YP) client programs
Summary(de):	NIS (YP)-Clients
Summary(es):	Clientes NIS (YP)
Summary(fr):	Clients NIS (YP)
Summary(ja):	NIS (╓ч╓©╓о YP)╔╞╔И╔╓╔╒╔С╔х╔в╔М╔╟╔И╔Ю
Summary(pl):	Klienci NIS (YP)
Summary(pt_BR):	Clientes NIS (YP)
Summary(ru):	Клиентские программы NIS (или YP)
Summary(tr):	NIS (YP) istemcileri
Summary(uk):	Кл╕╓нтськ╕ програми NIS (або YP)
Summary(zh_CN):	NIS(╩Руъ YP)©м╩╖╤кЁлпР.
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
Diese Implementierung von NIS fЭr Linux basiert auf dem YP-Material
fЭr FreeBSD.

Diese Implementierung stellt nur NIS-_Clients_ zur VerfЭgung. Es muъ
irgendwo bereits ein NIS-Server laufen.

%description -l es
Esta implementaciСn de NIS para Linux estА basada en el YP para
FreeBSD. Es un porte especial para glibc 2.x y libc $>$=5.4.21. Esta
implementaciСn solamente provee clientes NIS. Debes tener un servidor
NIS ejecutando en alguna mАquina. Puedes encontrar uno para Linux en
http://www-vt.uni-paderborn.de/\~kukuk/Linux/nis.html. Por Favor, lee
tambiИn NIS-HOWTO.

%description -l fr
Implantation de NIS pour Linux basИe sur l'YP de FreeBSD.

Cette implantation n'offre que les *clients* NIS. Vous devez avoir un
serveur NIS qui tourne.

%description -l pl
NIS (Network Information Service - sieciowy system informacji) jest
systemem dostarczaj╠cym przez informacje sieciowe (loginy, hasЁa,
katalogi domowe, grupy u©ytkownikСw) do wszystkich maszyn w sieci. NIS
mo©e pozwalaФ u©ytkownikom logowaФ siЙ na dowoln╠ maszynЙ w sieci o
ile na tej maszynie dziaЁaj╠ programy klienckie NIS i hasЁo
u©ytkownika jest zapisane w bazie NIS passwd. NIS byЁ wcze╤niej znany
jako Sun Yellow Pages (YP).

Implementacja NIS z tego pakietu bazuje na YP z FreeBSD. Ten pakiet
zawiera tylko klientСw NIS. Aby u©ywaФ klientСw, musisz mieФ gdzie╤ w
sieci dziaЁaj╠cy serwer NIS - ten znajduje siЙ w pakiecie ypserv.

Zainstaluj pakiet yp-tools je©eli potrzebujesz programСw klienckich
NIS. BЙdziesz potrzebowaЁ zainstalowaФ te© pakiet ypbind na ka©dej
maszynie z klientami NIS. Je©eli potrzebujesz serwer NIS, zainstaluj
pakiet ypserv na jednej maszynie w sieci.

%description -l pt_BR
Esta implementaГЦo de NIS para Linux И baseada no YP para FreeBSD. Ele
И um porte especial para glibc 2.x e libc >=5.4.21.

Esta implementaГЦo somente provЙ clientes NIS. VocЙ deve ter um
servidor NIS rodando em alguma mАquina. VocЙ pode encontrar um para o
Linux em http://www-vt.uni-paderborn.de/~kukuk/Linux/nis.html. Por
favor leia tambИm o NIS-HOWTO.

%description -l ru
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

%description -l tr
Bu paket Linux iГin bir NIS uyarlamasЩnЩn yalnЩzca istemci kЩsЩmlarЩnЩ
iГermektedir. Bu hizmetten yararlanabilmek iГin ГalЩЧan bir NIS
sunucusuna gerek vardЩr.

%description -l uk
Network Information Service (NIS) - це система, яка нада╓ мережеву
╕нформац╕ю (╕мена користувач╕в, парол╕, домашн╕ каталоги, ╕нформац╕ю
про групи) вс╕м машинам мереж╕. NIS дозволя╓ користувачам лог╕нитися
на будь-як╕й машин╕ мереж╕ якщо на ц╕й машин╕ запущен╕ кл╕╓нтськ╕
програми NIS ╕ пароль користувача внесений до бази даних парол╕в NIS.
NIS також в╕домий як Sun Yellow Pages (YP).

Ця реал╕зац╕я NIS базована на YP з FreeBSD ╕ спец╕ально портована п╕д
glibc 2.x та libc верс╕й 5.4.21 та старше. Цей пакет м╕стить т╕льки
кл╕╓нтськ╕ програми NIS. Для того, щоб використовувати ц╕ кл╕╓нти,
необх╕дно щоб десь у мереж╕ працював сервер NIS. Такий сервер
м╕ститься у пакет╕ ypserv.

Встанов╕ть пакет yp-tools на ус╕х машинах, як╕ запускають кл╕╓нтськ╕
програми NIS. Якщо вам потр╕бен NIS-сервер, вам також необх╕дно
встановити пакет ypserv на як╕йсь з машин вашо╖ мереж╕.

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
