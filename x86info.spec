Summary:	Displays extended CPU information
Summary(pl.UTF-8):	Wyświetla rozszerzone informacje o procesorze
Name:		x86info
Version:	1.20
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.codemonkey.org.uk/projects/x86info/%{name}-%{version}.tgz
# Source0-md5:	fc593ee2510fc2e265de9c2681170842
URL:		http://www.codemonkey.org.uk/projects/x86info/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unlike other `cpuinfo' tools which just parse /proc/cpuinfo, x86info
probes the CPU registers to find out a lot more information. It can
discover the contents of model-specific registers, discover CPU
silicon revisions, and lots more.

%description -l pl.UTF-8
W przeciwieństwie do innych narzędzi `cpuinfo', które tylko parsują
/proc/cpuinfo, x86info sprawdza rejestry procesorów, aby się
dowiedzieć wielu więcej informacji. Może odczytywać rejestry
specyficzne dla danego modelu, serię wafla krzemowego i wiele więcej.

%prep
%setup -q

%build
%{__make} x86info \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
