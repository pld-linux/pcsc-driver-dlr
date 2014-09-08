Summary:	PC/SC driver for DeLaRue serial smartcard readers
Summary(pl.UTF-8):	Sterowniki PC/SC do czytników kart procesorowych DeLaRue na porcie szeregowym
Name:		pcsc-driver-dlr
Version:	0.0.5
Release:	1
License:	GPL v2+ (GemPC410), BSD (GemPC430)
Group:		Libraries
Source0:	http://pcsclite.alioth.debian.org/musclecard.com/drivers/readers/files/dlr_ifd-drv-%{version}.tar.gz
# Source0-md5:	c128478e4c4225c732c6c56ff8942f10
Patch0:		dlr_ifd-update.patch
URL:		http://pcsclite.alioth.debian.org/musclecard.com/sourcedrivers.html
BuildRequires:	pcsc-lite-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC/SC driver for DeLaRue serial smartcard readers.

%description -l pl.UTF-8
Sterownik PC/SC do czytników kart procesorowych firmy DeLaRue
podłączanych do portu szeregowego.

%prep
%setup -q -n dlr_ifd
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D IFD_Handler_DLR.so $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/IFD_Handler_DLR.so
install -d $RPM_BUILD_ROOT/etc/reader.conf.d
cat >$RPM_BUILD_ROOT/etc/reader.conf.d/DLR.conf <<EOF
FRIENDLYNAME	"DeLaRue"
LIBPATH		%{_libdir}/pcsc/drivers/IFD_Handler_DLR.so
CHANNELID	0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/pcsc/drivers/IFD_Handler_DLR.so
%config(noreplace) %verify(not md5 mtime size) /etc/reader.conf.d/DLR.conf
