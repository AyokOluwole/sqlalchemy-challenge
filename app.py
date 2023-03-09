import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
       
    )




@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
#Convert the query results from your precipitation analysis 
#(i.e. retrieve only the last 12 months of data) to a dictionary 
#using date as the key and prcp as the value.

# Calculate the date one year from the last date in data set.
    lastdate = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores

#prep = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>lastdate).order_by(Measurement.date).all()
    prep = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= lastdate).all()

    session.close()

#


    return jsonify(prep)


############################################
#################
    
            

#id INTEGER
#station TEXT
#name TEXT
#latitude FLOAT
#longitude FLOAT
#elevation FLOAT



#active_stations = session.query(Measurement.station,func.count(Measurement.station)).\
                       #group_by(Measurement.station).\
                       #order_by(func.count(Measurement.station).desc()).all()
#active_stations


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    active_stations = session.query(Station.station, Station.name).all()
    return jsonify(active_stations)

###################################################
###################################################

#active  = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
                         #   filter(Measurement.date >= lastdate).all()
#active

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    active = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
                            filter(Measurement.date >= lastdate).all()
    return jsonify(active)

###################################################
###################################################




        
        
@app.route("/api/v1.0/<start>")

def start():

    session = Session(engine)

    low_high_avg = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date).all()
    return jsonify(low_high_avg)

    return jsonify(low_high_avg)












###################################################
###################################################




@app.route("/api/v1.0/<start>/<end>")

def startend (startend):
    session = Session(engine)

    low_high_startend = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(low_high_startend)











###################################################
###################################################

if __name__ == '__main__':
    app.run(debug=True)

