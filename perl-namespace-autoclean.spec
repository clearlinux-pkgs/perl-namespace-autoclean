#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-namespace-autoclean
Version  : 0.28
Release  : 17
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/namespace-autoclean-0.28.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/namespace-autoclean-0.28.tar.gz
Summary  : 'Keep imports out of your namespace'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-namespace-autoclean-license = %{version}-%{release}
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

%description
This archive contains the distribution namespace-autoclean,
version 0.28:
Keep imports out of your namespace

%package dev
Summary: dev components for the perl-namespace-autoclean package.
Group: Development
Provides: perl-namespace-autoclean-devel = %{version}-%{release}

%description dev
dev components for the perl-namespace-autoclean package.


%package license
Summary: license components for the perl-namespace-autoclean package.
Group: Default

%description license
license components for the perl-namespace-autoclean package.


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
/usr/lib/perl5/vendor_perl/5.28.1/namespace/autoclean.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/namespace::autoclean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-namespace-autoclean/LICENCE
