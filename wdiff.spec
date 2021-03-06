Summary:	Word-based diff front end
Name:		wdiff
Version:	1.2.2
Release:	3
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
rm -rf %{buildroot} *.lang
%makeinstall
%find_lang %{name}
%find_lang %{name}-gnulib
cat %{name}-gnulib.lang >> %{name}.lang



%files -f %{name}.lang
%doc README NEWS THANKS TODO COPYING ChangeLog BACKLOG
%{_bindir}/wdiff
%{_mandir}/man1/wdiff.1*
%{_infodir}/wdiff.info*


