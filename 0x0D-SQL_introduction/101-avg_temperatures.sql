-- Import in hbtn_0c_0 database this table dump
mysql -u root < temperatures.sql

-- Displays cities avg temperature in accord

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp`;
