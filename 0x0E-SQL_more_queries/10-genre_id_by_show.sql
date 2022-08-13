-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
SELECT CONCAT(`tv_shows.title`, '-', `tv_show_genres.genre_id`) 
FROM tv_shows INNER JOIN tv_show_genres 
ON  tv_show_genres.genre_id = tv_shows.show_genres_id
