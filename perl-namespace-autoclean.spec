#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-namespace-autoclean
Version  : 0.29
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/namespace-autoclean-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/namespace-autoclean-0.29.tar.gz
Summary  : 'Keep imports out of your namespace'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-namespace-autoclean-license = %{version}-%{release}
Requires: perl-namespace-autoclean-perl = %{version}-%{release}
Requires: perl(B::Hooks::EndOfScope)
Requires: perl(Module::Implementation)
Requires: perl(Module::Runtime)
Requires: perl(Package::Stash)
Requires: perl(Sub::Exporter::Progressive)
Requires: perl(Sub::Identify)
Requires: perl(Test::Requires)
Requires: perl(Try::Tiny)
Requires: perl(Variable::Magic)
Requires: perl(namespace::clean)
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution namespace-autoclean,
version 0.29:
Keep imports out of your namespace

%package dev
Summary: dev components for the perl-namespace-autoclean package.
Group: Development
Provides: perl-namespace-autoclean-devel = %{version}-%{release}
Requires: perl-namespace-autoclean = %{version}-%{release}

%description dev
dev components for the perl-namespace-autoclean package.


%package license
Summary: license components for the perl-namespace-autoclean package.
Group: Default

%description license
license components for the perl-namespace-autoclean package.


%package perl
Summary: perl components for the perl-namespace-autoclean package.
Group: Default
Requires: perl-namespace-autoclean = %{version}-%{release}

%description perl
perl components for the perl-namespace-autoclean package.


%prep
%setup -q -n namespace-autoclean-0.29
cd %{_builddir}/namespace-autoclean-0.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-namespace-autoclean
cp %{_builddir}/namespace-autoclean-0.29/LICENCE %{buildroot}/usr/share/package-licenses/perl-namespace-autoclean/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/namespace::autoclean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-namespace-autoclean/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/namespace/autoclean.pm
