Summary:	-
Summary(pl):	-
Name:		mined
Version:	2000.5
Release:	0.1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		-
Vendor:		-
Icon:		-
Source0:	http://towo.net/mined/%{name}-%{version}.tar.gz
URL:		http://towo.net/mined/
BuildRequires:	-
PreReq:		-
Requires:	-
Requires(pre,post):	-
Requires(preun):	-
Requires(postun):	-
Provides:	-
Obsoletes:	-
Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
