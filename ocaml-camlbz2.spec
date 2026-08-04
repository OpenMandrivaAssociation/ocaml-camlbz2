%define	oname	camlbz2
%define	modname	bz2

Name:           ocaml-%{oname}
Version:        0.6.0
Release:	14
Summary:        OCaml library for reading and writing zip, jar and gzip files
Group:          Development/Other
License:        LGPLv2 with exceptions
URL:            https://camlbz2.forge.ocamlcore.org/
Source0:	camlbz2-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  bzip2-devel

%description
CamlBZ2 provides OCaml bindings for libbz2 (AKA bzip2), a popular compression
library which typically compresses better (i.e., smaller resulting files) than
gzip.

Using CamlBZ2 you can read and write compressed "files", where files can be
anything offering an in_channel/out_channel abstraction (files, sockets, ...).

Also, with CamlBZ2 you can compress and decompress strings in memory using the
bzip2 compression algorithm.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{EVRD}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n camlbz2-%{version}
# OCaml 5: Pervasives gone; C API renames
sed -i 's/Pervasives\.//g' *.ml *.mli 2>/dev/null || true
sed -i \
	-e 's/alloc_string/caml_alloc_string/g' \
	-e 's/string_length/caml_string_length/g' \
	-e 's/invalid_argument/caml_invalid_argument/g' \
	-e 's/raise_out_of_memory/caml_raise_out_of_memory/g' \
	-e 's/copy_string/caml_copy_string/g' \
	-e 's/alloc_custom/caml_alloc_custom/g' \
	-e 's/raise_sys_error/caml_raise_sys_error/g' \
	-e 's/raise_constant/caml_raise_constant/g' \
	-e 's/raise_with_string/caml_raise_with_string/g' \
	-e 's/raise_end_of_file/caml_raise_end_of_file/g' \
	-e 's/failwith/caml_failwith/g' \
	-e 's/alloc_small/caml_alloc_small/g' \
	c_bz.c
grep -q 'caml/alloc.h' c_bz.c || sed -i 's|#include <caml/mlvalues.h>|#include <caml/mlvalues.h>
#include <caml/alloc.h>
#include <caml/memory.h>
#include <caml/fail.h>|' c_bz.c


%build
%configure2_5x
%make

%install
make install DESTDIR=%{buildroot}%{_libdir}/ocaml

%files
%doc LICENSE
%{_libdir}/ocaml/%{modname}
%exclude %{_libdir}/ocaml/%{modname}/*.a
%exclude %{_libdir}/ocaml/%{modname}/*.cmxa
%exclude %{_libdir}/ocaml/%{modname}/*.cmx
%exclude %{_libdir}/ocaml/%{modname}/*.mli

%files devel
%doc LICENSE README
%{_libdir}/ocaml/%{modname}/*.a
%{_libdir}/ocaml/%{modname}/*.cmxa
%{_libdir}/ocaml/%{modname}/*.cmx
%{_libdir}/ocaml/%{modname}/*.mli
