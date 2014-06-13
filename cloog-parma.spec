%define	major	1
%define	libname	%mklibname cloog-ppl %{major}
%define	devname	%mklibname -d cloog-ppl

Summary:	The Chunky Loop Generator
Name:		cloog-parma
Version:	0.16.1
Release:	10
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.cloog.org
Source0:	ftp://gcc.gnu.org/pub/gcc/infrastructure/%{name}-%{version}.tar.gz
Patch0:		cloog-parma-aarch64.patch

BuildRequires:	texinfo
BuildRequires:	gmp-devel
BuildRequires:	ppl-devel >= 0.11
BuildRequires:	ppl_c-devel >= 0.11

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %{libname}
Summary:	Parma Polyhedra Library backend (ppl) based version of the Cloog binaries
Group:		Development/C
Obsoletes:	%{_lib}cloog1 < 0.16.1-5

%description -n %{libname}
The dynamic shared libraries of the Chunky Loop Generator

%package -n %{devname}
Summary:	Development tools for the ppl based version of Chunky Loop Generator
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--with-ppl=system \
	--disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_infodir}/dir
# MD same bin as offer in cloog
rm -rf %{buildroot}%{_bindir}/cloog

%files -n %{libname}
%{_libdir}/libcloog-ppl.so.%{major}*

%files -n %{devname}
%{_includedir}/cloog
%{_libdir}/libcloog-ppl.so
%{_libdir}/pkgconfig/cloog-ppl.pc

