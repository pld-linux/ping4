Summary:	ping program
Summary(pl.UTF-8):   Program ping
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

%description -l pl.UTF-8
Całkowicie nowa implementacja pinga z wieloma nowymi możliwościami.
Obejmują one:
- przeprojektowanie w celu poprawnej obsługi pinga typu flood i Cisco
- poprawne raportowanie strat pakietów we wszystkich trybach
- obsługa opcji swobodnego routingu źródłowego oprócz ustalonego
- szybki ping bez normalnego wyjścia, zakończenie pracy jeśli host
  docelowy odpowie
- opcja do sprawdzania wszystkich adresów hostów o wielu adresach
- obsługa pingowania adresów broadcast
- łatwa instalacja na wielu platformach
- rozpoznawanie wielu nowych rodzajów i podkodów pakietów ICMP
- rozpoznawanie komunikatów o odbiciach na własne żądania ping
- raportowanie czasu podróży w ułamkach milisekund
- wyświetlanie standardowego odchylenia czasu podróży w statystykach
- buforowanie zapytań do serwera nazw w celu minimalizacji ich liczby
- automatyczne dostrajanie limitu czasu w celu zwalczenia wolnych
  łącz
- wiele bramek przy definiowaniu swobodnego routingu źródłowego
- opcja do ustawiania wartości TOS w nagłówku IP.

Zawiera łatę umożliwiającą działanie zachowywania tras IP w przypadku
maszyn Sun z kartą sieciową NC400.

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
