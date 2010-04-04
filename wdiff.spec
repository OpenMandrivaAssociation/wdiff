%define name wdiff
%define version 0.6.1
%define release %mkrel 1

Summary: Word-based diff front end
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnu.org/pub/gnu/wdiff/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libtermcap-devel
BuildRequires: texinfo
URL: http://www.gnu.org/software/wdiff/wdiff.html

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
rm -rf $RPM_BUILD_ROOT *.lang
%makeinstall
%find_lang %name
%find_lang %name-gnulib
cat %name-gnulib.lang >> %name.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS THANKS TODO COPYING ChangeLog BACKLOG
%{_bindir}/wdiff
%_mandir/man1/wdiff.1*
%{_infodir}/wdiff.info*
