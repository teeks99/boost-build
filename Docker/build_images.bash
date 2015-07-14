
pushd gcc-4.8
docker build -t teeks99/gcc-4.8 .
popd
pushd gcc-4.9
docker build -t teeks99/gcc-4.9 .
popd
pushd gcc-5.1
docker build -t teeks99/gcc-5.1 .
popd


pushd clang-3.3
docker build -t teeks99/clang-3.3 .
popd
pushd clang-3.4
docker build -t teeks99/clang-3.4 .
popd
pushd clang-3.5
docker build -t teeks99/clang-3.5 .
popd
pushd clang-3.6
docker build -t teeks99/clang-3.6 .
popd
