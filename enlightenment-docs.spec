Summary:	Enlightenment documentation
Summary(pl):	Dokumentacja dla Enlightenmenta
Name:		enlightenment-docs
Version:	0.16.7
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	2f5ca4bad4e995fd9594c23c95837fcc
# Source0-size:	1791137
URL:		http://enlightenment.org/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Documentation for Enlightenment in edox form.

%description -l pl
Dokumentacja dla Enlightenmenta w formie edox.

%prep
%setup  -q
rm E-docs/Makefile*
#it has to be in UTF-8, for ttf fonts to work
iconv -f ISO-8859-2 -t UTF-8 E-docs/MAIN.pl > E-docs/MAIN.pl-utf
mv -f E-docs/MAIN.pl{-utf,}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment

cp -a E-docs $RPM_BUILD_ROOT%{_datadir}/enlightenment

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/E-docs
