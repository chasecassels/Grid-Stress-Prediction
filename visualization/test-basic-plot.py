import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_manhattan():

    conn = sqlite3.connect("../database/nyc-data.db")
    query = "SELECT * from Manhattan_CentralPark"

    df = pd.read_sql_query(query, conn)
    conn.close()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(df["Timestamp"], df["Temperature"], label="Temperature", linewidth=2)
    ax1.set_xlabel("Timestamp")
    ax1.set_ylabel("Temperature")
    ax1.tick_params(axis='y')

    # Right y-axis (Population)
    ax2 = ax1.twinx()
    ax2.plot(df["Timestamp"], df["Population"], label="Population", color="green", linewidth=2)
    ax2.set_ylabel("Population")
    ax2.tick_params(axis='y')

    # Title
    plt.title("Temperature and Population Over Time")

    # Combined legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_manhattan()
