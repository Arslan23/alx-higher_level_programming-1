-- lists all the cities of Californiag
USE @database_name;
SELECT cities.* FROM cities where name = 'California' ORDER BY cities.id