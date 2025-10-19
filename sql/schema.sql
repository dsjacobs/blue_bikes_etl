CREATE TABLE IF NOT EXISTS stations AS 
    SELECT DISTINCT start_station_id AS id,
        start_station_name AS station_name,
        start_lat AS lat,
        start_lng AS long 
    FROM lnd
    UNION SELECT end_station_id,
        end_station_name,
        end_lat AS lat,
        end_lng AS long
    FROM lnd;

CREATE INDEX ix_station on stations (station_id);

CREATE TABLE IF NOT EXISTS rides AS 
SELECT 
    ride_id,
    rideable_type,
    started_at AS start_ts,
    ended_at AS end_ts,
    start_station_id,
    end_station_id,
    member_casual
FROM lnd;

CREATE INDEX ix_rides on rides (ride_id)