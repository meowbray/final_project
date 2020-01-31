DROP TABLE spotify;

CREATE TABLE IF NOT EXISTS spotify (
    track_id VARCHAR NOT NULL PRIMARY KEY,
    danceability FLOAT(30) NOT NULL,
    energy FLOAT(30) NOT NULL,
    key INTEGER NOT NULL,
    loudness FLOAT(50) NOT NULL,
    mode INTEGER NOT NULL,
    speechiness FLOAT(30) NOT NULL,
    acousticness FLOAT(30) NOT NULL,
    instrumentalness VARCHAR(30) NOT NULL,
    liveness FLOAT(30) NOT NULL,
    valence FLOAT(30) NOT NULL,
    tempo FLOAT(30) NOT NULL,
    duration_ms INTEGER NOT NULL,
    time_signature INTEGER NOT NULL,
    pos INTEGER NOT NULL,
    artistit_and_title VARCHAR(200) NOT NULL,
    wks INTEGER NOT NULL,
    t10 VARCHAR(40),
    pk INTEGER NOT NULL,
    weeks_in_top_ten VARCHAR(30),
    pkstreams INTEGER NOT NULL,
    total INTEGER NOT NULL,
    track VARCHAR(200)

);

CREATE TABLE IF NOT EXISTS million (
        track_id VARCHAR NOT NULL PRIMARY KEY,
    danceability FLOAT(30) NOT NULL,
    energy FLOAT(30) NOT NULL,
    key INTEGER NOT NULL,
    loudness FLOAT(50) NOT NULL,
    mode INTEGER NOT NULL,
    speechiness FLOAT(30) NOT NULL,
    acousticness FLOAT(30) NOT NULL,
    instrumentalness VARCHAR(30) NOT NULL,
    liveness FLOAT(30) NOT NULL,
    valence FLOAT(30) NOT NULL,
    tempo FLOAT(30) NOT NULL,
    duration_ms INTEGER NOT NULL,
    time_signature INTEGER NOT NULL,
    pos INTEGER NOT NULL,
    artistit_and_title VARCHAR(200) NOT NULL,
    wks INTEGER NOT NULL,
    t10 VARCHAR(40),
    pk INTEGER NOT NULL,
    weeks_in_top_ten VARCHAR(30),
    pkstreams INTEGER NOT NULL,
    total INTEGER NOT NULL,
    track VARCHAR(200) NOT NULL

);

