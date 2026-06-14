
- INSERTS tabla shows
INSERT INTO shows (show_id, type, title, date_added, release_year, rating, duration, description) VALUES ('s1', 'Movie', 'Dick Johnson Is Dead', 'September 25, 2021', '2020', 'PG-13', '90 min', 'As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.');
INSERT INTO shows (show_id, type, title, date_added, release_year, rating, duration, description) VALUES ('s2', 'TV Show', 'Blood & Water', 'September 24, 2021', '2021', 'TV-MA', '2 Seasons', 'After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.');
INSERT INTO shows (show_id, type, title, date_added, release_year, rating, duration, description) VALUES ('s3', 'TV Show', 'Ganglands', 'September 24, 2021', '2021', 'TV-MA', '1 Season', 'To protect his family from a powerful drug lord, skilled thief Mehdi and his expert team of robbers are pulled into a violent and deadly turf war.');
INSERT INTO shows (show_id, type, title, date_added, release_year, rating, duration, description) VALUES ('s4', 'TV Show', 'Jailbirds New Orleans', 'September 24, 2021', '2021', 'TV-MA', '1 Season', 'Feuds, flirtations and toilet talk go down among the incarcerated women at the Orleans Justice Center in New Orleans on this gritty reality series.');
INSERT INTO shows (show_id, type, title, date_added, release_year, rating, duration, description) VALUES ('s5', 'TV Show', 'Kota Factory', 'September 24, 2021', '2021', 'TV-MA', '2 Seasons', 'In a city of coaching centers known to train India’s finest collegiate minds, an earnest but unexceptional student and his friends navigate campus life.');

- INSERTS tabla directors
INSERT INTO directors (director_id, name) VALUES ('1', 'Kirsten Johnson');
INSERT INTO directors (director_id, name) VALUES ('2', 'Julien Leclercq');
INSERT INTO directors (director_id, name) VALUES ('3', 'Mike Flanagan');
INSERT INTO directors (director_id, name) VALUES ('4', 'Robert Cullen');
INSERT INTO directors (director_id, name) VALUES ('5', 'José Luis Ucha');

- INSERTS tabla actors
INSERT INTO actors (actor_id, name) VALUES ('1', 'Ama Qamata');
INSERT INTO actors (actor_id, name) VALUES ('2', 'Khosi Ngema');
INSERT INTO actors (actor_id, name) VALUES ('3', 'Gail Mabalane');
INSERT INTO actors (actor_id, name) VALUES ('4', 'Thabang Molaba');
INSERT INTO actors (actor_id, name) VALUES ('5', 'Dillon Windvogel');

- INSERTS tabla countries
INSERT INTO countries (country_id, name) VALUES ('1', 'United States');
INSERT INTO countries (country_id, name) VALUES ('2', 'South Africa');
INSERT INTO countries (country_id, name) VALUES ('3', 'India');
INSERT INTO countries (country_id, name) VALUES ('4', 'Ghana');
INSERT INTO countries (country_id, name) VALUES ('5', 'Burkina Faso');

- INSERTS tabla genres
INSERT INTO genres (genre_id, name) VALUES ('1', 'Documentaries');
INSERT INTO genres (genre_id, name) VALUES ('2', 'International TV Shows');
INSERT INTO genres (genre_id, name) VALUES ('3', 'TV Dramas');
INSERT INTO genres (genre_id, name) VALUES ('4', 'TV Mysteries');
INSERT INTO genres (genre_id, name) VALUES ('5', 'Crime TV Shows');

- INSERTS tabla show_director
INSERT INTO show_director (show_id, director_id) VALUES ('s1', '1');
INSERT INTO show_director (show_id, director_id) VALUES ('s3', '2');
INSERT INTO show_director (show_id, director_id) VALUES ('s6', '3');
INSERT INTO show_director (show_id, director_id) VALUES ('s7', '4');
INSERT INTO show_director (show_id, director_id) VALUES ('s7', '5');

- INSERTS tabla show_actor
INSERT INTO show_actor (show_id, actor_id) VALUES ('s2', '1');
INSERT INTO show_actor (show_id, actor_id) VALUES ('s2', '2');
INSERT INTO show_actor (show_id, actor_id) VALUES ('s2', '3');
INSERT INTO show_actor (show_id, actor_id) VALUES ('s2', '4');
INSERT INTO show_actor (show_id, actor_id) VALUES ('s2', '5');

- INSERTS tabla show_country
INSERT INTO show_country (show_id, country_id) VALUES ('s1', '1');
INSERT INTO show_country (show_id, country_id) VALUES ('s2', '2');
INSERT INTO show_country (show_id, country_id) VALUES ('s5', '3');
INSERT INTO show_country (show_id, country_id) VALUES ('s8', '1');
INSERT INTO show_country (show_id, country_id) VALUES ('s8', '4');

- INSERTS tabla show_genre
INSERT INTO show_genre (show_id, genre_id) VALUES ('s1', '1');
INSERT INTO show_genre (show_id, genre_id) VALUES ('s2', '2');
INSERT INTO show_genre (show_id, genre_id) VALUES ('s2', '3');
INSERT INTO show_genre (show_id, genre_id) VALUES ('s2', '4');
INSERT INTO show_genre (show_id, genre_id) VALUES ('s3', '5');
