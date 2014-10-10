%define upstream_name    MooseX-Async
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A Method Metaclass for MooseX::Async
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::AttributeHelpers)
BuildArch:	noarch

%description
MooseX::Async is a set of Metaclasses for MooseX::POE and it's siblings.
Please see them for documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 655061
- rebuild for updated spec-helper

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 381916
- adding missing buildrequires:
- import perl-MooseX-Async


* Mon Jun 01 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

