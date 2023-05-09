%bcond_without check
%global debug_package %{nil}

%global crate aho-corasick

Name:           rust-aho-corasick
Version:        1.0.1
Release:        1
Summary:        Fast multiple substring searching

License:        Unlicense OR MIT
URL:            https://crates.io/crates/aho-corasick
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(memchr) >= 2.4.0 with crate(memchr) < 3.0.0~)
BuildRequires:  (crate(memchr/std) >= 2.4.0 with crate(memchr/std) < 3.0.0~)
%if %{with check}
BuildRequires:  (crate(doc-comment/default) >= 0.3.3 with crate(doc-comment/default) < 0.4.0~)
%endif

%global _description %{expand:
Fast multiple substring searching.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(aho-corasick) = 1.0.1
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(aho-corasick/default) = 1.0.1
Requires:       cargo
Requires:       crate(aho-corasick) = 1.0.1
Requires:       crate(aho-corasick/perf-literal) = 1.0.1
Requires:       crate(aho-corasick/std) = 1.0.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(aho-corasick/logging) = 1.0.1
Requires:       (crate(log/default) >= 0.4.17 with crate(log/default) < 0.5.0~)
Requires:       cargo
Requires:       crate(aho-corasick) = 1.0.1

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+perf-literal-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(aho-corasick/perf-literal) = 1.0.1
Requires:       (crate(memchr) >= 2.4.0 with crate(memchr) < 3.0.0~)
Requires:       cargo
Requires:       crate(aho-corasick) = 1.0.1

%description -n %{name}+perf-literal-devel %{_description}

This package contains library source intended for building other packages which
use the "perf-literal" feature of the "%{crate}" crate.

%files       -n %{name}+perf-literal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(aho-corasick/std) = 1.0.1
Requires:       (crate(memchr/std) >= 2.4.0 with crate(memchr/std) < 3.0.0~)
Requires:       cargo
Requires:       crate(aho-corasick) = 1.0.1

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
