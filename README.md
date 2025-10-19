run "Python3 etl.py"
(Prerequisites: matplotlib, sqlite3, and pandas)

I picked Blue Bikes (the rideshare bikes in Boston) as they are of local interest to me, and I picked the most recent month over 10MB, April 2025.

Documentation: https://bluebikes.com/system-data

Question 1: Which stations have the most difference in bikes taken out and bikes returned on the same day? 
This could help BlueBikes determine where to bus bikes to and from.

BlueBikes is already likely driving bikes to these locations, which is how it's possible to have more bikes taken than returned. Where should they continue to focus their efforts?

Question 2: Are members taking advantage of their benefits (unlimited under 45 min rides, and a discounted rate on ebikes) compared to casual riders? Do members or non members tend to take more under or over 45m rides and ebikes?

Members are more active than casual riders in all categories, are more likely to take ebikes, and are more likely to stay under the 45 minute limit.

Question 3: Which stations are the most popular, and are they frequented more often than not during commuter hours?

How much of the most popular activity on the BlueBike network happens during commuter housrs (7-9a, 4-6p), and where?