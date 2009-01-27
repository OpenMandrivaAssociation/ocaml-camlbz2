Name:           ocaml-camlbz2
Version:        0.6.0
Release:        %mkrel 1
Summary:        OCaml bindings for the libbz2 (AKA, bzip2) (de)compression library.
License:        LGPL
Group:          Development/Other
URL:            http://camlbz2.forge.ocamlcore.org/
Source0:        http://forge.ocamlcore.org/frs/download.php/72/camlbz2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  libbzip2-devel

%description
CamlBZ2 provides OCaml bindings for libbz2 (AKA bzip2), a popular
compression library which typically compresses better (i.e., smaller
resulting files) than gzip.

Using CamlBZ2 you can read and write compressed "files", where
files can be anything offering an in_channel/out_channel abstraction
(files, sockets, ...).

Also, with CamlBZ2 you can compress and decompress strings in memory
using the bzip2 compression algorithm.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n camlbz2-%{version}

%build
./configure
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/bz2
mkdir -p $DLLDIR
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COPYING ChangeLog INSTALL LICENSE README ROADMAP
%dir %{_libdir}/ocaml/bz2
%{_libdir}/ocaml/bz2/META
%{_libdir}/ocaml/bz2/*.cma
%{_libdir}/ocaml/bz2/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/bz2/*.a
%{_libdir}/ocaml/bz2/*.cmxa
%{_libdir}/ocaml/bz2/*.cmx
%{_libdir}/ocaml/bz2/*.mli

