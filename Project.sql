--EZ RENTALS
SET SERVEROUTPUT ON;

CREATE TABLE VEHICLES(
    V_ID INT NOT NULL,
    V_NAME VARCHAR(20),
    HOURLY_RATE NUMBER(4),
    DAILY_RATE NUMBER(4),
    PRIMARY KEY(V_ID)
);

CREATE TABLE CUSTOMERS(
    C_NAME VARCHAR (20),
    REG NUMBER(7),
    st_name VARCHAR (20),
    v VARCHAR(20)
);

-- drop table customers;

INSERT ALL 
INTO VEHICLES VALUES (1,'BI-CYCLE',4,20)
INTO VEHICLES VALUES (2,'E-BIKE',7,28)
INTO VEHICLES VALUES (3,'GEAR BIKE',5,22)
INTO VEHICLES VALUES (4,'SPORTS BIKE',6,25)
SELECT *FROM DUAL;

SELECT CONCAT('$',HOURLY_RATE) AS HOURLY_RATE, CONCAT('$',DAILY_RATE) AS DAILY_RATE FROM VEHICLES;

SELECT *FROM CUSTOMERS;

CREATE TABLE STATIONS(
    S_ID INT NOT NULL,
    S_NAME VARCHAR2(30),
    LOCATION VARCHAR2(50),
    V_ID INT,
    PRIMARY KEY(S_ID),
    FOREIGN KEY (V_ID) REFERENCES VEHICLES(V_ID)
);


INSERT ALL
INTO STATIONS VALUES (1,'S1','HOSTELS',1)
INTO STATIONS VALUES (2,'S1','HOSTELS',1)
INTO STATIONS VALUES (3,'S1','HOSTELS',2)
INTO STATIONS VALUES (4,'S1','HOSTELS',2)
INTO STATIONS VALUES (5,'S1','HOSTELS',3)
INTO STATIONS VALUES (6,'S1','HOSTELS',4)
INTO STATIONS VALUES (7,'S1','HOSTELS',4)
INTO STATIONS VALUES (8,'S2','TUC',1)
INTO STATIONS VALUES (9,'S2','TUC',1)
INTO STATIONS VALUES (10,'S2','TUC',2)
INTO STATIONS VALUES (11,'S2','TUC',2)
INTO STATIONS VALUES (12,'S2','TUC',3)
INTO STATIONS VALUES (13,'S2','TUC',3)
INTO STATIONS VALUES (14,'S2','TUC',4)
INTO STATIONS VALUES (15,'S2','TUC',4)
SELECT *FROM DUAL;


INSERT ALL
INTO STATIONS VALUES (16,'S3','FCSE',1)
INTO STATIONS VALUES (17,'S3','FCSE',1)
INTO STATIONS VALUES (18,'S3','FCSE',2)
INTO STATIONS VALUES (19,'S3','FCSE',2)
INTO STATIONS VALUES (20,'S3','FCSE',3)
INTO STATIONS VALUES (21,'S3','FCSE',4)
INTO STATIONS VALUES (22,'S3','FCSE',4)
INTO STATIONS VALUES (23,'S4','ACB',1)
INTO STATIONS VALUES (24,'S4','ACB',1)
INTO STATIONS VALUES (25,'S4','ACB',2)
INTO STATIONS VALUES (26,'S4','ACB',2)
INTO STATIONS VALUES (27,'S4','ACB',3)
INTO STATIONS VALUES (28,'S4','ACB',3)
INTO STATIONS VALUES (29,'S4','ACB',4)
INTO STATIONS VALUES (30,'S4','ACB',4)
SELECT *FROM DUAL;



--INPUT
SELECT *FROM VEHICLES WHERE V_ID=&V_ID;

-- dbms_output.put_line('name:');

-- CREATE OR REPLACE PROCEDURE Insert_CUSTOMERS 
-- AS
--    i int;
--    n varchar2(20); 
--    r NUMBER(7);
-- BEGIN 
--     dbms_output.put_line('ID:'|| (SELECT COUNT(C_ID) FROM CUSTOMERS) );
--     i := &i;
--     i := i +1;
--     insert into CUSTOMERS values (i,n,r);
-- END; 
-- /

CREATE OR REPLACE PROCEDURE Insert_CUSTOMERS(i in int,n in VARCHAR2,r in NUMBER)
AS
   i int;
   n varchar2(20); 
   r NUMBER(7);
BEGIN 
    select count(c_id) into i from CUSTOMERS;
    i := i + 1;
    insert into CUSTOMERS values (i,n,r);
END; 
/

create or replace function ret_id
return int
is
    i int;
BEGIN
    select count(c_id) into i from CUSTOMERS;
    i := i + 1;
    return i;
end;
/

EXECUTE Insert_CUSTOMERS;

-- select count(O_id) from ORDERS;

-- CREATE VIEW V AS (SELECT V_ID FROM VEHICLES WHERE V_NAME = &V_NAME);

CREATE OR REPLACE PROCEDURE USER_RECORD
AS
    OD INT;
    CD INT,
    SD INT;
    VD INT;
BEGIN
    SELECT COUNT(O_ID) INTO OD FROM ORDERS;
    OD := OD + 1;

    SELECT C_ID INTO CD FROM (SELECT *FROM CUSTOMERS
    ORDER BY C_ID DESC) WHERE ROWNUM = 1; 

    SELECT S_ID INTO SD,V_ID INTO VD FROM (SELECT S_ID ,V_ID  FROM STATIONS WHERE S_NAME= &S_NAME 
    AND V_ID = (SELECT V_ID FROM VEHICLES WHERE V_NAME = &V_NAME))
    WHERE ROWNUM = 1;

    INSERT INTO ORDERS VALUES(OD,CD,SD,VD);
END;
/

EXECUTE USER_RECORD;

SELECT *FROM ORDERS;

SELECT C_ID FROM (SELECT *FROM CUSTOMERS
ORDER BY C_ID DESC) WHERE ROWNUM = 1; 

SELECT S_ID FROM STATIONS 
WHERE S_NAME = &S_NAME AND 
V_ID = (SELECT V_ID FROM VEHICLES WHERE V_ID = &V_ID); 

SELECT S_ID FROM STATIONS WHERE S_NAME= &S_NAME;

SELECT V_ID FROM VEHICLES WHERE V_NAME = &V_NAME; 

SELECT *FROM (SELECT S_ID ,V_ID  FROM STATIONS WHERE S_NAME= &S 
AND V_ID = (SELECT V_ID FROM VEHICLES WHERE V_NAME = &V_NAME))
WHERE ROWNUM = 1;

SELECT COUNT(O_ID) FROM ORDERS;



CREATE TABLE STATIONS_Backup(
    S_ID INT NOT NULL,
    S_NAME VARCHAR2(30),
    LOCATION VARCHAR2(50),
    V_ID INT,
    PRIMARY KEY(S_ID),
    FOREIGN KEY (V_ID) REFERENCES VEHICLES(V_ID)
);


CREATE OR REPLACE TRIGGER TRG_Stations
    BEFORE DELETE ON STATIONS
    FOR EACH ROW
    BEGIN
        INSERT INTO STATIONS_Backup (S_Id,S_NAME,LOCATION,V_ID)
        SELECT S_Id,S_NAME,LOCATION,V_ID FROM STATIONS;
    END;
/

DELETE FROM STATIONS WHERE S_ID=1;