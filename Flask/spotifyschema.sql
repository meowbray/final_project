CREATE TABLE Spotify_Data (
  pos INT NOT NULL,
  artist_title  character varying (155),
  wks character varying (5),
  t INT  NULL,
  pk INT  NULL,
  pkstreams INT NULL,
  total INT NOT NULL,
  track character varying(155), 
  track_id character varying (155),
  danceability FLOAT NOT NULL ,
  energy FLOAT NOT NULL ,
  key INT NOT NULL ,
  loudness FLOAT NOT NULL ,
  mode INT NOT NULL ,
  speechiness FLOAT NOT NULL,
  acoustiness FLOAT NOT NULL,
  instrumentalness FLOAT NOT NULL,
  liveness FLOAT NOT NULL,
  valence FLOAT NOT NULL,
  tempo FLOAT NOT NULL,
  duration_ms INT NOT NULL,
  time_signature INT NOT NULL
);

drop table spotify_data;