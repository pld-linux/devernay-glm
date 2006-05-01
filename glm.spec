#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	glm Alias Wavefront OBJ File Reader/Viewer Library
Name:		glm
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://devernay.free.fr/hacks/glm/%{name}-%{version}.tar.gz
# Source0-md5:	f154f0d6c3316b31ad8e8b5ced7dd5c9
#Patch0: %{name}-DESTDIR.patch
URL:		http://devernay.free.fr/hacks/glm/
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glm is an Alias Wavefront OBJ File Reader/Viewer Library.

%package examples
Summary:	examples
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description examples
This is the package containing the examples, both binary and source.

%prep
%setup -q
#%setup -q -c -T
#%setup -q -n %{name}
#%%setup -q -n %{name}-%{version}.orig -a 1
#%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-shared \
	--enable-static
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_bindir}
# gluiobj dont work
install examples/glutobj $RPM_BUILD_ROOT%{_bindir}/
install examples/smooth  $RPM_BUILD_ROOT%{_bindir}/
# game_glutobj seems same as glutobj
install examples/*.c examples/*.cpp examples/*.h examples/Makefile* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_libdir}/libglm.so.*
%{_libdir}/libglm.a
%{_includedir}/glm.h

%files examples
%defattr(644,root,root,755)
#%%doc
%{_examplesdir}/%{name}-%{version}
