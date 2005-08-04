%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	IPv6
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - check and validate IPv6 addresses
Summary(pl):	%{_pearname} - sprawdzanie poprawno¶ci adresów IPv6
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	438594e605140247dd510b12a3878f6f
URL:		http://pear.php.net/package/Net_IPv6/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class allows you to:
- check if an address is an IPv6 address
- compress/uncompress IPv6 addresses
- check for an IPv4 compatible ending in an IPv6 address

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na:
- sprawdzenie czy dany adres jest adresem IPv6
- kompresjê/dekompresjê adresu IPv6
- sprawdzenie czy koñcówka adresu IPv6 jest kompatybilna z IPv4

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
