from etl_helpers import lnd

src_url = "https://s3.amazonaws.com/hubway-data/202504-bluebikes-tripdata.zip"
lnd(src_url)