/*
die db"secret_intel" hab ich manuel im terminal erstellt. 
und mit "mysql -u root -p secret_intel < secretIntel.sql"
die "TABLE" creiert
*/
USE secret_intel;

CREATE TABLE Squad (
	sid SMALLINT NOT NULL AUTO_INCREMENT,
	squadName VARCHAR(100),
	homeTown VARCHAR(100),
	formed SMALLINT,
	amigood VARCHAR(20),
	secretBase VARCHAR(100),
	active BOOLEAN,
	PRIMARY KEY (sid)
);

CREATE TABLE Member (
	mid SMALLINT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100),
	age INT(255),
	secretIdentity VARCHAR(100),
	sid SMALLINT,
	PRIMARY KEY (mid),
	FOREIGN KEY (sid) REFERENCES Squad (sid)
);

CREATE TABLE Power (
	pid SMALLINT NOT NULL AUTO_INCREMENT,
	powerName VARCHAR(100),
	mid SMALLINT,
	PRIMARY KEY (pid),
	FOREIGN KEY (mid) REFERENCES Member (mid)
);
