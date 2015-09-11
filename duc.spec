Name:           duc
Version:        1.3.3
Release:        3%{?dist}
Summary:        Duc, a library and suite of tools for inspecting disk usage
Group:		Applications/System
License:        GNU General Public License
URL:            https://github.com/zevv/duc
Source0:        %{name}-%{version}.tar.gz
Patch1:		duc-1.3.3-html-fixes.patch
Patch2:		duc-1.3.3-no-header.patch
Patch3:     duc-1.3.3-no-css.patch
BuildArch:      x86_64
BuildRequires:  libtool autoconf
BuildRequires:  pango-devel cairo-devel tokyocabinet-devel
BuildRequires:	ncurses-devel

%description
Duc is a small library and a collection of tools for inspecting and visualizing
disk usage.

Duc maintains a database of accumulated sizes of directories of your file system,
and allows you to query this database with some tools,
or create fancy graphs showing you where your bytes are.

%prep
%setup -q
%patch1 -p1 -b htmlfixes
%patch2 -p1 -b noheader
%patch3 -p1 -b noheader

%build
autoreconf --install
%configure --disable-x11 --enable-ui
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%{_libdir}/*.so*
%{_mandir}/man1/duc*
%{_bindir}/%{name}

%changelog
* Thu Sep 10 2015 ClearFoundation <developer@clearfoundation.com> - 1.3.3-3
- Added no CSS patch

* Mon Jun 22 2015 ClearFoundation <developer@clearfoundation.com> - 1.3.3-2
- Added patch for HTML cleanup
- Added no-header patch for wrapping CGI inside ClearOS webconfig

* Thu Jun 18 2015 ClearFoundation <developer@clearfoundation.com> - 1.3.3-1
- Initial build for ClearOS 7

* Wed Feb 11 2015 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0
- first version
