Summary:	ping program
Summary(pl):	Program ping
Name:		ping4
Version:	990522
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.nikhef.nl/pub/network/ping_%{version}.tar.Z
# Source0-md5:	1d50747f7e0eb39a351d970772207cb4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A completely new version of good old 'ping'. New features are:
- Redesign for proper flood and Cisco style ping handling.
- Packet loss is now properly reported in all modes.
- Support for loose source route option besides record route.
- Quick ping without normal output, quit when target is alive.
- Option to probe all addresses of multi-homed destinations.
- Support for pinging to broadcast address.
- Portability hooks for easy installation on various platforms.
- Recognize various new ICMP packet types and subcodes.
- Recognize bounce messages to our own ping requests.
- Round-trip time reporting in fractional milliseconds.
- Display rtt standard deviation in statistics summary.
- Cache nameserver lookups to minimize DNS queries.
- Auto-adjust timeout period to cope with slow links.
- Multiple gateways to define explicit loose source route.
- Define explicit source address for multi-homed hosts.
- Option to set an explicit TOS value in the IP header.

Contains a patch for making IP route recording work in case you have a
SUN with an NC400 ethernet controller.

%description -l pl
Ca�kowicie nowa implementacja pinga z wieloma nowymi mo�liwo�ciami.
Obejmuj� one:
- przeprojektowanie w celu poprawnej obs�ugi pinga typu flood i Cisco
- poprawne raportowanie strat pakiet�w we wszystkich trybach
- obs�uga opcji swobodnego routingu �r�d�owego opr�cz ustalonego
- szybki ping bez normalnego wyj�cia, zako�czenie pracy je�li host
  docelowy odpowie
- opcja do sprawdzania wszystkich adres�w host�w o wielu adresach
- obs�uga pingowania adres�w broadcast
- �atwa instalacja na wielu platformach
- rozpoznawanie wielu nowych rodzaj�w i podkod�w pakiet�w ICMP
- rozpoznawanie komunikat�w o odbiciach na w�asne ��dania ping
- raportowanie czasu podr�y w u�amkach milisekund
- wy�wietlanie standardowego odchylenia czasu podr�y w statystykach
- buforowanie zapyta� do serwera nazw w celu minimalizacji ich liczby
- automatyczne dostrajanie limitu czasu w celu zwalczenia wolnych
  ��cz
- wiele bramek przy definiowaniu swobodnego routingu �r�d�owego
- opcja do ustawiania warto�ci TOS w nag��wku IP.

Zawiera �at� umo�liwiaj�c� dzia�anie zachowywania tras IP w przypadku
maszyn Sun z kart� sieciow� NC400.

%prep
%setup -q -c ping

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ping $RPM_BUILD_ROOT%{_bindir}/ping4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES
%attr(4754,root,icmp) %{_bindir}/ping4
