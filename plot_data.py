#!/usr/bin/python3
import csv
import sys
import matplotlib.pyplot as plt

OPENSSL_BASE_FILE_NAME = "./results/OpenSSL_v3-4-0dev_results.csv"
OPENSSL_INTERLEAVING_FILE_NAME = "./results/OpenSSL_v3-4-0dev_interleaving_results.csv"
AARCH64CRYPTOLIB_FILE_NAME = "./results/AArch64cryptolib_results.csv"

OPENSSL_BASE_SERIES_NAME = "OpenSSL_base"
OPENSSL_INTERLEAVING_SERIES_NAME = "OpenSSL_interleaving"
AARCH64CRYPTOLIB_SERIES_NAME = "AArch64cryptolib"

X_DATA_LABEL = "Buffer Size (B)"
Y_DATA_LABEL = "Thoughput (Gbps)"

class DataSeries:
    def __init__(self, file_name, series_name):
        self.file_name = file_name
        self.series_name = series_name
        self.load_csv_data(self.file_name)

    def load_csv_data(self, file_name):
        with open(self.file_name, newline='') as file:
            reader = csv.reader(file)
            self.data = list(reader)
            self.x_data = list()
            self.y_data = list()
            for pair in self.data:
                self.x_data.append(int(pair[0]))
                self.y_data.append(float(pair[1]))

def main():
    print("Plotting data...")

    openssl_base_series = DataSeries(OPENSSL_BASE_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)
    aarch64cryptolib_series = DataSeries(AARCH64CRYPTOLIB_FILE_NAME, AARCH64CRYPTOLIB_SERIES_NAME)


    complete_data_series = [openssl_base_series, openssl_interleaving_series, aarch64cryptolib_series]
    colours = ['r', 'b', 'g']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='o', c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA1 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("results.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    sys.exit(main())