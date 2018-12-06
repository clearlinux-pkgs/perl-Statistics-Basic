#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Statistics-Basic
Version  : 1.6611
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-1.6611.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-1.6611.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstatistics-basic-perl/libstatistics-basic-perl_1.6611-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Statistics-Basic-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Number::Format)

%description
use Statistics::Basic qw(:all);
my $median = median( 1,2,3 );
my $mean   = mean(  [1,2,3]); # array refs are ok too

%package dev
Summary: dev components for the perl-Statistics-Basic package.
Group: Development
Provides: perl-Statistics-Basic-devel = %{version}-%{release}

%description dev
dev components for the perl-Statistics-Basic package.


%package license
Summary: license components for the perl-Statistics-Basic package.
Group: Default

%description license
license components for the perl-Statistics-Basic package.


%prep
%setup -q -n Statistics-Basic-1.6611
cd ..
%setup -q -T -D -n Statistics-Basic-1.6611 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Statistics-Basic-1.6611/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Statistics-Basic
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Statistics-Basic/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/ComputedVector.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/ComputedVector.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Correlation.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Correlation.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Covariance.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Covariance.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/LeastSquareFit.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/LeastSquareFit.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Mean.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Mean.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Median.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Median.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Mode.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Mode.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/StdDev.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/StdDev.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Variance.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Variance.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Vector.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/Vector.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/_OneVectorBase.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/_OneVectorBase.pod
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/_TwoVectorBase.pm
/usr/lib/perl5/vendor_perl/5.28.1/Statistics/Basic/_TwoVectorBase.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Statistics::Basic.3
/usr/share/man/man3/Statistics::Basic::ComputedVector.3
/usr/share/man/man3/Statistics::Basic::Correlation.3
/usr/share/man/man3/Statistics::Basic::Covariance.3
/usr/share/man/man3/Statistics::Basic::LeastSquareFit.3
/usr/share/man/man3/Statistics::Basic::Mean.3
/usr/share/man/man3/Statistics::Basic::Median.3
/usr/share/man/man3/Statistics::Basic::Mode.3
/usr/share/man/man3/Statistics::Basic::StdDev.3
/usr/share/man/man3/Statistics::Basic::Variance.3
/usr/share/man/man3/Statistics::Basic::Vector.3
/usr/share/man/man3/Statistics::Basic::_OneVectorBase.3
/usr/share/man/man3/Statistics::Basic::_TwoVectorBase.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Statistics-Basic/deblicense_copyright
