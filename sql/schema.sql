DROP TABLE IF EXISTS stations;
CREATE TABLE stations AS 
    SELECT DISTINCT start_station_id AS id,
        start_station_name AS station_name
    FROM lnd
    UNION SELECT end_station_id,
        end_station_name
    FROM lnd;

CREATE INDEX ix_station on stations (id);

DROP TABLE IF EXISTS rides;
CREATE TABLE rides AS 
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