Name:           jhlabs-filters
Version:        2.0.235
Release:        0.0.6
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
The filters are all standard Java BufferedImageOps
and can be plugged directly into existing programs. 

%package        javadoc
Summary:        Javadoc for %{name}
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.235-0.0.4mdv2011.0
+ Revision: 619826
- the mass rebuild of 2010.0 packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.0.235-0.0.3mdv2010.0
+ Revision: 436047
- rebuild

* Thu Feb 21 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.235-0.0.2mdv2008.1
+ Revision: 173720
- bump release
- fix javadoc package summary

* Thu Feb 21 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.235-0.0.1mdv2008.1
+ Revision: 173708
- add build.xml
- clean spec file

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Wed Sep 19 2007 Nicolas Vigier <nvigier@mandriva.com> 0-2mdv2008.0
+ Revision: 90640
- rebuild

* Thu Sep 13 2007 Nicolas Vigier <nvigier@mandriva.com> 0-1mdv2008.0
+ Revision: 85209
- Import jhlabs-filters

