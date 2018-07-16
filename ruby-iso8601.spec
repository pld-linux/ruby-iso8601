#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	iso8601
Summary:	Ruby parser to work with ISO 8601 dateTimes and durations - http://en.wikipedia.org/wiki/ISO_8601
Name:		ruby-%{pkgname}
Version:	0.9.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c06e3b9f98b233274b5f52f02e970332
URL:		https://github.com/arnau/ISO8601
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-pry < 0.11
BuildRequires:	ruby-pry >= 0.10.3
BuildRequires:	ruby-pry-doc < 0.9
BuildRequires:	ruby-pry-doc >= 0.8.0
BuildRequires:	ruby-rspec < 4
BuildRequires:	ruby-rspec >= 3.4
BuildRequires:	ruby-rubocop < 1
BuildRequires:	ruby-rubocop >= 0.40
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO8601 is a simple implementation in Ruby of the ISO 8601 (Data
elements and interchange formats - Information interchange -
Representation of dates and times) standard.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
