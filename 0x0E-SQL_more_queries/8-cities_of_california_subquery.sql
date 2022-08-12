-- lists all the cities of Californiag
USE 
SELECT cities.* FROM cities where cities.state_id IN ( SELECT states.id FROM states WHERE states.name = 'California' ) ORDER BY cities.id