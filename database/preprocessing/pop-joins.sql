CREATE TABLE Brooklyn_JFK AS SELECT
	a.*,
	b."0" AS Population
FROM
	Brooklyn_JFK_weather a
JOIN nyc_population b ON
	a."Timestamp" = b."index";

CREATE TABLE Manhattan_CentralPark AS SELECT
	a.*,
	b."1" AS Population
FROM
	Manhattan_CentralPark_weather a
JOIN nyc_population b ON
	a."Timestamp" = b."index";

CREATE TABLE Queens_LaGuardia AS SELECT
	a.*,
	b."2" AS Population
FROM
	Queens_LaGuardia_weather a
JOIN nyc_population b ON
	a."Timestamp" = b."index";