#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-namespace-autoclean
Version  : 0.28
Release  : 8
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/namespace-autoclean-0.28.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/namespace-autoclean-0.28.tar.gz
Summary  : 'Keep imports out of your namespace'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-namespace-autoclean-data = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution namespace-autoclean,
version 0.28:
Keep imports out of your namespace

%package data
Summary: data components for the perl-namespace-autoclean package.
Group: Data

%description data
data components for the perl-namespace-autoclean package.


%package dev
Summary: dev components for the perl-namespace-autoclean package.
Group: Development
Requires: perl-namespace-autoclean-data = %{version}-%{release}
Provides: perl-namespace-autoclean-devel = %{version}-%{release}

%description dev
dev components for the perl-namespace-autoclean package.


%prep
%setup -q -n namespace-autoclean-0.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-namespace-autoclean
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-namespace-autoclean/LICENCE
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
/usr/lib/perl5/vendor_perl/5.28.0/namespace/autoclean.pm

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-namespace-autoclean/LICENCE

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/namespace::autoclean.3
