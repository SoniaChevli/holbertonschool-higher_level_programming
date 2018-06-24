-- uses hbtn_0d_tvshows to list all genres of the show dexter
SELECT name AS genre
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genre.id
JOIN tv_shows
WHERE tv_shows.title="Dexter"
ORDER BY tv_genres.name ASC;
