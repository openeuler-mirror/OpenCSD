Summary        : An open source CoreSight(tm) Trace Decode library
Name           : OpenCSD
Version        : 1.3.3
Release        : 4
License        : BSD
Source         : %{name}-%{version}.tar.gz
BuildRoot      : %{_tmppath}/%{name}-%{version}-${release}-root
BuildRequires  : gcc-c++ make


%description
%{name} will decode formatted trace in three stages:
1. Frame Deformatting : Removal CoreSight frame formatting from individual trace streams.
2. Packet Processing : Separate individual trace streams into discrete packets.
3. Packet Decode : Convert the packets into fully decoded trace describing the program flow on a core.
The library is implemented in C++ with an optional "C" API.

%global debug_package %{nil}

%prep
%setup -q


%build
make CC=$CC CXX=$CXX -C decoder/build/linux CPPFLAGS="-fPIE" LDFLAGS="-s -pie -Wl,-z,defs" -j


%install
rm -rf %{buildroot}
make -C decoder/build/linux install PREFIX=%{buildroot}/usr LIB_PATH=lib64


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,0644)
%doc README.md LICENSE
%{_includedir}/opencsd
%{_libdir}/libopencsd*
%exclude %{_bindir}
%exclude %{_libdir}/*.a*


%changelog
* Thu Apr 27 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 1.3.3-4
- Fix CC compiler support

* Thu Mar 16 2023 huangfangrun <huangfangrun1@h-partners.com> - 1.3.3-3
- [Compile Option] Add -fPIE -s and -pie options

* Tue Feb 28 2023 liweiganga <liweiganga@uniontech.com> - 1.3.3-2
- fix #I6I3EM and #I6I31E

* Tue Jan 03 2023 Junhao He <hejunhao3@hauwei.com> - 1.3.3-1
- Package init
