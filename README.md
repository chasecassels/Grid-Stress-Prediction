# NYC Grid Stress

Exploratory data analysis project to study how grid stress may change across NYC due to climate change, land use changes, population growth, and technological changes.

- [Data Ingestion](#ingest)
- [Preprocessing](#preproc)
- [ML](#ml)
- [Mapping and Visualization](#display)
- [To-dos](#to-dos)

---

## Data Ingestion

Ingest Historical NYC Weather Data from the Open Science Foundation API into an empty SQLite database:

```
$ touch database/nyc-data.db
$ cd file-extraction
$ bash weather-import.sh
```  

Temporally downscale (currently using basic linear interpolation) and ingest historic and future nyc population data:

```
$ python3 load-interp-pop-csv.py
```

---

## Preprocessing

Using a database manager or via command line, execute following sql scripts in order. The result will be 3 tables of hourly  
temperature, humiditity, and population data for Brooklyn (JFK), Manhattan (Central Park), and Queens (LaGuardia)

```
combine-source-tables.sql
nec-vals.sql
pop-joins.sql
```





---

## ML

Some inspiration:

https://www.sciencedirect.com/science/article/pii/S0306261923011479


---

## Mapping and Visulization

Basic weather/population plots

```
$ cd visualization
$ python3 test-basic-plot.py

---

## To-dos

Data sourcing:  

- [ ] Source land-use historical data and future data  
- [x] Source population historical and future data  
- [ ] Source grid use historical data  
- [ ] Source annual temperature rise projections  


Preprocessing:  
  
- [ ] Create future weather data tables (emulate format of historical data and use averages + projected increases to fill)  
- [ ] Temporally downscale population and land use data (pop data downscaling in progress) 
- [ ] Write and test Joins/Unions to create one comprehensive historical table and one comprehensive future table with an empty grid use column  


ML Research/Testing:  

- [ ] Research suitable models & mathematical justification (Random Forest / Neural Net / Time Series Models)  
- [ ] Write a python script for training on comprehensive historical table (Scikit-learn)  
- [ ] Write a script for predicting grid use column values based on training results  


Visualization:  

- [ ] Grafana?  



























