import requests
from zipfile import ZipFile
import sqlite3
import os
import pandas as pd

cur_dir = os.getcwd()
csv_path = "lnd/202504-bluebikes-tripdata.csv"
db_pth = "sqlite/bluebikes.db"
conn = sqlite3.connect("bluebikes.db")
            
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

    response = requests.get(src_url)
    zip_download_path = 'LND.zip'

    if response.status_code == 200:
        with open(zip_download_path, 'wb') as file:
            file.write(response.content)

    with ZipFile(zip_download_path) as zipObject:
        zipObject.extractall(os.path.join(cur_dir,"lnd"))

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect("bluebikes.db")

    df.to_sql('LND',conn,if_exists="replace")