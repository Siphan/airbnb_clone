/*
   As it is crucial to distinguish between development and production environments,
   this script creates a user and a database specific for each environment.
*/

-- Create users for SQL Authentication
CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY ''; -- Can access to MySQL from anywhere
CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY ''; -- Can access to MySQL from only localhost

-- Create 2 databases in UTF8 (utf8_general_ci)
CREATE DATABASE airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Add user dev to database dev
GRANT ALL PRIVILEGES ON database.airbnb_dev TO 'airbnb_user_dev'@'%' IDENTIFIED BY '';

-- Add user prod to database prod
GRANT ALL PRIVILEGES ON	database.airbnb_prod TO 'airbnb_user_prod'@'localhost' IDENTIFIED BY '';
