-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Seldct database
USE hbtn_0d_usa;cities
-- Create table states
CREATE TABLE IF NOT EXISTS states (`id` INT PRIMARY KEY  NOT NULL AUTO_INCREMENT, `name` VARCHAR(256) NOT NULL);
-- CREATE TABLE cities
CREATE TABLE IF NOT EXISTS cities ('id' INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 'state_id' INT NOT NULL, 'name' VARCHAR(256), PRIMARY KEY ('id'), FOREIGN KEY ('state_id') REFERENCES states('id'));
