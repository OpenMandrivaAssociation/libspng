%define libname %mklibname shumate
%define devname %mklibname -d shumate

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


%package -n %{libname}
Summary:        Shared library for %{name}
Provides:     spng = %{version}-%{release}

%description -n %{libname}
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package -n %{devname}
Summary:        Development files for %{name}
Provides: spng-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
# Not compile with Clang 15:
# ../spng/spng.c:3798:23: error: type '_Float32' (aka 'float') in generic association compatible with previously specified type 'float'
export CC=gcc
export CXX=g++
%meson -Ddev_build=true
%meson_build

%install
%meson_install

%files -n %{libname} 
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/libspng.so.0*

%files -n %{devname}
%doc docs
%{_includedir}/spng.h
%{_libdir}/libspng.so
%{_libdir}/pkgconfig/spng.pc
