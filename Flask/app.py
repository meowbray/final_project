import numpy as np
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from collections import OrderedDict
from flask import Flask, jsonify, Response, render_template
import psycopg2
from datetime import date, timedelta


#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:YOURPASSWORDHERE@localhost:5432/YOURDATABASEHERE')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    
    return render_template("Final_project.html")

@app.route("/viral_viz")

def viz():
    daily = "https://kworb.net/spotify/country/us_daily.html"
    viral = pd.read_html(daily)
    df=viral[0]
    df.sort_values(by='Days', ascending=True)
    drop_over_1day = df[df['Days'] > 15  ].index
    df.drop(drop_over_1day , inplace=True)
    viral_charts = df.to_json(orient='columns')

    return viral_charts

@app.route("/bday_group1")

def group1():
    data = engine.execute('SELECT * FROM spotify_data WHERE total > 80000000 ORDER BY total DESC LIMIT 100').fetchall()

    artist = []
    position = []
    total= []
    dance = []
    key= []
    mode=[]
    loudness=[]
    energy=[]
    acousticness=[]
    tempo=[]
    valence=[]
    liveness=[]
    weeks = []

    for x in data:
        act = x[1]
        post = x[0]
        tot = x[6]
        dnc = x[9]
        ky = x[11]
        mod = x[13]
        loud = x[12]
        en=x[10]
        auct=x[15]
        tmp=x[19]
        vl=x[18]
        live=x[17]
        week=x[2]
        artist.append(act)
        position.append(post)
        total.append(tot)
        dance.append(dnc)
        key.append(ky)
        mode.append(mod)
        loudness.append(loud)
        energy.append(en)
        acousticness.append(auct)
        tempo.append(tmp)
        valence.append(vl)
        liveness.append(live)
        weeks.append(week)

        # list(datetime_range(start=datetime(1967, 1, 1), end=datetime(1999, 12, 31)))
    song_data = {
        "artist" : artist,
        "postion" : position,
        "streams" : total,
        "dance" : dance,
        "key": key,
        "mode": mode,
        "loudness" : loudness,
        "energy" : energy,
        "acousticness" : acousticness,
        "tempo" : tempo,
        "valence" : valence,
        "liveness" : liveness,
        "weeks" : weeks
    }
     
    return jsonify(song_data)

@app.route("/one_song")
def one():
    data = engine.execute("SELECT * FROM spotify_data WHERE total < 1000000 AND wks < 2 LIMIT 50").fetchall()
    for x in data:
        artist = []
    position = []
    total= []
    dance = []
    key= []
    mode=[]
    loudness=[]
    energy=[]
    acousticness=[]
    tempo=[]
    valence=[]
    liveness=[]
    weeks = []

    for x in data:
        act = x[1]
        post = x[0]
        tot = x[6]
        dnc = x[9]
        ky = x[11]
        mod = x[13]
        loud = x[12]
        en=x[10]
        auct=x[15]
        tmp=x[19]
        vl=x[18]
        live=x[17]
        week=x[2]
        artist.append(act)
        position.append(post)
        total.append(tot)
        dance.append(dnc)
        key.append(ky)
        mode.append(mod)
        loudness.append(loud)
        energy.append(en)
        acousticness.append(auct)
        tempo.append(tmp)
        valence.append(vl)
        liveness.append(live)
        weeks.append(week)

        # list(datetime_range(start=datetime(1967, 1, 1), end=datetime(1999, 12, 31)))
    song_data = {
        "artist" : artist,
        "postion" : position,
        "streams" : total,
        "dance" : dance,
        "key": key,
        "mode": mode,
        "loudness" : loudness,
        "energy" : energy,
        "acousticness" : acousticness,
        "tempo" : tempo,
        "valence" : valence,
        "liveness" : liveness,
        "weeks" : weeks
    }
     
    return jsonify(song_data)

if __name__ == '__main__':
    app.run(debug=True)