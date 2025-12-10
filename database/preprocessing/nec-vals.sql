CREATE TABLE Queens_LaGuardia_weather AS SELECT
    datetime(
        "Year" || '-' ||
        printf('%02d', "Month") || '-' ||
        printf('%02d', "Day") || ' ' ||
        printf('%02d:00:00', "Hour")
    ) AS Timestamp,
    "Ta" AS Temperature,
    "RH" AS Humidity
FROM S725030 
;

CREATE TABLE Manhattan_CentralPark_weather AS SELECT
    datetime(
        "Year" || '-' ||
        printf('%02d', "Month") || '-' ||
        printf('%02d', "Day") || ' ' ||
        printf('%02d:00:00', "Hour")
    ) AS Timestamp,
    "Ta" AS Temperature,
    "RH" AS Humidity
FROM S725033
;

CREATE TABLE Brooklyn_JFK_weather AS SELECT
    datetime(
        "Year" || '-' ||
        printf('%02d', "Month") || '-' ||
        printf('%02d', "Day") || ' ' ||
        printf('%02d:00:00', "Hour")
    ) AS Timestamp,
    "Ta" AS Temperature,
    "RH" AS Humidity
FROM S744860
;

