Summary:	Displays extended CPU information
Summary(pl):	Wy¶wietla rozszerzone informacje o procesorze
Name:		x86info
Version:	1.11
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.codemonkey.org.uk/projects/x86info/%{name}-%{version}.tgz
# Source0-md5:	c383845a7cbaa9c9e9784b1469e19950
URL:		http://www.codemonkey.org.uk/projects/x86info/
Requires:	dev >= 2.8.0-25
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unlike other `cpuinfo' tools which just parse /proc/cpuinfo, x86info
probes the CPU registers to find out a lot more information. It can
discover the contents of model-specific registers, discover CPU
silicon revisions, and lots more.

%description -l pl
W przeciwieñstwie do innych narzêdzi `cpuinfo', które tylko parsuj±
/proc/cpuinfo, x86info sprawdza rejestry procesorów, aby siê
dowiedzieæ wielu wiêcej informacji. Mo¿e odczytywaæ rejestry
specyficzne dla danego modelu, seriê wafla krzemowego i wiele wiêcej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
