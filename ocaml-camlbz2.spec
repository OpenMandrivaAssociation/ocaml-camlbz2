%define	oname	camlbz2
%define	modname	bz2

Name:           ocaml-%{oname}
Version:        0.6.0
Release:	15
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
sed -i 's/Pervasives\.//g' *.ml *.mli 2>/dev/null || true
# OCaml 5 C API renames (avoid double caml_ prefix)
perl -i -pe '
  for my $s (qw(
    raise_with_string raise_with_arg raise_out_of_memory raise_sys_error
    invalid_argument copy_string alloc_custom alloc_string string_length
    failwith alloc_small raise_constant raise_end_of_file
  )) {
    s/(?<![A-Za-z0-9_])$s\s*\(/caml_$s(/g;
  }
  s/caml_caml_/caml_/g;
  
if (!/caml\/fail\.h/) {
  s|#include <caml/mlvalues.h>|#include <caml/mlvalues.h>\n#include <caml/alloc.h>\n#include <caml/memory.h>\n#include <caml/fail.h>\n#include <caml/custom.h>|;
}

' c_bz.c


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
