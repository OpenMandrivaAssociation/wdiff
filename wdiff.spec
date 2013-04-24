%define name wdiff
%define version 1.1.2
%define release %mkrel 1

Summary:	Word-based diff front end
Name:		wdiff
Version:	%version
Release:	%release
URL:		http://www.gnu.org/software/wdiff/wdiff.html
Source0:	ftp://ftp.gnu.org/pub/gnu/wdiff/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Text tools
BuildRequires:	termcap-devel
BuildRequires:	texinfo

%description
GNU wdiff is a front-end to GNU diff.  It compares two files, finding
which words have been deleted or added to the first in order to create
the second.  It has many output formats and interacts well with
terminals and pagers (notably with less).  GNU wdiff is particularly
useful when two texts differ only by a few words and paragraphs have
been refilled.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot *.lang
%makeinstall
%find_lang %name
%find_lang %name-gnulib
cat %name-gnulib.lang >> %name.lang



%files -f %name.lang
%doc README NEWS THANKS TODO COPYING ChangeLog BACKLOG
%{_bindir}/wdiff
%_mandir/man1/wdiff.1*
%{_infodir}/wdiff.info*


%changelog
* Thu May 31 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 801526
- version update 1.1.2

* Mon May 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 800970
- version update 1.1.1

* Sat Nov 19 2011 Götz Waschk <waschk@mandriva.org> 1.1.0-1
+ Revision: 731831
- new version

* Tue Sep 20 2011 Götz Waschk <waschk@mandriva.org> 1.0.1-1
+ Revision: 700492
- new version

* Sun Sep 11 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-1
+ Revision: 699393
- new version
- update to new version 1.0.0

* Tue Dec 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.5-1mdv2011.0
+ Revision: 614425
- 0.6.5
- spec cleanup
- correct use of %%buildroot
- fix source0

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2011.0
+ Revision: 550276
- update to new version 0.6.3

* Sun Apr 04 2010 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 531349
- new version
- drop patch
- update file list

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 0.5-9mdv2010.0
+ Revision: 395464
- spec fix
- update license

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.5-8mdv2009.0
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 11 2007 Götz Waschk <waschk@mandriva.org> 0.5-8mdv2008.0
+ Revision: 51178
- Import wdiff

