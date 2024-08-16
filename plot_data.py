#!/usr/bin/python3
import csv
import sys
import matplotlib.pyplot as plt

OPENSSL_BASE_AES128_SHA1_FILE_NAME = "./results/OpenSSL_aes_cbc_128_sha1_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES128_SHA1_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_128_sha1_hmac_encrypt.csv"
AARCH64CRYPTOLIB_AES128_SHA1_FILE_NAME = "./results/AArch64cryptolib_aes_cbc_128_sha1_hmac_encrypt.csv"

OPENSSL_BASE_AES128_SHA256_FILE_NAME = "./results/OpenSSL_aes_cbc_128_sha256_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES128_SHA256_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_128_sha256_hmac_encrypt.csv"
AARCH64CRYPTOLIB_AES128_SHA256_FILE_NAME = "./results/AArch64cryptolib_aes_cbc_128_sha256_hmac_encrypt.csv"

OPENSSL_BASE_AES256_SHA1_FILE_NAME = "./results/OpenSSL_aes_cbc_256_sha1_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES256_SHA1_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_256_sha1_hmac_encrypt.csv"

OPENSSL_BASE_AES256_SHA256_FILE_NAME = "./results/OpenSSL_aes_cbc_256_sha256_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES256_SHA256_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_256_sha256_hmac_encrypt.csv"

OPENSSL_BASE_AES128_SHA512_FILE_NAME = "./results/OpenSSL_aes_cbc_128_sha512_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES128_SHA512_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_128_sha512_hmac_encrypt.csv"

OPENSSL_BASE_AES256_SHA512_FILE_NAME = "./results/OpenSSL_aes_cbc_256_sha512_hmac_encrypt.csv"
OPENSSL_INTERLEAVING_AES256_SHA512_FILE_NAME = "./results/OpenSSL_interleaving_aes_cbc_256_sha512_hmac_encrypt.csv"

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

    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA1_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)
    aarch64cryptolib_series = DataSeries(AARCH64CRYPTOLIB_AES128_SHA1_FILE_NAME, AARCH64CRYPTOLIB_SERIES_NAME)


    complete_data_series = [openssl_base_series, openssl_interleaving_series, aarch64cryptolib_series]
    colours = ['r', 'b', 'g']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA1 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha1.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA256_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)
    aarch64cryptolib_series = DataSeries(AARCH64CRYPTOLIB_AES128_SHA256_FILE_NAME, AARCH64CRYPTOLIB_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series, aarch64cryptolib_series]
    colours = ['r', 'b', 'g']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA256 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha256.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA1_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA1_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA1 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha1.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA256_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA256 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha256.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA512_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA512_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA512 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha512.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA512_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA512_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data, series.y_data, label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA512 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha512.png", dpi=300)
    plt.close()


########################################## Zoomed plots ##########################################

    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA1_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)
    aarch64cryptolib_series = DataSeries(AARCH64CRYPTOLIB_AES128_SHA1_FILE_NAME, AARCH64CRYPTOLIB_SERIES_NAME)


    complete_data_series = [openssl_base_series, openssl_interleaving_series, aarch64cryptolib_series]
    colours = ['r', 'b', 'g']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA1 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha1_zoomed.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA256_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)
    aarch64cryptolib_series = DataSeries(AARCH64CRYPTOLIB_AES128_SHA256_FILE_NAME, AARCH64CRYPTOLIB_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series, aarch64cryptolib_series]
    colours = ['r', 'b', 'g']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA256 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha256_zoomed.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA1_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA1_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA1 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha1_zoomed.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA256_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA256_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA256 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha256_zoomed.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES128_SHA512_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES128_SHA512_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_128_HMAC_SHA512 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes128_sha512_zoomed.png", dpi=300)
    plt.close()



    openssl_base_series = DataSeries(OPENSSL_BASE_AES256_SHA512_FILE_NAME, OPENSSL_BASE_SERIES_NAME)
    openssl_interleaving_series = DataSeries(OPENSSL_INTERLEAVING_AES256_SHA512_FILE_NAME, OPENSSL_INTERLEAVING_SERIES_NAME)

    complete_data_series = [openssl_base_series, openssl_interleaving_series]
    colours = ['r', 'b']


    for series, colour in zip(complete_data_series, colours):
        plt.plot(series.x_data[0:6], series.y_data[0:6], label=series.series_name, marker='.', markersize=3, c=colour)
    # plt.yticks = series.y_data
    plt.figure(1)

    plt.grid(True)
    plt.title("AES_CBC_256_HMAC_SHA512 - Encrypt: Buffer size vs. Throughput")
    plt.xlabel(X_DATA_LABEL)
    plt.ylabel(Y_DATA_LABEL)
    plt.legend()
    plt.savefig("./plots/aes256_sha512_zoomed.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    sys.exit(main())