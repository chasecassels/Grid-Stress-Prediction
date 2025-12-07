import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os

folder_path = "../source-data"
db_path = "../database/nyc-data.db"
conn = sqlite3.connect(db_path)
file = 'New_York_City_Population_by_Borough,_1950_-_2040_20251203.csv'
df = pd.DataFrame()

#transpose and format input data
def process_input(df) -> pd.DataFrame:
    df = df.drop(df.columns[0], axis = 1)
    df = df.drop(df.columns[2::2], axis = 1)
    df_with_names = df.copy()
    df = df_with_names.T
    df = df.drop(df.columns[[0, 1, 5]], axis = 1)
    return df

#temporal downscaling to hours (unnecessary but why not), linear interpolation (improve later)
def interpolate(df) -> pd.DataFrame:
    df.index = df.index.astype(int)
    years = np.arange(1950, 2040+1)
    df_yearly = df.reindex(years)
    df_yearly = df_yearly.interpolate(method='linear')

    df_yearly.index = pd.to_datetime(df_yearly.index, format='%Y')

    df_hourly = df_yearly.resample('H').interpolate('linear')

    return df_hourly

#import population csv into sqlite db
for name in os.listdir(folder_path):
    if name == file:
        filename = name
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        df = process_input(df)
        table_name = os.path.splitext(filename)[0]

        parts = table_name.split("_")
        output_table_name = "nyc_population"
        df.index.values[0] = "Decade"

        df = df.set_axis(list(range(len(df.columns))), axis=1)
        df = df.iloc[1:].replace(',', '', regex=True).apply(pd.to_numeric, errors='coerce')
        df = interpolate(df)

        df.to_sql(output_table_name, conn, if_exists="replace", index=True)

        print(f"Imported '{filename}' into table '{output_table_name}'", flush=True)

if not df.empty:
    df.plot()
    plt.title("Line Plot of DataFrame")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.show()

conn.commit()
conn.close()
print("All files imported successfully!", flush=True)
