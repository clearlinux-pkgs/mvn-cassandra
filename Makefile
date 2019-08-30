PKG_NAME := mvn-cassandra
URL = https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-sources.jar
ARCHIVES = https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1.pom : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.1/cassandra-driver-core-3.0.1-shaded.jar : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-parent/3.0.1/cassandra-driver-parent-3.0.1.pom : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.jar : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-core/3.0.0/cassandra-driver-core-3.0.0.pom : https://repo.maven.apache.org/maven2/com/datastax/cassandra/cassandra-driver-parent/3.0.0/cassandra-driver-parent-3.0.0.pom :

include ../common/Makefile.common
