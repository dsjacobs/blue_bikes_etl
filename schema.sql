CREATE TABLE stations AS (
    SELECT DISTINCT start_station_id AS id,
        start_station_name AS station_name 
    FROM lnd
    UNION SELECT end_station_id,
        end_station_name
    FROM lnd
);

CREATE TABLE rides AS (
SELECT 
    ride_id,
    rideable_type,
    started_at,
    ended_at,
    start_station_id,
    end_station_id,
    member_casual
FROM lnd
);