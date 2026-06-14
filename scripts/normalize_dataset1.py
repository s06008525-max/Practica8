import pandas as pd
import os

RAW_FILE = '/app/data/raw/netflix.csv'
NORM_DIR = '/app/data/normalized/dataset1/'
DDL_FILE = '/app/sql/ddl/dataset1_schema.sql'

os.makedirs(NORM_DIR, exist_ok=True)
os.makedirs(os.path.dirname(DDL_FILE), exist_ok=True)

print("Normalización de Netflix")
df = pd.read_csv(RAW_FILE)

for col in ['director', 'cast', 'country', 'listed_in']:
    df[col] = df[col].fillna('Unknown')

def extract_entity(dataframe, column_name, entity_name):
    print(f"Normalizando {column_name}...")
    exploded = dataframe[['show_id', column_name]].copy()
    exploded[column_name] = exploded[column_name].apply(lambda x: [item.strip() for item in str(x).split(',')])
    exploded = exploded.explode(column_name)
    exploded = exploded[exploded[column_name] != 'Unknown'] 
    
    unique_items = exploded[column_name].unique()
    catalog_df = pd.DataFrame(unique_items, columns=['name'])
    catalog_df.index.name = f'{entity_name}_id'
    catalog_df.reset_index(inplace=True)
    catalog_df[f'{entity_name}_id'] += 1 
    
    relation_df = exploded.merge(catalog_df, left_on=column_name, right_on='name')
    relation_df = relation_df[['show_id', f'{entity_name}_id']]
    
    return catalog_df, relation_df

directors_df, show_director_df = extract_entity(df, 'director', 'director')
actors_df, show_actor_df = extract_entity(df, 'cast', 'actor')
countries_df, show_country_df = extract_entity(df, 'country', 'country')
genres_df, show_genre_df = extract_entity(df, 'listed_in', 'genre')

print("Limpiar tabla Shows")
shows_df = df[['show_id', 'type', 'title', 'date_added', 'release_year', 'rating', 'duration', 'description']].copy()

print("Export a CSVs data/normalized/dataset1/")
shows_df.to_csv(os.path.join(NORM_DIR, 'shows.csv'), index=False)
directors_df.to_csv(os.path.join(NORM_DIR, 'directors.csv'), index=False)
show_director_df.to_csv(os.path.join(NORM_DIR, 'show_director.csv'), index=False)
actors_df.to_csv(os.path.join(NORM_DIR, 'actors.csv'), index=False)
show_actor_df.to_csv(os.path.join(NORM_DIR, 'show_actor.csv'), index=False)
countries_df.to_csv(os.path.join(NORM_DIR, 'countries.csv'), index=False)
show_country_df.to_csv(os.path.join(NORM_DIR, 'show_country.csv'), index=False)
genres_df.to_csv(os.path.join(NORM_DIR, 'genres.csv'), index=False)
show_genre_df.to_csv(os.path.join(NORM_DIR, 'show_genre.csv'), index=False)

print("script DDL de SQL...")
ddl_script = """-- DDL Dataset 1: Netflix normalizado a 3FN

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
"""

with open(DDL_FILE, 'w', encoding='utf-8') as f:
    f.write(ddl_script)

print("\nNetflix actualizado 'normalized' y 'sql/ddl'")