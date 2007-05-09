%define real_name WWW-Search-AlltheWeb

Summary:	WWW::Search::AlltheWeb - class for searching AlltheWeb
Name:		perl-%{real_name}
Version:	1.5
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW//%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(WWW::Search)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/WWW/Search/*
%{_mandir}/*/*

