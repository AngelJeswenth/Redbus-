CREATE DATABASE REDBUS_DETAILS;

use REDBUS_DETAILS;

CREATE TABLE BUS_ROUTES( ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
				        Bus_name TEXT, Bus_type TEXT, Start_time VARCHAR(255),
                        End_time VARCHAR(255),Total_duration TEXT,
                        Price DECIMAL,Seats_Available INT,
                        Ratings FLOAT,Route_link TEXT,Route_name TEXT);
                        
 Select * From BUS_ROUTES;    
 
 select * from Final_busdetails_df;
 
 DESCRIBE BUS_ROUTES;

 SHOW COLUMNS FROM BUS_ROUTES;
 SELECT COUNT(*) 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'BUS_ROUTES' 
AND table_schema = 'REDBUS_DETAILS';

SELECT COUNT(*) FROM BUS_ROUTES;

DELETE FROM BUS_ROUTES WHERE ID IS NULL;

Select * From BUS_ROUTES;  

SELECT COUNT(*) AS total_count
FROM BUS_ROUTES
WHERE Ratings = 0;





