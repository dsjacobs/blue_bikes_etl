import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def station_analysis():
    conn = sqlite3.connect("sqlite_db/bluebikes.db")

    stations = pd.read_sql_query("SELECT * FROM stations", conn)
    rides = pd.read_sql_query("SELECT * FROM rides", conn)

    rides["started_at_ts"] = pd.to_datetime(rides["start_ts"])
    rides["hour"] = rides["started_at_ts"].dt.hour
        
    def commuter_time(hour):
        if  7 < hour < 9:
            return 1
        if 16 < hour < 18:
            return 1
        else:
            return 0
        
    rides["commuter_hours"] = rides["hour"].apply(commuter_time)

    by_station = rides.groupby(["start_station_id","commuter_hours"])["ride_id"].count().reset_index()
    by_station["station_id"] = by_station["start_station_id"]
    stations["station_id"] = stations["id"]
    by_station = pd.merge(by_station,stations,on="station_id")
    by_station_and_commute = by_station[["station_name","ride_id","commuter_hours"]]

    total_rides_per_station = by_station.groupby("station_name")["ride_id"].sum()
    top_20 = total_rides_per_station.nlargest(20).index
    by_station_top20 = by_station[by_station["station_name"].isin(top_20)]
    by_station_top20 = by_station_top20[["commuter_hours","station_name","ride_id"]]
    by_station_top20 = by_station_top20.pivot(
        index="station_name", 
        columns="commuter_hours", 
        values="ride_id"
    )
    ax = by_station_top20.plot.bar(stacked=True)
    fig = ax.get_figure()
    fig.savefig('top_20_stations.png',bbox_inches='tight')

