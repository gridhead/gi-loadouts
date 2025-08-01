%global         hyphen gi-loadouts
%global         actual gi_loadouts
%global         identity net.gridhead.gi-loadouts

Name:           %{hyphen}
Version:        0.1.9
Release:        1%{?dist}
Summary:        Loadouts for Genshin Impact

License:        GPL-3.0-or-later
URL:            https://github.com/gridhead/%{hyphen}
Source0:        %{pypi_source %{actual}}
Patch0:         dependencies.diff

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       python3-pillow-qt
Requires:       python3-pyside6
Requires:       hicolor-icon-theme

%description
This is a desktop application that allows travelers to manage their custom
equipment of artifacts and weapons for playable characters and makes it
convenient for travelers to calculate the associated statistics based on their
equipment using the semantic understanding of how the gameplay works. Travelers
can create their bespoke loadouts consisting of characters, artifacts and
weapons and share them with their fellow travelers. Supported file formats
include a human-readable Yet Another Markup Language (YAML) serialization
format and a JSON-based Genshin Open Object Definition (GOOD) serialization
format.

%prep
%autosetup -n %{actual}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{actual}
install -Dm644 %{buildroot}%{python3_sitelib}/%{actual}/pack/%{identity}.desktop %{buildroot}%{_datadir}/applications/%{identity}.desktop
install -Dm644 %{buildroot}%{python3_sitelib}/%{actual}/pack/%{identity}.metainfo.xml %{buildroot}%{_metainfodir}/%{identity}.metainfo.xml
install -Dm644 %{buildroot}%{python3_sitelib}/%{actual}/pack/%{identity}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{identity}.svg

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{identity}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{identity}.metainfo.xml

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_metainfodir}/%{identity}.metainfo.xml
%{_datadir}/applications/%{identity}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{identity}.svg

%changelog
* Sat Jul 12 2025 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.9-1
- Version 0.1.9 release of Loadouts for Genshin Impact
- Announcement - https://gridhead.net/loadouts-for-genshin-impact-v0-1-9-released/