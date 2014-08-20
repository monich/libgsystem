Name: libgsystem
Version: 2014.2
Release: 0
Summary: Glib extension library
Group: Development/Libraries
License: GPLv2
URL: http://git.gnome.org/libgsystem
Source: %{name}-%{version}.tar.bz2
BuildRequires: libattr-devel
BuildRequires: glib2-devel
BuildRequires: systemd-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Glib extension library

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the development library for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh --prefix=%{_prefix}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libgsystem
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig
