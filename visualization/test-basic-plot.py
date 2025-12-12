import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_path = "../database/nyc-data.db"

def plot_sql_data():

    conn = sqlite3.connect(db_path)
    query = "SELECT * from Manhattan_CentralPark"

    df = pd.read_sql_query(query, conn)
    conn.close()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    plt.figure(figsize=(12, 6))
    plt.plot(df["Timestamp"], df["Temperature"], label="Temperature")
    plt.plot(df["Timestamp"], df["Humidity"], label="Humidity")
    plt.plot(df["Timestamp"], df["Population"], label="Population")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.title("Temperature, Humidity, and Population Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    

if __name__ == "__main__":
    plot_sql_data()
