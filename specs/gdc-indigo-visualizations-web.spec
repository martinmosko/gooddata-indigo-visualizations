%global gdc_prefix /var/www/doc

Name: gdc-indigo-visualizations-web
Version: 3.%{gdcversion}
Release: 1%{dist}
Summary: GDC Indigo Visualizations Web

Group: Applications/Productivity
License: Proprietary
URL: https://github.com/gooddata/gdc-indigo-visualizations
Source0: %{name}.tar.gz
BuildArch: noarch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if "%{?dist}" == ".el6"
BuildRequires:  nodejs < 5.0, npm < 4, git
%else
BuildRequires:  nodejs > 1:6.0, nodejs < 1:7.0, npm > 3.10, git
%endif

%description
%{summary}

%prep
%setup -q -n %{name} -c

%build
export PATH="$PATH:$PWD/node_modules/.bin/"
node --version
npm --version
. ci/lib.sh
grunt web

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{gdc_prefix}/indigo-visualizations
cp -a web/* $RPM_BUILD_ROOT%{gdc_prefix}/indigo-visualizations/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%dir %{gdc_prefix}/indigo-visualizations
%{gdc_prefix}/indigo-visualizations/*

%changelog