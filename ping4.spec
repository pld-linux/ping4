Summary:	ping program
Name:		ping4
Version:	990522
Release:	1
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.nikhef.nl/pub/network/ping_%{version}.tar.Z
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A completely new version of good old 'ping'. New features are:
o  Redesign for proper flood and cisco style ping handling.
o  Packet loss is now properly reported in all modes.
o  Support for loose source route option besides record route.
o  Quick ping without normal output, quit when target is alive.
o  Option to probe all addresses of multi-homed destinations.
o  Support for pinging to broadcast address.
o  Portability hooks for easy installation on various platforms.
o  Recognize various new icmp packet types and subcodes.
o  Recognize bounce messages to our own ping requests.
o  Round-trip time reporting in fractional milliseconds.
o  Display rtt standard deviation in statistics summary.
o  Cache nameserver lookups to minimize DNS queries.
o  Auto-adjust timeout period to cope with slow links.
o  Multiple gateways to define explicit loose source route.
o  Define explicit source address for multi-homed hosts.
o  Option to set an explicit TOS value in the IP header.
Contains a patch for making ip route recording work in
case you have a SUN with an NC400 ethernet controller.

%description -l pl
Ca³kowicie nowa implementacja pinga z wieloma nowymi mo¿liwo¶ciami.

%prep
%setup -q -c ping

%build
make CFLAGS="$RPM_OPT_FLAGS -D_BSD_SOURCE" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

install -d   $RPM_BUILD_ROOT/%{_bindir}
install ping $RPM_BUILD_ROOT/%{_bindir}/ping4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(640,root,root,755)
%attr(4711,root,root)%{_bindir}/ping4

%changelog
* Fri May 28 1999 Arkadiusz Mi¶kiewicz <misiek@pld.org.pl>
- initial version  
