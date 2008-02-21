Name:           jhlabs-filters
Version:        2.0.235
Release:        %mkrel 0.0.1
Summary:        Java Image Filters
License:        Apache License
Group:          Development/Java
Url:            http://www.jhlabs.com/ip/filters/
Source0:        http://www.jhlabs.com/ip/filters/Filters.zip
Source1:        build.xml
BuildRequires:  jpackage-utils
BuildRequires:  java-rpmbuild 
BuildRequires:  ant
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The filters are all standard Java BufferedImageOps and can be plugged directly into existing programs. 

%package        javadoc
Summary:        Javadoc for %{oname}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c %{name}-%{version}
cp %{SOURCE1} build.xml
%remove_java_binaries

%build
%{ant} -f build.xml jar javadoc

%install
rm -rf %{buildroot}
install -m644 dist/Filters.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%create_jar_links

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}
