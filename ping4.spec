Summary:	ping program
Name:		ping4
Version:	990522
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.nikhef.nl/pub/network/ping_%{version}.tar.Z
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A completely new version of good old 'ping'. New features are:
 - Redesign for proper flood and cisco style ping handling.
 - Packet loss is now properly reported in all modes.
 - Support for loose source route option besides record route.
 - Quick ping without normal output, quit when target is alive.
 - Option to probe all addresses of multi-homed destinations.
 - Support for pinging to broadcast address.
 - Portability hooks for easy installation on various platforms.
 - Recognize various new icmp packet types and subcodes.
 - Recognize bounce messages to our own ping requests.
 - Round-trip time reporting in fractional milliseconds.
 - Display rtt standard deviation in statistics summary.
 - Cache nameserver lookups to minimize DNS queries.
 - Auto-adjust timeout period to cope with slow links.
 - Multiple gateways to define explicit loose source route.
 - Define explicit source address for multi-homed hosts.
 - Option to set an explicit TOS value in the IP header. Contains a
   patch for making ip route recording work in case you have a SUN with
   an NC400 ethernet controller.

%description -l pl
Ca³kowicie nowa implementacja pinga z wieloma nowymi mo¿liwo¶ciami.

%prep
%setup -q -c ping

%build
make CFLAGS="$RPM_OPT_FLAGS -D_BSD_SOURCE" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

install ping $RPM_BUILD_ROOT/%{_bindir}/ping4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4755,root,root)%{_bindir}/ping4
