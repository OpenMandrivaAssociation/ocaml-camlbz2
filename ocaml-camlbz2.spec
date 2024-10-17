%define	oname	camlbz2
%define	modname	bz2

Name:           ocaml-%{oname}
Version:        0.6.0
Release:        9
Summary:        OCaml library for reading and writing zip, jar and gzip files
Group:          Development/Other
License:        LGPLv2 with exceptions
URL:            https://camlbz2.forge.ocamlcore.org/
Source0:        https://forge.ocamlcore.org/frs/download.php/72/%{oname}-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x
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
%setup -q -n %{oname}-%{version}

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



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 0.6.0-8
+ Revision: 797833
- Rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - imported package ocaml-camlbz2

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 390237
- rebuild

* Tue Jan 27 2009 Florent Monnier <blue_prawn@mandriva.org> 0.6.0-1mdv2009.1
+ Revision: 334307
- summary-ended-with-dot
- stublibs dir for dll
- import ocaml-camlbz2

