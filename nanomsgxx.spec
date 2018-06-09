Name:           nanomsgxx
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        Nanomsg binding for C++11
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/achille-roussel/nanomsgxx
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc-c++
BuildRequires:  nanomsg-devel

%description

nanomsgxx is a binding of the nanomsg library for C++11.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
./waf configure --prefix=/usr
./waf build

%install
./waf install  --destdir=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README.md
/usr/lib/lib*.so

%files devel
%defattr(-,root,root)
%{_includedir}/*
/usr/lib/lib*.so
/usr/lib/pkgconfig/*.pc

%changelog

