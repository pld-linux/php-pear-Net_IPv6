%define		_status		stable
%define		_pearname	Net_IPv6
%define		snap		b4
Summary:	%{_pearname} - check and validate IPv6 addresses
Summary(pl.UTF-8):	%{_pearname} - sprawdzanie poprawności adresów IPv6
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	0.%{snap}.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{snap}.tgz
# Source0-md5:	ce65df2c910333711a528bf85e68226d
Patch0:		ipv6.patch
URL:		http://pear.php.net/package/Net_IPv6/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class allows you to:
- check if an address is an IPv6 address
- compress/uncompress IPv6 addresses
- check for an IPv4 compatible ending in an IPv6 address

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala na:
- sprawdzenie czy dany adres jest adresem IPv6
- kompresję/dekompresję adresu IPv6
- sprawdzenie czy końcówka adresu IPv6 jest kompatybilna z IPv4

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}
%patch0 -p1
cd -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/IPv6.php
