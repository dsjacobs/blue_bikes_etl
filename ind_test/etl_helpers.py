import requests
from zipfile import ZipFile
import sqlite3
import os
import pandas as pd
from analysis import station_analysis

cur_dir = os.getcwd()
csv_path = "lnd/202504-bluebikes-tripdata.csv"
lnd_folder = os.path.join(cur_dir,"lnd")
db_folder = os.path.join(cur_dir,"sqlite_db")
conn = sqlite3.connect(os.path.join(db_folder,"bluebikes.db"))
      
def run_sql_folder(conn, folder, file_list):
    for file in file_list:
        path = os.path.join(folder, file)
        with open(path, "r") as f:
            sql = f.read()
        conn.executescript(sql)

def run_sql(path):
    with open(path, "r") as f:
        sql = f.read()
    conn.executescript(sql)  

def lnd(src_url):
    lnd_folder = os.path.join(cur_dir,"lnd")
    os.makedirs(lnd_folder, exist_ok=True)
    response = requests.get(src_url)
    zip_download_path = os.path.join(lnd_folder,'LND.zip')

    if response.status_code == 200:
        with open(zip_download_path, 'wb') as file:
            file.write(response.content)

    with ZipFile(zip_download_path) as zipObject:
        zipObject.extractall(lnd_folder)

    os.makedirs(db_folder, exist_ok=True)
    df = pd.read_csv(csv_path)
    df.to_sql('LND',conn,if_exists="replace")


def run_sql_analysis():
    run_sql("busy_stations.sql")
    run_sql("time_limits.sql")
    station_analysis()
