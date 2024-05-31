%global _scl_prefix /opt/
%global _scl_vendor pokemon-studio
%global scl pokemon-studio
%global scl_prefix pokemon-studio-
%global scl_name %scl     
%global macrosdir        %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_root_sysconfdir}/rpm; echo $d)
%global install_scl      1
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global rh_layout        1
%endif

%if 0%{?fedora} >= 20 && 0%{?fedora} < 27
# Requires scl-utils v2 for SCL integration, dropeed in F29
%global with_modules     1
%else
# Works with file installed in /usr/share/Modules/modulefiles/
%global with_modules     0
%endif

%scl_package %scl

# do not produce empty debuginfo package
%global debug_package %{nil}
%define osstring %(source /etc/os-release; echo ${NAME})
%if 0%{?rhel} <= 5
%define epelstring %(echo epel-release)
%endif
%if 0%{?fedora} <= 35
%define epelstring %(echo fedora-release)
%endif

Summary: Package that installs %scl
Name: %scl_name
Version: 2.2.0
Release: 2%{?dist}
License: PokemonStudio
Group: Applications/File
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0: https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/pokemon-studio-scl/macros-build
Source1: https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/pokemon-studio-scl/README
Source2: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/LICENSE.md
Source3: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/LICENSE-SIMPLIFIED.md
Source4: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/LICENSE-FR.md
Source5: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/LICENSE-FR-SIMPLIFIEE.md
Source6: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/CONTRIBUTING.md
Source7: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/CodeGuidelines.md
Source8: https://github.com/PokemonWorkshop/PokemonStudio/raw/develop/EPIC_Cleanup_responsibility_of_Studio.md
Source9: https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/pokemon-studio-scl/macros-build
Source10: https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/pokemon-studio-scl/pokemon-studio.desktop
Source11: https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/pokemon-studio-scl/pokemon-studio.sh
BuildRequires: scl-utils-build
BuildRequires: help2man
# Temporary work-around
BuildRequires: iso-codes
BuildRequires: environment-modules
Requires: %{?scl_name}-runtime%{?_isa} = %{version}-%{release}
Requires: %{scl_prefix}pokemon-studio
Obsoletes: %{name} < %{version}-%{release}
%if 0%{?rhel} <= 5
BuildRequires:  %{epelstring}
Requires:  %{epelstring}
%endif
%if "%{osstring}" == "CentOS Stream"
BuildRequires:  epel-next-release
Requires:  epel-next-release
%endif

%description
This is the main package for %scl Software Collection.

%package runtime
Summary:   Package that handles %scl Software Collection.
Group:     Development/Languages
Requires:  scl-utils
Requires:  environment-modules
Requires(post): %{_root_sbindir}/semanage
Requires(post): %{_root_sbindir}/selinuxenabled
Provides:  %{?scl_name}-runtime(%{scl_vendor})
Provides:  %{?scl_name}-runtime(%{scl_vendor})%{?_isa}

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary:   Package shipping basic build configuration
Group:     Development/Languages
Requires:  scl-utils-build
Requires(post): %{_root_sbindir}/semanage
Requires(post): %{_root_sbindir}/selinuxenabled
Provides:  %{?scl_name}-runtime(%{scl_vendor})
Provides:  %{?scl_name}-runtime(%{scl_vendor})%{?_isa}

%description build
Package shipping essential configuration macros
to build %scl Software Collection.

%package scldevel
Summary:   Package shipping development files for %scl
Group:     Development/Languages
Requires(post): %{_root_sbindir}/semanage
Requires(post): %{_root_sbindir}/selinuxenabled
Provides:  %{?scl_name}-runtime(%{scl_vendor})
Provides:  %{?scl_name}-runtime(%{scl_vendor})%{?_isa}

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.

%prep
%setup -c -T

cat <<EOF | tee enable
export PATH=%{_bindir}:%{_sbindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}\${MANPATH:+:\${MANPATH}}
export INFOPATH=%{_infodir}\${INFOPATH:+:\${INFOPATH}}
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
EOF

# generate rpm macros file for depended collections
cat << EOF | tee scldev
%%scl_%{scl_name_base}         %{scl}
%%scl_prefix_%{scl_name_base}  %{scl_prefix}
EOF

# This section generates README file from a template and creates man page
# from that file, expanding RPM macros in the template file.
cat <<'EOF' | tee README
%{expand:%(cat %{SOURCE0})}
EOF

%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} Software Collection (PHP %{version})" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7


%install
mkdir -p %{buildroot}%{_scl_scripts}/
install -D -m 644 enable %{buildroot}%{_scl_scripts}/enable
mkdir -p %{buildroot}%{macrosdir}/
install -D -m 644 scldev %{buildroot}%{macrosdir}/macros.%{scl_name_base}-scldevel
mkdir -p %{buildroot}/usr/share/man/man7/
install -D -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/%{scl_name}.7
install -D -m 644 %{scl_name}.7 %{buildroot}/usr/share/man/man7/%{scl_name}.7
mkdir -p %{buildroot}%{_datadir}/licenses/PokemonStudio/
install -D -m 777 %{SOURCE1} %{buildroot}%{_datadir}/licenses/PokemonStudio/
install -D -m 777 %{SOURCE2} %{buildroot}%{_datadir}/licenses/PokemonStudio/
install -D -m 777 %{SOURCE3} %{buildroot}%{_datadir}/licenses/PokemonStudio/
install -D -m 777 %{SOURCE4} %{buildroot}%{_datadir}/licenses/PokemonStudio/
mkdir -p %{buildroot}/usr/share/licenses/PokemonStudio/
install -D -m 777 %{SOURCE1} %{buildroot}/usr/share/licenses/PokemonStudio/
install -D -m 777 %{SOURCE2} %{buildroot}/usr/share/licenses/PokemonStudio/
install -D -m 777 %{SOURCE3} %{buildroot}/usr/share/licenses/PokemonStudio/
install -D -m 777 %{SOURCE4} %{buildroot}/usr/share/licenses/PokemonStudio/
mkdir -p %{buildroot}%{_datadir}/PokemonStudio/
install -D -m 777 %{SOURCE5} %{buildroot}%{_datadir}/PokemonStudio/
install -D -m 777 %{SOURCE6} %{buildroot}%{_datadir}/PokemonStudio/
install -D -m 777 %{SOURCE7} %{buildroot}%{_datadir}/PokemonStudio/
mkdir -p %{buildroot}/usr/share/PokemonStudio/
install -D -m 777 %{SOURCE5} %{buildroot}/usr/share/PokemonStudio/
install -D -m 777 %{SOURCE6} %{buildroot}/usr/share/PokemonStudio/
install -D -m 777 %{SOURCE7} %{buildroot}/usr/share/PokemonStudio/
mkdir -p %{buildroot}%{_datadir}/applications/
install -D -m 777 %{SOURCE9} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}/usr/share/applications/
install -D -m 777 %{SOURCE9} %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}%_scl_prefix
%scl_install
install -d -m 755 %{buildroot}%{macrosdir}/
cat %{SOURCE8} > %{buildroot}%{macrosdir}/macros.%{scl}-config
chmod 777 %{buildroot}%{macrosdir}/macros.%{scl}-config
cp %{SOURCE10} ./
shc -v -r -f pokemon-studio.sh
mv pokemon-studio.sh.x pokemon-studio
mkdir -p %{buildroot}%{_bindir}/
install -D -m 777 pokemon-studio %{buildroot}%{_bindir}/
mkdir -p %{buildroot}/usr/bin/
install -D -m 777 pokemon-studio %{buildroot}/usr/bin/
mkdir -p %{buildroot}%_scl_prefix/%_scl_vendor
install -D -m 777 enable %{buildroot}%_scl_prefix/%_scl_vendor

%if 0%{?fedora} < 19 && 0%{?rhel} < 7
%files runtime
/etc/rpm/macros.pokemon-studio-config
/usr/bin/pokemon-studio
/usr/share/applications/pokemon-studio.desktop
%_scl_prefix/%_scl_vendor/enable
%{_datadir}/PokemonStudio/CONTRIBUTING.md
%{_datadir}/PokemonStudio/CodeGuidelines.md
%{_datadir}/PokemonStudio/EPIC_Cleanup_responsibility_of_Studio.md
%{_datadir}/licenses/PokemonStudio/LICENSE-FR-SIMPLIFIEE.md
%{_datadir}/licenses/PokemonStudio/LICENSE-FR.md
%{_datadir}/licenses/PokemonStudio/LICENSE-SIMPLIFIED.md
%{_datadir}/licenses/PokemonStudio/LICENSE.md
/usr/share/PokemonStudio/CONTRIBUTING.md
/usr/share/PokemonStudio/CodeGuidelines.md
/usr/share/PokemonStudio/EPIC_Cleanup_responsibility_of_Studio.md
/usr/share/licenses/PokemonStudio/LICENSE-FR-SIMPLIFIEE.md
/usr/share/licenses/PokemonStudio/LICENSE-FR.md
/usr/share/licenses/PokemonStudio/LICENSE-SIMPLIFIED.md
/usr/share/licenses/PokemonStudio/LICENSE.md
/usr/share/man/man7/pokemon-studio.7.gz
%else
%files runtime -f filesystem
/etc/rpm/macros.pokemon-studio-config
/usr/bin/pokemon-studio
/usr/share/applications/pokemon-studio.desktop
%{_datadir}/PokemonStudio/CONTRIBUTING.md
%{_datadir}/PokemonStudio/CodeGuidelines.md
%{_datadir}/PokemonStudio/EPIC_Cleanup_responsibility_of_Studio.md
%{_datadir}/licenses/PokemonStudio/LICENSE-FR-SIMPLIFIEE.md
%{_datadir}/licenses/PokemonStudio/LICENSE-FR.md
%{_datadir}/licenses/PokemonStudio/LICENSE-SIMPLIFIED.md
%{_datadir}/licenses/PokemonStudio/LICENSE.md
/usr/share/PokemonStudio/CONTRIBUTING.md
/usr/share/PokemonStudio/CodeGuidelines.md
/usr/share/PokemonStudio/EPIC_Cleanup_responsibility_of_Studio.md
/usr/share/licenses/PokemonStudio/LICENSE-FR-SIMPLIFIEE.md
/usr/share/licenses/PokemonStudio/LICENSE-FR.md
/usr/share/licenses/PokemonStudio/LICENSE-SIMPLIFIED.md
/usr/share/licenses/PokemonStudio/LICENSE.md
/usr/share/man/man7/pokemon-studio.7.gz
%endif
#"""###""%defattr(-,root,root)
#%scl_files
#%{_root_mandir}/man7/%{scl_name}.*
#%{?_licensedir:%{_datadir}/licenses}
#%if 0%{?fedora} < 26 && 0%{?rhel} < 8
#%{_root_sysconfdir}/opt/%{scl_vendor}/%{scl}
#%{_root_localstatedir}/opt/%{scl_vendor}/%{scl}
#%endif


%files build
%defattr(-,root,root)
%{macrosdir}/macros.%{scl}-config


%files scldevel
%defattr(-,root,root)
%{macrosdir}/macros.%{scl_name_base}-scldevel

%changelog
* Mon May 21 2024 andykimpe
- init package
