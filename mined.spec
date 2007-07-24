Summary:	Mined is a Unicode-capable small and easy to use text editor
Summary(pl.UTF-8):	Mined - korzystający z unikodu, mały, prosty w użyciu edytor
Name:		mined
Version:	2000.14
Release:	1
License:	GPL
Group:		Applications/Editors
Vendor:		Thomas Wolff <mined@towo.net>
#Source0Download:	http://towo.net/mined/download.html
Source0:	http://towo.net/mined/%{name}-%{version}.tar.gz
# Source0-md5:	829917760fa0cef2b8de91be8487169c
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

%description -l pl.UTF-8
Mined to edytor tekstu, mały i łatwy w użyciu, a jednak potężny.
Umożliwia korzystanie z unikodu przy użyciu kodowania UTF-8
(konwertuje też wejście w UTF-16; może także obsłużyć mieszane
8/16-bitowe zestawy znaków używane dla języka chińskiego). Ma obsługę
myszy (na terminalach tekstowych), menu, pasek przewijania i widoczne
oznaczenia znaków specjalnych (szczególnie TABów i różnych znaków
końca linii).

%prep
%setup -q
%patch0 -p1

%build
cd src
%{__make} -f makefile.linux \
	prefix=%{_prefix} \
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
%doc usrshare/package_doc/{README,CHANGES} doc/{*.html,*.gif}
%doc usrshare/{setup_install/bin/configure-xterm,bin/uterm}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
#%{_applnkdir}/Editors/*
#%{_pixmapsdir}/*
%{_mandir}/man1/*
