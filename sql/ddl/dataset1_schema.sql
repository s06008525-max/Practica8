-- DDL Dataset 1: Netflix normalizado a 3FN

CREATE TABLE shows (
    show_id VARCHAR(20) PRIMARY KEY,
    type VARCHAR(20),
    title VARCHAR(255),
    date_added VARCHAR(50),
    release_year INT,
    rating VARCHAR(15),
    duration VARCHAR(50),
    description TEXT
);

CREATE TABLE directors (
    director_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE actors (
    actor_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE countries (
    country_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE show_director (
    show_id VARCHAR(20) REFERENCES shows(show_id),
    director_id INT REFERENCES directors(director_id),
    PRIMARY KEY (show_id, director_id)
);

CREATE TABLE show_actor (
    show_id VARCHAR(20) REFERENCES shows(show_id),
    actor_id INT REFERENCES actors(actor_id),
    PRIMARY KEY (show_id, actor_id)
);

CREATE TABLE show_country (
    show_id VARCHAR(20) REFERENCES shows(show_id),
    country_id INT REFERENCES countries(country_id),
    PRIMARY KEY (show_id, country_id)
);

CREATE TABLE show_genre (
    show_id VARCHAR(20) REFERENCES shows(show_id),
    genre_id INT REFERENCES genres(genre_id),
    PRIMARY KEY (show_id, genre_id)
);
