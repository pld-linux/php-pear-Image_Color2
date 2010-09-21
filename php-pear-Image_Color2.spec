%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Image_Color2
Summary:	%{_pearname} - Color conversion and mixing for PHP5
Summary(pl.UTF-8):	%{_pearname} - Konwersja i mieszanie kolorów w PHP5
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6858768259ef6d96a22046be1ec71007
URL:		http://pear.php.net/package/Image_Color2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP5 color conversion and basic mixing. Currently supported color
models:
- CMYK - Used in printing.
- Grayscale - Perceptively weighted grayscale.
- Hex - Hex RGB colors i.e. #abcdef.
- Hsl - Used in CSS3 to define colors.
- Hsv - Used by Photoshop and other graphics pacakges.
- Named - RGB value for named colors like black, khaki, etc.
- WebsafeHex - Just like Hex but rounds to websafe colors.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta dostarcza metod do konwersji i mieszania kolorów. Aktualnie
wspierane modele kolorów:
- CMYK - wykorzystywane w drukowaniu,
- skala szarości,
- hex - kolory RGB przedstawione szesnastkowo, np. #abcdef,
- hsl - wykorzystywane w CSS3 do definiowania kolorów,
- hsv - wykorzystywane w Photoshopie oraz innych programach
  graficznych,
- słowne - słowne określenia dla wartości RGB, np. 'black' (czarny),
  'khaki'
- websafehex - tak jak hex, ale ograniczone do kolorów bezpiecznych
  dla stron internetowych

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/Color2
%{php_pear_dir}/Image/Color2.php
