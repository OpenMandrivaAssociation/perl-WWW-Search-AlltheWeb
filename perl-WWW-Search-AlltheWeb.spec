%define real_name WWW-Search-AlltheWeb

Summary:	WWW::Search::AlltheWeb - class for searching AlltheWeb
Name:		perl-%{real_name}
Version:	1.5
Release:	10
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW//%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(WWW::Search)
BuildArch:	noarch

%description
AlltheWeb is a class specialization of WWW::Search. It handles
making and interpreting AlltheWeb searches. This is one of the
fastest and largest search engines around.

http://www.alltheweb.com

This class exports no public interface; all interaction should
be done through WWW::Search objects. See SYNOPSIS.

%prep
%setup -q -n %{real_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/WWW/Search/*
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-7mdv2010.0
+ Revision: 430661
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-6mdv2009.0
+ Revision: 242159
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-4mdv2008.0
+ Revision: 25464
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5-3mdv2008.0
+ Revision: 23568
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.5-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdk
- initial Mandriva package

