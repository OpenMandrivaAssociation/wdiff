Summary:	Word-based diff front end
Name:		wdiff
Version:	1.2.2
Release:	4
URL:		https://www.gnu.org/software/wdiff/wdiff.html
Source0:	https://ftp.gnu.org/gnu/wdiff/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Text tools
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	texinfo
BuildRequires:	help2man

%description
GNU wdiff is a front-end to GNU diff.  It compares two files, finding
which words have been deleted or added to the first in order to create
the second.  It has many output formats and interacts well with
terminals and pagers (notably with less).  GNU wdiff is particularly
useful when two texts differ only by a few words and paragraphs have
been refilled.


%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install
%find_lang %{name}
%find_lang %{name}-gnulib
cat %{name}-gnulib.lang >> %{name}.lang

%files -f %{name}.lang
%doc README NEWS THANKS TODO COPYING ChangeLog BACKLOG
%{_bindir}/wdiff
%{_mandir}/man1/wdiff.1*
%{_infodir}/wdiff.info*
