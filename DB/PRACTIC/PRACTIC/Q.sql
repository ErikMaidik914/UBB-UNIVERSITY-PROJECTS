USE [PRACTIC]

drop table Leases
drop table RealEstateAgents
drop table Properties
drop table Owners
DROP TABLE Payments
drop table Tenants


CREATE TABLE Owners
(
	OWNER_ID INT PRIMARY KEY,
	name VARCHAR(50),
	contact VARCHAR(50)
);

CREATE TABLE Properties
(
	PROPERTY_ID INT PRIMARY KEY,
	cathegory VARCHAR(50),
	adress VARCHAR(50),
	type VARCHAR(50),
	area VARCHAR(50),
	OWNER_ID INT,
	FOREIGN KEY (OWNER_ID) REFERENCES Owners(OWNER_ID),	
);


CREATE TABLE RealEstateAgents
(
	REALESTATEAGENT_ID INT PRIMARY KEY,
	name VARCHAR(50),
	birth DATE,
	email VARCHAR(50),
	company VARCHAR(50),
);



------------------------------------------------------


CREATE TABLE Tenants
(
	TENANT_ID INT PRIMARY KEY,
	name VARCHAR(50),
	contact VARCHAR(50),
	
);

CREATE TABLE Payments
(
	PAYMENT_ID INT PRIMARY KEY,
	method VARCHAR(50),
	status VARCHAR(50),
	pay_date DATE,
	TENANT_ID INT,
	FOREIGN KEY (TENANT_ID) REFERENCES Tenants(TENANT_ID),
	
);
------------------------------------------------------

CREATE TABLE Leases
(
	TENANT_ID INT,
	PROPERTY_ID INT,
	start_date DATE,
	end_date DATE, --'2021-12-25'
	rent INT,
	REALESTATEAGENT_ID INT,
    FOREIGN KEY (TENANT_ID) REFERENCES Tenants(TENANT_ID),
    FOREIGN KEY(PROPERTY_ID) REFERENCES Properties(PROPERTY_ID),
	CONSTRAINT Treats_ID Primary KEY(TENANT_ID,PROPERTY_ID),
	FOREIGN KEY (REALESTATEAGENT_ID) REFERENCES RealEstateAgents(REALESTATEAGENT_ID)
);

INSERT INTO Tenants (TENANT_ID,name, contact) VALUES 
(1, 'Alice', 'email1'), 
(2, 'Bob', 'email2'), 
(3, 'Charlie', 'email3'), 
(4, 'Dave', 'email4')
SELECT * FROM Tenants

INSERT INTO Payments (PAYMENT_ID,method, status, pay_date, TENANT_ID) VALUES 
(1, 'credit card','completed', '2024-12-25', 1), 
(2, 'bank transfer','completed', '2024-12-27', 2), 
(3, 'credit card','completed', '2024-12-28', 2), 
(4, 'credit card','completed', '2024-12-29', 3),
(5, 'bank transfer','new', '2024-12-26', 4)

SELECT * FROM Payments
SELECT * FROM Tenants