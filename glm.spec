Summary:	glm - Alias Wavefront OBJ File Reader/Viewer Library
Summary(pl.UTF-8):	glm - biblioteka do odczytu i przeglądania plików OBJ Alias Wavefront
Name:		glm
Version:	0.3.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://devernay.free.fr/hacks/glm/%{name}-%{version}.tar.gz
# Source0-md5:	63836fce687ac5ed2108d7bc889db71f
Patch0:		%{name}-build.patch
URL:		http://devernay.free.fr/hacks/glm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glm is an Alias Wavefront OBJ File Reader/Viewer Library.

%description -l pl.UTF-8
glm to biblioteka do odczytu i przeglądania plików OBJ Alias
Wavefront.

%package devel
Summary:	Header file for glm library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki glm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for glm library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki glm.

%package static
Summary:	Static glm library
Summary(pl.UTF-8):	Statyczna biblioteka glm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glm library.

%description static -l pl.UTF-8
Statyczna biblioteka glm.

%package examples
Summary:	glm examples
Summary(pl.UTF-8):	Przykłady do glm
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description examples
This is the package containing the examples, both binary and source.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykłady w postaci źródeł i binariów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_bindir}

# gluiobj don't work
cp -p examples/glutobj $RPM_BUILD_ROOT%{_bindir}
cp -p examples/smooth  $RPM_BUILD_ROOT%{_bindir}
# game_glutobj seems same as glutobj
cp -p examples/*.c examples/*.cpp examples/*.h examples/Makefile* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_libdir}/libglm.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglm.so
%{_includedir}/glm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libglm.a

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glutobj
%attr(755,root,root) %{_bindir}/smooth
%{_examplesdir}/%{name}-%{version}
