# $Revision:$, $Date:$
%define         _state          stable
%define         orgname        	nepomuk-widgets
%define         qtver           4.8.3

Summary:	Nepomuk Widgets utilities and libraries
Name:		kde4-nepomuk-widgets
Version:	4.11.0
Release:	1
License:	LGPLv2 or LGPLv3
Group:		X11/Applications
URL:		http://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	e122a48eb6d16daae5c945651308a4f2
BuildRequires:	kde4-nepomuk-core-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nepomuk Widgets utilities.

%package devel
Summary:	Developer files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Nepomuk Widgets development files and libraries.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		-DHTML_INSTALL_DIR=%{_kdedocdir} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
		-DKDE4_ENABLE_FINAL=OFF \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnepomukwidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukwidgets.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/nepomuk2
%{_libdir}/cmake/NepomukWidgets
%attr(755,root,root) %{_libdir}/libnepomukwidgets.so
