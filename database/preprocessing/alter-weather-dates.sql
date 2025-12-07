ALTER TABLE nyc_weather_historic ADD COLUMN date;

UPDATE nyc_weather_historic SET date = datetime(
    "Year" || '-' ||
    printf('%02d', "Month") || '-' ||
    printf('%02d', "Day") || ' ' ||
    printf('%02d', "Hour") || ':00:00'
);

CREATE TABLE weather_new AS
SELECT
	"Location",
    "date" AS "Date",
    "Temperature",
    "Humidity"
    
FROM nyc_weather_historic;

DROP TABLE nyc_weather_historic;

ALTER TABLE weather_new RENAME TO nyc_weather_historic;

