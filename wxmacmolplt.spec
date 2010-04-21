Summary:	Program for plotting 3-D molecular structures
Summary(pl.UTF-8):	Program do wykreślania trójwymiarowych struktur molekularnych
Name:		wxmacmolplt
Version:	7.4
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://www.scl.ameslab.gov/~brett/MacMolPlt/download/%{name}-%{version}.tar.gz
# Source0-md5:	26e1a2f5e5860334f29edc3b5f5c30e9
Patch0:		%{name}-desktop.patch
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
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-wx-config="wx-gtk2-unicode-config"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install resources/wxmacmolplt.desktop $RPM_BUILD_ROOT%{_desktopdir}
install resources/wxmacmolplt.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/wxmacmolplt
%{_datadir}/wxmacmolplt
%{_desktopdir}/wxmacmolplt.desktop
%{_pixmapsdir}/wxmacmolplt.png
%{_mandir}/man1/wxmacmolplt.1*
