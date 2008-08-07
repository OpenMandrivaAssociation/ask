%define name	ask
%define version	2.5.3
%define release	%mkrel 5

Summary:	Active Spam Killer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
URL:		http://www.paganini.net/ask-2.4
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


