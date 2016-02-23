%{?scl:%scl_package nodejs-realize-package-specifier}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-realize-package-specifier

%global npm_name realize-package-specifier
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-realize-package-specifier
Version:	3.0.1
Release:	2%{?dist}
Summary:	Like npm-package-arg, but more so, producing full file paths and differentiating local tar and directory sources.
Url:		https://github.com/npm/realize-package-specifier
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(require-inject)
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}npm(dezalgo)
BuildRequires:	%{?scl_prefix}npm(npm-package-arg)

Requires:	%{?scl_prefix}npm(dezalgo)
Requires:	%{?scl_prefix}npm(npm-package-arg)

%description
Like npm-package-arg, but more so, producing full file paths and differentiating local tar and directory sources.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/realize-package-specifier

%doc README.md
%doc LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-2
- rebuilt

* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-1
- Initial build
