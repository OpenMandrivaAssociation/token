%define major 0
%define libname %mklibname token
%define devname %mklibname token -d

Name:		token
Version:	24.09
Release:	1
Source0:	https://gitlab.kitware.com/utils/token/-/archive/%{version}/token-%{version}.tar.bz2
Summary:	Library for string tokenization
URL:		https://gitlab.kitware.com/utils/token
License:	MIT
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	cmake(nlohmann_json)
BuildSystem:	cmake

%patchlist
token-24.09-soversion.patch

%description
Library for string tokenization

%package -n %{libname}
Summary:	Library for string tokenization
Group:		System/Libraries

%description -n %{libname}
Library for string tokenization

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for string tokenization.

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
