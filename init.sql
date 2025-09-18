CREATE DATABASE wine_db;

\connect wine_db;

CREATE TABLE wines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    rating FLOAT,
    year VARCHAR(100),
    goes_with TEXT[],
    descript VARCHAR(100)
);
