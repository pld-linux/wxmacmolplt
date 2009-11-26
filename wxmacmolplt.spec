Summary:	Program for plotting 3-D molecular structures
Summary(pl.UTF-8):	Program do wykreślania trójwymiarowych struktur molekularnych
Name:		wxmacmolplt
Version:	7.4
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.scl.ameslab.gov/~brett/MacMolPlt/download/%{name}-%{version}.tar.gz
# Source0-md5:	26e1a2f5e5860334f29edc3b5f5c30e9
URL:		http://www.scl.ameslab.gov/~brett/MacMolPlt/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	wxGTK2-unicode-gl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern graphics program for plotting 3-D molecular structures and
normal modes (vibrations).

%description -l pl.UTF-8
Nowoczesny program graficzny do wykreślania trójwymiarowych struktur
molekularnych oraz drgań swobodnych (wibracji).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-wx-config="wx-gtk2-unicode-config"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/wxmacmolplt
%{_datadir}/wxmacmolplt
%{_mandir}/man1/wxmacmolplt.1*
