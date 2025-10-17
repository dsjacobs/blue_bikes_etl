from etl_helpers import lnd, run_sql

src_url = "https://s3.amazonaws.com/hubway-data/202504-bluebikes-tripdata.zip"
lnd(src_url)
run_sql("schema.sql")
