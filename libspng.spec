Name:           libspng
Version:        0.7.3
Release:        1
Summary:        Simple, modern libpng alternative
Group:          System/Libraries
License:        BSD
URL:            https://libspng.org/
Source0:        https://github.com/randy408/libspng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%meson -Ddev_build=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/libspng.so.0*

%files devel
%doc docs
%{_includedir}/spng.h
%{_libdir}/libspng.so
%{_libdir}/pkgconfig/spng.pc
