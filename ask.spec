%define name	ask
%define version	2.5.3
%define release	%mkrel 8

Summary:	Active Spam Killer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
URL:		http://a-s-k.sourceforge.net/
Group:		Networking/Mail
Requires:	python
BuildRequires:  python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Active Spam Killer (ASK) protects your email account against spam
by confirming the sender's email address before actual delivery
takes place. The confirmation happens by means of a "confirmation
message" that is automatically sent to all "unknown" users. Once
the sender replies to that message (a simple reply will do),
future emails from that person will be delivered immediately. You
can also specify (regexp) addresses to be immediately accepted,
rejected (with a nastygram) or ignored. The package also includes
a utility to scan your old mailboxes and generate a list of emails
to be accepted automatically.

%prep

%setup -q
perl -p -i -e 's@#!/usr/bin/env python.*@#!/usr/bin/env python@' *.py */*.py
%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}/ask
install -d %{buildroot}%{_datadir}/ask
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/ask/templates

install -m0755 askfilter asksetup %{buildroot}%{_bindir}/
install -m0755 utils/asksenders %{buildroot}%{_bindir}/

install -m0644 askversion.py %{buildroot}%{_libdir}/
install -m0644 askconfig.py %{buildroot}%{_libdir}/ask/
install -m0644 asklock.py %{buildroot}%{_libdir}/ask/
install -m0644 asklog.py %{buildroot}%{_libdir}/ask/
install -m0644 askmail.py %{buildroot}%{_libdir}/ask/
install -m0644 askmain.py %{buildroot}%{_libdir}/ask/
install -m0644 askmessage.py %{buildroot}%{_libdir}/ask/
install -m0644 askremote.py %{buildroot}%{_libdir}/ask/

install -m0644 templates/* %{buildroot}%{_datadir}/ask/templates/

install -m0644 docs/*.1 %{buildroot}%{_mandir}/man1/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ChangeLog 
%doc docs/ask_doc.css docs/ask_doc.html docs/ask_doc.pdf docs/ask_doc.txt
%{_bindir}/asksetup
%{_bindir}/asksenders
%{_bindir}/askfilter
%{_libdir}/askversion.py
%{_libdir}/ask/askconfig.py
%{_libdir}/ask/asklock.py
%{_libdir}/ask/asklog.py
%{_libdir}/ask/askmail.py
%{_libdir}/ask/askmain.py
%{_libdir}/ask/askmessage.py
%{_libdir}/ask/askremote.py

%{_datadir}/ask/templates/ask.rc
%{_datadir}/ask/templates/ignorelist.txt
%{_datadir}/ask/templates/whitelist.txt
%{_datadir}/ask/templates/confirm_da.txt
%{_datadir}/ask/templates/confirm_de.txt
%{_datadir}/ask/templates/confirm_en.txt
%{_datadir}/ask/templates/confirm_es.txt
%{_datadir}/ask/templates/confirm_fi.txt
%{_datadir}/ask/templates/confirm_fr.txt
%{_datadir}/ask/templates/confirm_it.txt
%{_datadir}/ask/templates/confirm_nl.txt
%{_datadir}/ask/templates/confirm_ptbr.txt

%{_mandir}/man1/asksenders.1*
%{_mandir}/man1/asksetup.1*
%{_mandir}/man1/askfilter.1*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.3-8mdv2011.0
+ Revision: 609995
- rebuild

* Wed Mar 10 2010 Emmanuel Andry <eandry@mandriva.org> 2.5.3-7mdv2010.1
+ Revision: 517497
- fix licence and URL

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.5.3-6mdv2010.0
+ Revision: 423962
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.5.3-5mdv2009.0
+ Revision: 266185
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.5.3-4mdv2009.0
+ Revision: 205584
- Should not be noarch ed

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 11 2007 Emmanuel Andry <eandry@mandriva.org> 2.5.3-3mdv2008.0
+ Revision: 84466
- rebuild


* Sun Feb 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2.5.3-2mdv2007.0
+ Revision: 116141
- Rebuild
- Import ask

* Sun May 14 2006 Emmanuel Andry <eandry@mandriva.org> 2.5.3-1mdk
- 2.5.3
- mkrel

* Sat Aug 27 2005 Oden Eriksson <oeriksson@mandriva.com> 2.5.0-2mdk
- rebuild

* Thu Jul 01 2004 Spencer Anderson <sdander@oberon.ark.com> 2.5.0-1mdk
- new version

