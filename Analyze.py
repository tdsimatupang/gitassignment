import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def import_data():
    """
    Import data from the TTC Bus Delay dataset
    """
    return pd.read_csv('ttc-bus-delay-data-2023.csv')


def compute_avg_delay(data):
    """
    Compute the average delay for each route
    """
    return data.groupby('Route')['Min Delay'].mean().reset_index()


def main():
    """
    Main function
    """
    data = import_data()
    avg_delay = compute_avg_delay(data)

    plt.hist(avg_delay['Min Delay'], bins=30)
    plt.title('Average Delay Distribution')
    plt.xlabel('Average Delay (minutes)')


if __name__ == '__main__':
    main()
