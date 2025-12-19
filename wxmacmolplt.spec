Summary:	Program for plotting 3-D molecular structures
Summary(pl.UTF-8):	Program do wykreślania trójwymiarowych struktur molekularnych
Name:		wxmacmolplt
Version:	7.7.2
Release:	3
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/brettbode/wxmacmolplt/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9689e9ba8a3ec50ab5e65fd1e0e9fb25
Patch0:		%{name}-desktop.patch
URL:		https://brettbode.github.io/wxmacmolplt/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glew-devel
BuildRequires:	ming-devel
BuildRequires:	wxGTK3-unicode-gl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern graphics program for plotting 3-D molecular structures and
normal modes (vibrations).

%description -l pl.UTF-8
Nowoczesny program graficzny do wykreślania trójwymiarowych struktur
molekularnych oraz drgań swobodnych (wibracji).

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
export CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure \
	--with-wx-config=wx-gtk3-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a resources/wxmacmolplt.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a resources/wxmacmolplt.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/wxmacmolplt
%{_datadir}/wxmacmolplt
%{_desktopdir}/wxmacmolplt.desktop
%{_pixmapsdir}/wxmacmolplt.png
%{_mandir}/man1/wxmacmolplt.1*
