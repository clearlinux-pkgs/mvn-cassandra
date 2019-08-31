#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-cassandra
Version  : 1
Release  : 3
URL      : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-sources.jar
Source0  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-sources.jar
Source1  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.jar
Source2  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.pom
Source3  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-shaded.jar
Source4  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1.pom
Source5  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-parent/3.0.0/cassandra-driver-parent-3.0.0.pom
Source6  : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-parent/3.0.1/cassandra-driver-parent-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-cassandra-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-cassandra package.
Group: Data

%description data
data components for the mvn-cassandra package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-shaded.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.0/cassandra-driver-parent-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.1/cassandra-driver-parent-3.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.jar
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.pom
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-shaded.jar
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-sources.jar
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1.pom
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.0/cassandra-driver-parent-3.0.0.pom
/usr/share/java/.m2/repository/com/datastax/cassandra/cassandra-driver-parent/3.0.1/cassandra-driver-parent-3.0.1.pom
