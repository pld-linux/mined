Summary:	Mined is a Unicode-capable small and easy to use text editor
Summary(pl):	Mined jest korzystaj±cym z unikodu, ma³ym, prostym w u¿yciu edytorem
Name:		mined
Version:	2000.5
Release:	0.1
License:	GPL
Group:		Applications/Editors
Vendor:		Thomas Wolff <mined@towo.net>
Source0:	http://towo.net/mined/%{name}-%{version}.tar.gz
#Source1:	%{name}.desktop
#Source2:	%{name}.png
Patch0:		%{name}-makeinstall.patch
URL:		http://towo.net/mined/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mined is a text editor, small and easy to use, yet powerful. It is
Unicode-capable, using UTF-8 encoding (also converts UTF-16 input).
(It can also handle mixed 8/16 bit charsets as used for Chinese.)
It has mouse support (in text mode terminals), menus, a scrollbar and
visible indications of special characters (esp. TABs and different
line-ends).

%description -l pl
# TODO

%prep
%setup -q
%patch0 -p1

%build
cd src
%{__make} -f makefile.linux prefix=/usr \
		bindir=%{_bindir} \
		helpdir=%{_datadir}/mined \
		mandir=%{_mandir} \
		OPT="%{rpmcflags}" \
		%{!?debug:DEBUG=}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cd src
%{__make} -f makefile.linux install \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		helpdir=$RPM_BUILD_ROOT%{_datadir}/mined \
		mandir=$RPM_BUILD_ROOT%{_mandir}

#install -d %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors
#install -d %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README doc/*.html doc/*.gif doc/{configure-xterm,uterm,compilation}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
#%{_applnkdir}/Editors/*
#%{_pixmapsdir}/*
%{_mandir}/man1/*
