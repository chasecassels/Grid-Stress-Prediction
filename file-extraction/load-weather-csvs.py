import pandas as pd
import sqlite3
import os

folder_path = "../source-data"
db_path = "../database/nyc-data.db"
conn = sqlite3.connect(db_path)

#import all csvs into sqlite db
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        table_name = os.path.splitext(filename)[0]
        parts = table_name.split("_")
        output_table_name = f"{parts[0]}_{parts[1]}"
        df.to_sql(output_table_name, conn, if_exists="replace", index=False)
        print(f"Imported '{filename}' into table '{output_table_name}'", flush=True)

conn.commit()
conn.close()
print("All files imported successfully!", flush=True)
