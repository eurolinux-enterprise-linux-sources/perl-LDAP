Name:           perl-LDAP
Version:        0.56
Release:        5%{?dist}
Epoch:          1
Summary:        LDAP Perl module
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/perl-ldap/
Source0:        http://www.cpan.org/authors/id/M/MA/MARSCHAP/perl-ldap-%{version}.tar.gz
# Do not set SSL ciphers at all by default, bug #1091316, CPAN RT#95001,
# in upstream 0.63
Patch0:         perl-ldap-0.56-Do-not-set-SSL_ciphers-to-ALL-by-default.patch
# Correct Do-not-set-SSL_ciphers-to-ALL-by-default patch, bug #1091316,
# in upstream 0.64
Patch1:         perl-ldap-0.56-LDAP.pm-set-SSL_cipher_list-to-correct-value.patch
# Pass actual length to syswrite() instead of default 1500 B, bug #1104243,
# CPAN RT#96203, in upstream 0.64
Patch2:         perl-ldap-0.56-RT-96203-LDAP.pm-use-correct-length-for-syswrite.patch
# Make LDAPS work after LDAP+start_tls, bug #1210032
Patch3:         perl-ldap-0.56-Make-LDAP-work-after-LDAP-start_tls.patch
# Fix typo in man pages, bug #1286921
Patch4:         perl-ldap-0.56-Fix-typos-in-man-pages.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(inc::Module::Install)
# Run-time:
# Not needed for tests perl(Authen::SASL) >= 2.00
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::ASN1) >= 0.2
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
# Not needed for tests perl(HTTP::Negotiate)
# Not needed for tests perl(HTTP::Response)
# Not needed for tests perl(HTTP::Status)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
# Not needed for tests perl(IO::Socket::SSL) >= 1.26
# Not needed for tests perl(JSON)
# Not needed for tests perl(LWP::MediaTypes)
# Not needed for tests perl(LWP::Protocol)
# Not needed for tests perl(MIME::Base64)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Prefer core Text::Soundex
BuildRequires:  perl(Text::Soundex)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Writer)
# Optional:
# Not needed for tests perl(IO::Socket::INET6)
# Tests:
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Authen::SASL) >= 2.00
Requires:       perl(Convert::ASN1) >= 0.2
Requires:       perl(IO::Socket::SSL) >= 1.26
Requires:       perl(JSON)
Requires:       perl(MIME::Base64)
# Prefer core Text::Soundex
Requires:       perl(Text::Soundex)
Requires:       perl(Time::Local)
Requires:       perl(XML::SAX::Writer)

# Remove under-specified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Net::LDAP::Filter\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)$

%description
Net::LDAP is a collection of modules that implements an LDAP services API
for Perl programs. The module may be used to search directories or perform
maintenance functions such as adding, deleting or modifying entries.

%prep
%setup -q -n perl-ldap-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
chmod -c 644 bin/* contrib/* lib/Net/LDAP/DSML.pm
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' contrib/*
# Remove bundled libraries
rm -rf inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
chmod -R u+w %{buildroot}/*

%check
make test
 
%files
%doc Changes CREDITS
%doc contrib/ bin/
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/LWP/
%{perl_vendorlib}/Net/
%{_mandir}/man3/*.3pm*

%changelog
* Mon Mar 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.56-5
- Update patch to cleanup patch leftover

* Fri Mar 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.56-4
- Make LDAPS work after LDAP+start_tls (bug #1210032)
- Fix typo in man pages (bug #1286921)

* Wed Aug 06 2014 Petr Pisar <ppisar@redhat.com> - 1:0.56-3
- Do not set SSL ciphers at all by default (bug #1091316)
- Pass actual length to syswrite() instead of default 1500 B (bug #1104243)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.56-2
- Mass rebuild 2013-12-27

* Wed Aug 07 2013 Petr Šabata <contyk@redhat.com> - 1:0.56-1.1
- Add a few missing BRs

* Mon Jun 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.56-1
- 0.56 bump

* Wed Apr 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.55-1
- 0.55 bump

* Wed Apr 03 2013 Petr Pisar <ppisar@redhat.com> - 1:0.54-1
- 0.54 bump

* Mon Jan 28 2013 Petr Šabata <contyk@redhat.com> - 1:0.53-1
- 0.53 enhancement update

* Thu Jan 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.52-1
- 0.52 bump

* Mon Dec 03 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.51-1
- 0.51 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 1:0.50-1
- 0.50 bump

* Tue Nov 20 2012 Petr Šabata <contyk@redhat.com> - 1:0.49-2
- Add a few missing deps
- Drop command macros
- Modernize the spec

* Mon Oct 08 2012 Petr Pisar <ppisar@redhat.com> - 1:0.49-1
- 0.49 bump

* Mon Sep 17 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.47-1
- 0.47 bump

* Fri Sep 14 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.46-1
- 0.46 bump
- Should fix: RT#72108, RT#74572, RT#74759, RT#77180
- Removed bundled libraries. Use perl(inc::Module::Install).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1:0.44-2
- Perl 5.16 rebuild
- Specify all dependencies

* Mon Feb  6 2012  Marcela Maslanova <mmaslano@redhat.com> - 1:0.44-1
- update which should fix RT#66753
- clean specfile according to new guidelines

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1:0.40-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.40-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.40-2
- Mass rebuild with perl-5.12.0

* Mon Apr 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.40-1
- update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:0.34-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.34-4
- rebuild for new perl

* Mon Apr 09 2007 Robin Norwood <rnorwood@redhat.com> - 1:0.34-3
- Resolves: bz#226267
- Only filter out the unversioned Provides: perl(Net::LDAP::Filter) to
  avoid breaking dependencies.

* Thu Apr 05 2007 Robin Norwood <rnorwood@redhat.com> - 1:0.34-2
- Resolves: bz#226267
- Filter out provides perl(Net::LDAP::Filter) per package review.

* Tue Feb 13 2007 Robin Norwood <rnorwood@redhat.com> - 1:0.34-1
- New version: 0.34

* Wed Sep 27 2006 Robin Norwood <rnorwood@redhat.com> - 1:0.33-3
- Bugzilla: 207430
- Incorporate fixes from Jose Oliveira's patch
- Add perl(IO::Socket::SSL) as a BuildRequires as well
- Other cleanups from Jose

* Wed Sep 27 2006 Robin Norwood <rnorwood@redhat.com> - 0.33-1.3
- Add a requirement for IO::Socket::SSL, per bug #122066

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 0.33-1.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Tue Apr 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.33-1
- Update to 0.33.

* Sat Apr 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.3202-1
- Update to 0.3202.
- Specfile cleanup. (#153766)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 0.31-5
- rebuild

* Wed Mar 10 2004 Chip Turner <cturner@redhat.com> - 0.31-1
- Specfile autogenerated.

