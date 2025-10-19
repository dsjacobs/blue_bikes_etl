DROP TABLE IF EXISTS station_day_arrivals_departures;
CREATE TABLE station_day_arrivals_departures AS
WITH leaving AS (
	SELECT start_station_id AS station_id,
    	STRFTIME('%m', start_ts) AS ride_month,
		STRFTIME('%d', start_ts) AS ride_date,
		count(*) AS ride_count
	FROM rides
	GROUP BY 1,2,3
),
arriving AS (
	SELECT end_station_id AS station_id,
    	STRFTIME('%m', end_ts) AS ride_month,
		STRFTIME('%d', end_ts) AS ride_date,
		count(*) AS ride_count
	FROM rides
	GROUP BY 1,2,3
)
SELECT s.id station_id,
	s.station_name,
    leaving.ride_month || '-' || leaving.ride_date AS ride_date,
	leaving.ride_count bikes_left,
	arriving.ride_count bikes_returned
FROM stations s
LEFT JOIN leaving ON s.id = leaving.station_id
LEFT JOIN arriving ON s.id = arriving.station_id 
WHERE arriving.ride_month = leaving.ride_month
	AND arriving.ride_date = leaving.ride_date
;

DROP TABLE IF EXISTS station_surplus_deficits;
CREATE TABLE station_surplus_deficits AS
SELECT station_name,
	ROUND(AVG(bikes_left - bikes_returned),2) avg_bike_deficit
FROM station_day_arrivals_departures
GROUP BY station_name
ORDER BY AVG(bikes_left - bikes_returned) DESC
LIMIT 10;