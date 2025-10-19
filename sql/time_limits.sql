DROP TABLE IF EXISTS time_limits_query;
CREATE TABLE time_limits_query AS
WITH ride_lengths AS (
SELECT ride_id,
	rideable_type,
	member_casual,
	end_ts,
	start_ts,
	CASE WHEN ((JULIANDAY(end_ts) - JULIANDAY(start_ts)) * 24 * 60)  < 45 THEN "under 45 min"
		ELSE "over 45 min" END over45m
FROM rides
)
SELECT rideable_type,
	member_casual,
	over45m,
	count(distinct ride_id) ride_count
FROM ride_lengths
GROUP BY 1,2,3
ORDER BY 1,2,3;