# Notes on setting up OpenSSL and DPDK in order to run crypto performance tests

## Tools and libraries required
AArch64cryptolib - Crypto primitives lib for AArch64 platforms
OpenSSL - Used by DPDK for crypto operations
DPDK - Building DPDK builds an app called `dpdk-test-crypto-perf` which is used for the testing

## Preparing AArch64cryptolib for use with DPDK
Clone the latest development version from the github repo. When building with `make` you must provide a value to the `OPT`variable which on AArch64 Neoverse N1 platforms is `big`:
`make OPT=big`
You must then export the `PKG_CONFIG_PATH` variable such that the OS knows where to find the package config files for AArch64cryptolib:
`export PKG_CONFIG_PATH=/home_local/thodau01/repos/AArch64cryptolib/pkgconfig/:$PKG_CONFIG_PATH`

## Preparing OpenSSL for use with DPDK
We need to build the latest dev version of OpenSSL and install it somewhere that doesn't overwrite the system OpenSSL.
Clone the latest OpenSSL on github and then run the following from the project root:
`./config --prefix=/home_local/thodau01/software/openssl_install --openssldir=/home_local/thodau01/software/openssl_install`

After configuring is successful, build the project:
`make -j$(nproc)`
`make install -j$(nproc)`

## Cross-compiling OpenSSL Linux x86 -> Aarch64
The following command will cross-compile for aarch64 with static linking:
`./Configure linux-aarch64 --cross-compile-prefix=/home/thodau01/opt/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu- --prefix=/home/thodau01/repos/openssl/main/openssl --openssldir=/home/thodau01/repos/openssl/main/openssl -static`

## Building DPDK
### Dependencies:
There are several dependencies that must be installed to build DPDK:
Meson build system: `python3 -m pip install --user meson`
Ninja-build: `apt-get install ninja-build`
Libs: `sudo apt install libdpdk-dev`

### Build commands:
With dependencies installed, you can now run the following from the `dpdk` project root:
`meson setup build` or for release mode `meson setup build -Dbuildtype=release` or optionally `meson setup build -Dbuildtype=debug`
`ninja -C build`

With OpenSSL installed to the directory above, use the following setup command in dpdk so the dpdk can detect the dev version of OpenSSL (as opposed to the system version):
`PKG_CONFIG_PATH=/home_local/thodau01/software/openssl_install/lib/pkgconfig/ PKG_CONFIG_LIBDIR=/home_local/thodau01/software/openssl_install/lib/ meson setup build -Dbuildtype=release`

### Setting up hugepages for running the DPDK tests
You need to configure hugepages in order to set aside enough memory for the large number of packets that are used in DPDKs tests. DPDK provides a script for this, but there is also a manual way to do it as well. 
Using the script:
`sudo usertools/dpdk-hugepages.py --reserve 1G`
Or manually:
`echo 1024 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages`
You can verify the number of hugepages that have been reserved with:
`cat /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages`

Once the hugepages have been set aside you then need to mount them which you can also do with the DPDK script:
`sudo usertools/dpdk-hugepages.py --mount`

Once mounted you can now run the tests.

## Running tests with DPDK
### AArch64cryptolib DPDK perf test
`sudo build/app/dpdk-test-crypto-perf --socket-mem 1024,0 --legacy-mem --vdev crypto_armv8 -l 3,4 -n 4 -- --buffer-sz 32,64,128,256,512,1024,2048,4096,8192 --optype cipher-then-auth --ptest throughput --auth-key-sz 64 --cipher-key-sz 16 --cipher-iv-sz 16 --auth-op generate --burst-sz 32 --total-ops 10000000 --silent --digest-sz 12 --auth-algo sha1-hmac --cipher-algo aes-cbc --cipher-op encrypt --devtype crypto_armv8`

### OpenSSL PMD tests
`sudo -E DPDK_TEST="cryptodev_openssl_autotest" LD_LIBRARY_PATH=/home_local/thodau01/software/openssl_install/lib build/app/dpdk-test -n 4 -l 2-3 --vdev "crypto_openssl" &> tests.txt`
These tests should all pass.

### Run the OpenSSL DPDK Perf Test
`sudo build/app/dpdk-test-crypto-perf --socket-mem 1024,0 --legacy-mem --vdev crypto_openssl -l 3,4 -n 4 -- --buffer-sz 32,64,128,256,512,1024,2048,4096,8192 --optype cipher-then-auth --ptest throughput --auth-key-sz 64 --cipher-key-sz 16 --cipher-iv-sz 16 --auth-op generate --burst-sz 32 --total-ops 10000000 --silent --digest-sz 12 --auth-algo sha1-hmac --cipher-algo aes-cbc --cipher-op encrypt --devtype crypto_openssl`

Notes:
- `--buffer-sz` can be adjusted as needed.
- Decryption can be tested by modifying the parameters appropriately.
- `-l` adjusts the number of cores.
- Other test types are available such as latency; the test above is for throughput. The `--ptest` parameter adjusts this.

## Apply Fangming's Interleaving patch to OpenSSL and DPDK
Fangming carried out some work that enabled `AES_CBC_HMAC_SHA` to use an interleaving technique when computing the cipher text and tag. In order to use this work we must apply a patch to the version of OpenSSL we are using, and then we must apply a second patch to DPDK to enable it to use these changes in OpenSSL. The patches are located at:
- OpenSSL: `https://gerrit.oss.arm.com/c/enterprise-llt/openssl/+/286860`
- DPDK: `https://gerrit.oss.arm.com/c/enterprise-network/dpdk/+/295830`

## Producing Flamegraphs
The data for flamegraphs is recorded using linux CLI tool `perf`. The data output from `perf` is then fed into a program called `Hotspot` which produces the flamegraphs.
Hotspot can be installed on Ubuntu with `sudo apt install hotspot`.

## Building DPDK for flamegraphs
DPDK needs to be built in the `debugoptimized` configuration in order to have debug symbols (required to produce flamegraphs). Additionally, better results are obtained when the CFLAG `-fno-omit-frame-pointer` is supplied at the `meson` setup stage. The below section provides the commands required for doing this. 

## Building DPDK for measurements with `perf`
First we need to export the PKG_CONFIG_PATH and PKG_CONFIG_LIBDIR variables so that `dpdk` can find the `AArch64cryptolib`and `OpenSSL` programs.
`export PKG_CONFIG_PATH=/home_local/thodau01/repos/AArch64cryptolib/pkgconfig/:$PKG_CONFIG_PATH`
`export PKG_CONFIG_PATH=/home_local/thodau01/software/openssl_install/lib/pkgconfig/:$PKG_CONFIG_PATH`
`export PKG_CONFIG_LIBDIR=/home_local/thodau01/software/openssl_install/lib/:$PKG_CONFIG_LIBDIR`

Now use `meson` to configure the build:
`CFLAGS=-fno-omit-frame-pointer meson setup build -Dbuildtype=debugoptimized`

Then build:
`ninja -C build`

## Making measurements with `perf`
`sudo perf record --call-graph fp -o ../../perf_data/perf-armv8-aes-cbc-128-sha1-hmac-32-buf.data ./build/app/dpdk-test-crypto-perf --socket-mem 1024,0 --legacy-mem --vdev crypto_armv8 -l 3,4 -n 4 -- --buffer-sz 32 --optype cipher-then-auth --ptest throughput --auth-key-sz 64 --cipher-key-sz 16 --cipher-iv-sz 16 --auth-op generate --burst-sz 32 --total-ops 10000000 --silent --digest-sz 12 --auth-algo sha1-hmac --cipher-algo aes-cbc --cipher-op encrypt --devtype crypto_armv8 --csv-friendly`
