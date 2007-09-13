%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Name:		jhlabs-filters
Summary:	Java Image Processing Classes
Version:	0
Release:	%mkrel 1
URL:		http://www.jhlabs.com/ip/filters/index.html
Source:		http://www.jhlabs.com/ip/filters/Filters.zip
Group:		Development/Java
License:	ASL 2.0
%if ! %{gcj_support}
BuildArch:	noarch
%endif
BuildRequires:	ant java-devel-icedtea
%if %{gcj_support}
BuildRequires:	java-gcj-compat-devel
Requires(post):	java-gcj-compat
Requires(postun):	java-gcj-compat
%endif
%description
Java Image Processing Classes.

%prep
%setup -q -c filters
%{__find} . -name '*.jar' -or -name '*.class' -exec %{__rm} -f {} \;

%build
%ant

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/Filters.jar %{buildroot}%{_javadir}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%{_javadir}/Filters.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif

